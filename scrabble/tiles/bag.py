from itertools import repeat

bag = ''.join(sum(map(list, [repeat('a',9), 
                            repeat('b',2),
                            repeat('c',2),
                            repeat('d',4),
                            repeat('e',12),
                            repeat('f',2),
                            repeat('g',3),
                            repeat('h',2),
                            repeat('i',9),
                            repeat('j',1),
                            repeat('k',1),
                            repeat('l',4),
                            repeat('m',2),
                            repeat('n',6),
                            repeat('o',8),
                            repeat('p',2),
                            repeat('q',1),
                            repeat('r',6),
                            repeat('s',4),
                            repeat('t',6),
                            repeat('u',4),
                            repeat('v',2),
                            repeat('w',2),
                            repeat('x',1),
                            repeat('y',2),
                            repeat('z',1),
                            repeat('*',2),
                            ]), []))

def new_bag():
  return bag
