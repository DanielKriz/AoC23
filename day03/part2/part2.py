#!/usr/bin/env python3
import sys
import re

class Grid:
    def __init__(self, data):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)

def get_rest_of_number(line, pos):
    for match in re.finditer(r'\d+', line):
        if pos >= match.start() and pos < match.end():
            return match.group(0)
    return None


def get_numbers_around(grid, line, pos):
    to_check =  [(line + x,
        [(pos-1) + y for y in range(0, 3)]
    ) for x in range(-1, 2)] 
    found = []
    for line, rows in to_check:
        if line < 0 or line >= grid.height:
            continue
        for row in rows:
            if row < 0 or row >= grid.width:
                continue
            if grid.data[line][row].isdigit():
                found.append(get_rest_of_number(grid.data[line], row))
    if len(set(found)) != 2:
        return 0,0
    return int(found[0]), int(found[-1])


with open(sys.argv[1]) as file:
    contents = [line.strip() for line in file.readlines()]

grid = Grid(contents)
sum = 0
for line_idx, line in enumerate(contents):
    for match in re.finditer(r'\*', line):
        x, y = get_numbers_around(grid, line_idx, match.start())
        sum += x * y
print(sum)
