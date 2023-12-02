#!/usr/bin/env python3
import sys
import re

conf = (12, 13, 14)

def is_possible(configuration, round):
    color_matches = (
        re.search(r'.* (\d+)( red)', round),
        re.search(r'.* (\d+)( green)', round),
        re.search(r'.* (\d+)( blue)', round),
    )
    get_count = lambda x: 0 if x is None else int(x.groups()[0])
    values = [get_count(color) for color in color_matches]
    for max, got in zip(configuration, values):
        if got > max:
            return False
    return True


with open(sys.argv[1]) as file:
    contents = file.readlines()

sum = 0
for line in contents:
    game_part, rounds_part = line.split(':')
    game_id = int(game_part.split(' ')[-1])
    rounds = [is_possible(conf, round) for round in rounds_part.split(';')]
    sum += game_id if False not in rounds else 0
print(sum)
