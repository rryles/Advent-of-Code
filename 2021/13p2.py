#!/usr/bin/python3


import re


with open('13.txt') as input:
    dots = set()

    for line in input.readlines():
        if not line.rstrip():
            continue
        match = re.match(r"fold along (x|y)=(\d+)", line)
        if match:
            fold = int(match.group(2))
            if match.group(1) == "x":
                folded = {(x, y) if x < fold else (fold+fold-x, y) for (x, y) in dots}
            else:
                folded = {(x, y) if y < fold else (x, fold+fold-y) for (x, y) in dots}
            dots = folded
        else:
            (x, y) = line.rstrip().split(",")
            dot = (int(x), int(y))
            dots.add(dot)

    for y in range(6):
        print("".join(["##" if (x, y) in dots else "  " for x in range(40)]))
