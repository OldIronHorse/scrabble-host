from unittest import TestCase
from scrabble.board import new_board

class TestNewBoard(TestCase):
  def test_new_board(self):
    board = new_board()
    for row in range(0, 15):
      for col in range(0, 15):
        self.assertEqual(' ', board[row][col])
