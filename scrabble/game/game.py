from scrabble.tiles import new_bag
from scrabble.board import new_board

def new_game(players):
  return {
      'bag': new_bag(),
      'board': new_board(),
      'players': [{'name': name, 'score': 0} for name in players],
    }

games = {'1': new_game(['Player1', 'Player2'])}

def fetch_games():
  return games

def fetch_game(game_id):
  return games[game_id]
