#!/usr/bin/env python3
import itertools
import sys
import re

def split_list(lst, delim):
    is_delim = lambda x: x == delim
    return [list(v) for k,v in itertools.groupby(lst, is_delim) if not k]

def get_ranges(line):
    dst, src, range_len = [int(x) for x in re.findall(r'\d+', line)]
    return (
        range(src, src+range_len),
        range(dst, dst+range_len),
    )

map_path = [
    'seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity'
]

with open(sys.argv[1]) as file:
    contents = [line.split(':')[-1] for line in file.readlines()]

seeds = [int(x) for x in re.findall(r'\d+', contents[0])]
almanac_ranges = [
    [get_ranges(x) for x in y] for y in split_list(contents[1:], '\n')
]
almanac = {k:v for k, v in zip(map_path, almanac_ranges)}

locations = []
for seed in seeds:
    key = seed
    seed_path = []
    for p in map_path:
        ranges = almanac[p]
        for r in ranges:
            src, dst = r
            if key in src:
                key = dst[abs(src[0] - key)]
                break
        seed_path.append(key)
    locations.append(seed_path[-1])
print(locations)
print(min(locations))
