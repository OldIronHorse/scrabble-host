from unittest import TestCase
from scrabble.game import new_game
from scrabble.board import new_board
from scrabble.tiles import new_bag
from scrabble.db import game_to_db, game_from_db

class TestDBConversion(TestCase):
  def setUp(self):
    self.maxDiff= None

  def test_new_game_to_db(self):
    self.assertEqual({
        'bag': new_bag(),
        'players': [{
            'name': 'P1',
            'tiles': '',
            'score': 0,
          },{
            'name': 'P2',
            'tiles': '',
            'score': 0,
        }],
        'next_player': 0,
        'board': new_board(),
      },game_to_db(new_game(['P1', 'P2'])))

  def test_game_to_db(self):
    self.assertEqual({
        'bag': new_bag(),
        'players': [{
            'name': 'P1',
            'tiles': '',
            'score': 0,
          },{
            'name': 'P2',
            'tiles': '',
            'score': 0,
        }],
        'next_player': 0,
        'board': new_board(),
      },game_to_db(new_game(['P1', 'P2'])))
      
  def test_game_from_db(self):
    g = game_from_db({
      '_id': '<ObjectId>',
      'bag': 'abcdef',
      'players': [{
          'name': 'P1',
          'score': 5,
          'tiles': 'ghi',
        },{
          'name': 'P2',
          'score': 6,
          'tiles': 'klmn',
        }],
        'board': [
          '_______________',
          '_______________',
          '_______________',
          '_______________',
          '_______________',
          '_____h_________',
          '____jumps______',
          '_____m_________',
          '____cat________',
          '_____n_________',
          '_______________',
          '_______________',
          '_______________',
          '_______________',
          '_______________',
        ],
        'next_player': 1,
      })
    self.assertEqual('abcdef', g.bag)
    self.assertEqual('P1', g.players[0].name)
    self.assertEqual(5, g.players[0].score)
    self.assertEqual('ghi', g.players[0].tiles)
    self.assertEqual('P2', g.players[1].name)
    self.assertEqual(6, g.players[1].score)
    self.assertEqual('klmn', g.players[1].tiles)
    self.assertEqual(('_______________',
                      '_______________',
                      '_______________',
                      '_______________',
                      '_______________',
                      '_____h_________',
                      '____jumps______',
                      '_____m_________',
                      '____cat________',
                      '_____n_________',
                      '_______________',
                      '_______________',
                      '_______________',
                      '_______________',
                      '_______________'),
                     g.board)
    self.assertEqual(1, g.next_player)
