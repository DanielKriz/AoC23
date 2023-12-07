#!/usr/bin/env python3
import functools
import sys
import re

def get_input(idx, contents):
    return int(functools.reduce(
        lambda x,y: x + y,
        re.findall(r'\d+', contents[idx])
    ))

with open(sys.argv[1]) as file:
    contents = file.readlines()

time = get_input(0, contents)
distance = get_input(1, contents)
results = [(int(time) - ms) * ms for ms in range(time)]
print(len(list(filter(lambda x: x > distance, results))))
