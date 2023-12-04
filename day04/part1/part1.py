#!/usr/bin/env python3
import sys
import re

get_nums = lambda x: set(re.findall(r'\d+',x))

with open(sys.argv[1]) as file:
    contents = [line.split(':')[-1] for line in file.readlines()]

total = 0
for line in contents:
    winning, given = line.split('|')
    true_winning = len(get_nums(winning).intersection(get_nums(given)))
    total += 2**(true_winning - 1) if true_winning > 0 else 0

print(total)
