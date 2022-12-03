#!/usr/bin/python3


import re


with open('13.txt') as input:
    dots = set()

    for line in input.readlines():
        if not line.rstrip():
            continue
        match = re.match(r"fold along (x|y)=(\d+)", line)
        if match:
            folded = {(x, y) if x < 655 else (1310-x, y) for (x, y) in dots}
            dots = folded
            print(len(dots))
            break
        else:
            (x, y) = line.rstrip().split(",")
            dot = (int(x), int(y))
            dots.add(dot)
