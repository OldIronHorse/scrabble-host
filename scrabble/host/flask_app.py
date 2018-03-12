from flask import Flask, g, redirect, render_template, request, session,\
  url_for
from werkzeug.security import check_password_hash
from pymongo import MongoClient
from scrabble.game import fetch_games, fetch_game

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
  return render_template('games.html', games=get_db().games.find())

@app.route('/games/<game_id>')
def game(game_id):
  return render_template('game.html', game=get_db().games.find_one(game_id))

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
  pass
