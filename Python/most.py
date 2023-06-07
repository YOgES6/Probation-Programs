import tornado.ioloop

games = ['heads', 'heads', 'tails', 'heads', 'tails']
items = set(games)
print(max(items, key = games.count))
