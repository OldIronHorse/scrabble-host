from random import choice
from scrabble.tiles import new_bag
from scrabble.board import new_board

def new_game(players):
  return {
      'bag': new_bag(),
      'board': new_board(),
      'players': [{'name': name, 'score': 0, 'tiles': ''} for name in players],
      'next_player': choice(players),
    }

