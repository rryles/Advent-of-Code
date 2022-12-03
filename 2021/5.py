#!/usr/bin/python3


from typing import DefaultDict
import re


with open('5.txt') as input:
    points = DefaultDict(int)

    for line in input.readlines():
        match = re.match(r"(\d+),(\d+) +-> +(\d+),(\d+)", line)
        if match:
            (x1, y1, x2, y2) = [int(g) for g in match.groups()]
            if x1 == x2:
                y_min = min(y1, y2)
                y_max = max(y1, y2)
                for y in range(y_min, y_max + 1):
                    points[(x1, y)] += 1
            elif y1 == y2:
                x_min = min(x1, x2)
                x_max = max(x1, x2)
                for x in range(x_min, x_max + 1):
                    points[(x, y1)] = points[(x, y1)] + 1

    danger = 0
    for point in points.values():
        if point > 1:
            danger += 1
    print(danger)
