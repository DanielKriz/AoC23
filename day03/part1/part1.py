#!/usr/bin/env python3
import sys
import re

class Grid:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)


def is_symbol_around(grid, line, pos, number):
    is_symbol = lambda x: x != '.' and not x.isdigit()
    to_check =  [(line + x,
        [(pos-1) + y for y in range(len(number) + 2)]
    ) for x in range(-1, 2)] 
    for line, rows in to_check:
        if line < 0 or line >= grid.height:
            continue
        for row in rows:
            if row < 0 or row >= grid.width:
                continue
            if is_symbol(grid.data[line][row]):
                return True
    return False


with open(sys.argv[1]) as file:
    contents = [line.strip() for line in file.readlines()]

grid = Grid(contents)
sum = 0
for line_idx, line in enumerate(contents):
    for match in re.finditer(r'\d+', line):
        if is_symbol_around(grid, line_idx, match.start(), match.group(0)):
            sum += int(match.group(0))
print(sum)
