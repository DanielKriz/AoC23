#!/usr/bin/env python3
import sys
import re

with open(sys.argv[1]) as file:
    contents = [line.split(':')[-1] for line in file.readlines()]

get_nums = lambda x: set(re.findall(r'\d+',x))

games = []
for idx, line in enumerate(contents, start=1):
    winning, given= line.split('|')
    max_id = len(get_nums(winning).intersection(get_nums(given))) + idx + 1
    games.append([x for x in range(idx+1, max_id)])

values = dict()
for game_id, game in reversed(list(enumerate(games, start=1))):
    values[game_id] = 1 if not game else sum([values[k] for k in game]) + 1

print(sum(values.values()))
