from unittest import TestCase
from scrabble.tiles import new_bag
from scrabble.board import new_board
from scrabble.game import new_game, draw_tiles, play_tiles

class TestNewGame(TestCase):
  def test_2_players(self):
    self.maxDiff=None
    game = new_game(['Player1', 'Player2'])
    self.assertEqual(new_bag(), game.bag)
    self.assertEqual(new_board(), game.board)
    self.assertEqual(2, len(game.players))
    self.assertEqual('Player1', game.players[0].name)
    self.assertEqual(0, game.players[0].score)
    self.assertEqual('', game.players[0].tiles)
    self.assertEqual('Player2', game.players[1].name)
    self.assertEqual(0, game.players[1].score)
    self.assertEqual('', game.players[1].tiles)
    self.assertEqual(0, game.next_player)


class TestDrawTiles(TestCase):
  def test_first_draw(self):
    g0 = new_game(['Player1','Player2'])
    g1 = draw_tiles(g0)
    self.assertEqual(7, len(g1.players[0].tiles))
    self.assertEqual(len(new_bag()) - 7, len(g1.bag))
    self.assertEqual(sorted(new_bag()), sorted(g1.bag + g1.players[0].tiles))
    self.assertEqual('', g1.players[1].tiles)

class TestPlayTiles(TestCase):
  def test_valid_first_move_across(self):
    g0 = new_game(['Player1','Player2'])
    g1 = g0._replace(players=(g0.players[0]._replace(tiles='xjmpusz'),
                              g0.players[1]))
    g2 = play_tiles(g1, (7, 3), 'across', 'jumps')
    self.assertEqual('___jumps_______', g2.board[7])
    self.assertEqual('xz', g2.players[0].tiles)
    # TODO: score
    self.assertEqual('Player1', g2.players[0].name)
    self.assertEqual(1, g2.next_player)

  def test_valid_player2_move_across(self):
    g0 = new_game(['Player1', 'Player2'])
    g1 = g0._replace(next_player=1,
                     players=(g0.players[0],
                              g0.players[1]._replace(tiles='xjmpusz')))
    g2 = play_tiles(g1, (7, 3), 'across', 'jumps')
    self.assertEqual('___jumps_______', g2.board[7])
    self.assertEqual('xz', g2.players[1].tiles)
    # TODO: score
    self.assertEqual(0, g2.next_player)

  def test_valid_first_move_down(self):
    g0 = new_game(['Player1','Player2'])
    g1 = g0._replace(players=(g0.players[0]._replace(tiles='xjmpusz'),
                              g0.players[1]))
    g2 = play_tiles(g1, (3, 7), 'down', 'jumps')
    self.assertEqual('_______________', g2.board[0])
    self.assertEqual('_______________', g2.board[1])
    self.assertEqual('_______________', g2.board[2])
    self.assertEqual('_______j_______', g2.board[3])
    self.assertEqual('_______u_______', g2.board[4])
    self.assertEqual('_______m_______', g2.board[5])
    self.assertEqual('_______p_______', g2.board[6])
    self.assertEqual('_______s_______', g2.board[7])
    self.assertEqual('_______________', g2.board[8])
    self.assertEqual('_______________', g2.board[9])
    self.assertEqual('_______________', g2.board[10])
    self.assertEqual('_______________', g2.board[11])
    self.assertEqual('_______________', g2.board[12])
    self.assertEqual('_______________', g2.board[13])
    self.assertEqual('_______________', g2.board[14])
    self.assertEqual('xz', g2.players[0].tiles)
    # TODO: score
    self.assertEqual(1, g2.next_player)

  def test_horizontal_intersection(self):
    g0 = new_game(['Player1','Player2'])
    g1 = g0._replace(players=(g0.players[0],
                              g0.players[1]._replace(tiles='xacefqz')),
                     next_player=1,
                     board=('_______________',
                            '_______________',
                            '_______________',
                            '_______j_______',
                            '_______u_______',
                            '_______m_______',
                            '_______p_______',
                            '_______s_______',
                            '_______________',
                            '_______________',
                            '_______________',
                            '_______________',
                            '_______________',
                            '_______________',
                            '_______________'))
    g2 = play_tiles(g1, (6, 5), 'across', 'cae')
    self.assertEqual('_______________', g2.board[0])
    self.assertEqual('_______________', g2.board[1])
    self.assertEqual('_______________', g2.board[2])
    self.assertEqual('_______j_______', g2.board[3])
    self.assertEqual('_______u_______', g2.board[4])
    self.assertEqual('_______m_______', g2.board[5])
    self.assertEqual('_____cape______', g2.board[6])
    self.assertEqual('_______s_______', g2.board[7])
    self.assertEqual('_______________', g2.board[8])
    self.assertEqual('_______________', g2.board[9])
    self.assertEqual('_______________', g2.board[10])
    self.assertEqual('_______________', g2.board[11])
    self.assertEqual('_______________', g2.board[12])
    self.assertEqual('_______________', g2.board[13])
    self.assertEqual('_______________', g2.board[14])
    self.assertEqual('xfqz', g2.players[1].tiles)
    # TODO: score
    self.assertEqual(0, g2.next_player)
    
