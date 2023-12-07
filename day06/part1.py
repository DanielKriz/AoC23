#!/usr/bin/env python3
import math
import sys
import re

with open(sys.argv[1]) as file:
    contents = file.readlines()

times = re.findall(r'\d+', contents[0])
distances = re.findall(r'\d+', contents[1])

above = []
for time, distance in zip(times, distances):
    results = [(int(time) - ms) * ms for ms in range(int(time))]
    above.append(len(list(filter(lambda x: x > int(distance), results))))
print(math.prod(above))
