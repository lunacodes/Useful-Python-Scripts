#!/usr/bin/env python3
"""Takes a file of newline separated values, and checks if each file exists."""

import pprint
import os.path

f = 'path_to_file'
# You can switch 
lines = [line.rstrip('\n') for line in open(f)]

lines2 = [i.strip('"') for i in lines]

pprint.pprint(lines2)

missing = []

for i in lines2:
    if os.path.exists(i):
        print(i, "True")
    else:
        print("FALSE")
        missing.append(i)
         
pprint.pprint(missing)       
