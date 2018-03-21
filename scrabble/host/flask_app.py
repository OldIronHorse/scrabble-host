from flask import Flask, g, redirect, render_template, request, session,\
  url_for
from werkzeug.security import check_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId
from random import choice
from scrabble.game import new_game, draw_tiles, play_tiles
from scrabble.db import game_from_db, game_to_db

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
  SECRET_KEY='develeopment key',
  MONGO_DB_URI='mongodb://localhost:27017'))

def connect_db():
  return MongoClient(app.config['MONGO_DB_URI']).scrabble

def get_db():
  if not hasattr(g, 'scrabble_db'):
    g.scrabble_db = connect_db()
  return g.scrabble_db

@app.shell_context_processor
def make_app_shell_context():
  return {'get_db': get_db}

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    user = get_db().users.find_one({'name': request.form['username']})
    if user \
        and check_password_hash(user['password_hash'], 
                                request.form['password']):
      session['logged_in'] = user['name']
      return redirect(url_for('games'))
    error='Invalid username and password combination'
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  return redirect(url_for('games'))

@app.route('/')
def root():
  return redirect('/games')

@app.route('/games')
def games():
  return render_template('games.html', 
                         games=[(g['_id'], game_from_db(g))
                                for g
                                in get_db().games.find()])

@app.route('/games/<game_id>', methods=['GET', 'POST'])
def game(game_id):
  g0 = game_from_db(get_db().games.find_one(ObjectId(game_id)))
  g1 = draw_tiles(g0)
  get_db().games.replace_one({'_id': ObjectId(game_id)}, game_to_db(g1))
  if request.method == 'GET':
    return render_template('game.html', 
                       game=g0,
                       game_id=game_id,
                       logged_in_player=[p for p 
                                         in g1.players
                                         if p.name == session['logged_in']][0]) 
  else:
    try:
      g2 = play_tiles(g1, 
                      (int(request.form['row']), int(request.form['column'])),
                      request.form['direction'],
                      request.form['tiles'])
    except ValueError:
      g2 = g1._replace(next_player=(0 if g1.next_player == len(g1.players) - 1 
                                      else g1.next_player + 1))
      print(g1)
      print(g2)
    get_db().games.replace_one({'_id': ObjectId(game_id)}, game_to_db(g2))
    return redirect(url_for('game', game_id=game_id))

@app.route('/new_game', methods=['GET', 'POST'])
def create_game():
  if request.method == 'POST':
    other = choice(list(
        get_db().users.find({'name': {'$ne': session['logged_in']}})))
    result = get_db().games.insert_one(game_to_db(new_game([session['logged_in'], 
                                               other['name']])))
    return redirect(url_for('game', game_id=str(result.inserted_id)))
  return render_template('new_game.html')
