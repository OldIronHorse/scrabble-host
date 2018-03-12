from unittest import TestCase
from scrabble.tiles import new_bag
from scrabble.board import new_board
from scrabble.game import new_game

class TestNewGame(TestCase):
  def test_2_players(self):
    self.assertEqual({
        'bag': new_bag(),
        'board': new_board(),
        'players':[{
            'name': 'Player1',
            'score': 0,
            'tiles': '',
          },{
            'name': 'Player2',
            'score': 0,
            'tiles': '',
      }]}, 
      new_game(['Player1', 'Player2']))
