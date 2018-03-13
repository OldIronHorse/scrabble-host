from unittest import TestCase
from scrabble.tiles import new_bag
from scrabble.board import new_board
from scrabble.game import new_game, draw_tiles

class TestNewGame(TestCase):
  def test_2_players(self):
    self.maxDiff=None
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
          }],
        'next_player': 'Player1',
      }, 
      new_game(['Player1', 'Player2']))

class TestDrawTiles(TestCase):
  def test_first_draw(self):
    game = new_game(['Player1','Player2'])
    self.assertEqual('', game['players'][0]['tiles'])
    self.assertEqual('', game['players'][1]['tiles'])
    self.assertEqual(new_bag(), game['bag'])
    draw_tiles(game)
    player1 = [p for p in game['players'] if p['name'] == 'Player1'][0]
    self.assertEqual(7, len(player1['tiles']))
    self.assertEqual(len(new_bag()) - 7, len(game['bag']))
    self.assertEqual(sorted(new_bag()), sorted(game['bag'] + player1['tiles']))
    player2 = [p for p in game['players'] if p['name'] == 'Player2'][0]
    self.assertEqual('', player2['tiles'])
