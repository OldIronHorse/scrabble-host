from collections import namedtuple
from random import shuffle
from scrabble.tiles import new_bag
from scrabble.board import new_board

Game = namedtuple('Game', 'bag board players next_player')
Player = namedtuple('Player', 'name score tiles')

def new_game(players):
  return Game(bag=new_bag(), 
              board=new_board(),
              players=tuple([Player(name, 0, '') for name in players]),
              next_player=0)

def draw_tiles(game):
  player = game.players[game.next_player]
  to_draw = 7 - len(player.tiles)
  bag = list(game.bag)
  shuffle(bag)
  drawn = ''.join(bag[:to_draw])
  bag = ''.join(bag[to_draw:])
  return game._replace(bag=bag,
                       players=game.players[:game.next_player] \
                              + (player._replace(tiles=player.tiles + drawn),) \
                              + game.players[game.next_player + 1:])

def add_across(board, start, word):
  r, c = start
  return board[:r] \
         + (board[r][:c] + word + board[r][c + len(word):],) \
         + board[r + 1:]
  
def add_down(board, start,word):
  r, c = start
  word_as_column = ' ' * r + word + ' ' * (15 - r - len(word))
  return tuple([row[:c] + l + row[c + 1:] if row[c] == '_' else row 
                for row, l 
                in zip(board, word_as_column)])

add_fns = {
  'across': add_across,
  'down': add_down,
}

def play_tiles(game, start, direction, word):
  board = add_fns[direction](game.board, start, word)
  tiles = list(game.players[game.next_player].tiles)
  for l in word:
    tiles.remove(l)
  player = game.players[game.next_player]._replace(tiles=''.join(tiles))
  next_player = game.next_player + 1
  if next_player >= len(game.players):
    next_player = 0
  return game._replace(next_player=next_player,
                       board=board,
                       players=game.players[:game.next_player] \
                              + (player,) \
                              + game.players[game.next_player + 1:])

