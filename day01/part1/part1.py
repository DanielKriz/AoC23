#!/usr/bin/env python3
import sys
import re

with open(sys.argv[1]) as file:
    contents = file.readlines()

nums = [re.findall(r'\d', x) for x in contents]
result = sum([int(x[0] + x[-1]) for x in nums])
print(result)
