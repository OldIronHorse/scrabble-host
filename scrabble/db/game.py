from scrabble.game import Game, Player

def player_from_db(db_player):
  return Player(name=db_player['name'],
                score=db_player['score'],
                tiles=db_player['tiles'])

def game_from_db(db_game):
  return Game(bag=db_game['bag'],
              board=tuple(db_game['board']),
              next_player=db_game['next_player'],
              players=tuple([player_from_db(p) for p in db_game['players']]))

def player_to_db(player):
  return {
    'name': player.name,
    'score': player.score,
    'tiles': player.tiles,
  }

def game_to_db(game):
  return {
    'bag': game.bag,
    'board': game.board,
    'next_player': game.next_player,
    'players': [player_to_db(p) for p in game.players],
  }
