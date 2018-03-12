from flask import Flask, redirect, render_template
from scrabble.host.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from scrabble.game import fetch_games, fetch_game

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __repr__(self):
    return '<User {}>'.format(self.username)

class Player(db.Model):
  #id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  game_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  tiles = db.Column(db.String(7))
  score = db.Column(db.Integer)

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  bag = db.Column(db.String(100))
  board = db.Column(db.String(15 * 15))


@app.route('/')
def root():
  return redirect('/games')

@app.route('/games')
def games():
  return render_template('games.html', games=fetch_games())

@app.route('/games/<game_id>')
def game(game_id):
  return render_template('game.html', game=fetch_game(game_id))
