#!/usr/bin/env python3
import sys
import re

num_map = {k: str(v) for v, k in enumerate(
    ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    start=1,
)}

def transform(num_str):
    nums = re.findall(fr'(?=(\d|{"|".join(num_map.keys())}))', num_str)
    return [x if x.isdigit() else num_map[x] for x in nums]

with open(sys.argv[1]) as file:
    contents = file.readlines()

nums = [transform(x) for x in contents]
result = sum([int(x[0] + x[-1]) for x in nums])
print(result)
