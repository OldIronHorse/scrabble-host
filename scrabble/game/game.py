from random import shuffle
from scrabble.tiles import new_bag
from scrabble.board import new_board

def new_game(players):
  return {
      'bag': new_bag(),
      'board': new_board(),
      'players': [{'name': name, 'score': 0, 'tiles': ''} for name in players],
      'next_player': players[0],
    }

def draw_tiles(game):
  player = [player for player 
            in game['players'] 
            if player['name'] == game['next_player']][0]
  to_draw = 7 - len(player['tiles'])
  bag = list(game['bag'])
  shuffle(bag)
  game['bag'] = ''.join(bag)
  player['tiles'] += game['bag'][:to_draw]
  game['bag'] = game['bag'][to_draw:]
