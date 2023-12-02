#!/usr/bin/env python3
from functools import reduce
import sys
import re

def get_values(round):
    color_matches = (
        re.search(r'.* (\d+)( red)', round),
        re.search(r'.* (\d+)( green)', round),
        re.search(r'.* (\d+)( blue)', round),
    )
    get_count = lambda x: 0 if x is None else int(x.groups()[0])
    return [get_count(color) for color in color_matches]


with open(sys.argv[1]) as file:
    contents = file.readlines()

powers = []
for line in contents:
    _, rounds_part = line.split(':')
    round_values = [get_values(round) for round in rounds_part.split(';')]
    powers.append(
        reduce(lambda x,y: x * y ,[max(v) for v in zip(*round_values)])
    )
print(sum(powers))
