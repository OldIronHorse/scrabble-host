from flask import Flask, render_template, redirect
from scrabble.game import fetch_games, fetch_game

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
  SECRET_KEY='development key'))

@app.route('/')
def root():
  return redirect('/games')

@app.route('/games')
def games():
  return render_template('games.html', games=fetch_games())

@app.route('/games/<game_id>')
def game(game_id):
  return render_template('game.html', game=fetch_game(game_id))
