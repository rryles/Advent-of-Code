#!/usr/bin/python3


import re
from typing import DefaultDict, Deque


with open('14.txt') as input:
    rules = dict()
    poly = Deque()

    for line in input.readlines():
        if not line.rstrip():
            continue
        match = re.match(r"([A-Z])([A-Z]) -> ([A-Z])", line)
        if match:
            rules[(match.group(1, 2))] = match.group(3)
        else:
            for c in line.rstrip():
                poly.append(c)

    for step in range(10):
        npoly = Deque()
        elem1 = poly.popleft()
        npoly.append(elem1)
        while len(poly):
            elem2 = poly.popleft()
            if (elem1, elem2) in rules:
                npoly.append(rules[(elem1, elem2)])
            npoly.append(elem2)
            elem1 = elem2
        poly = npoly

    quantity = DefaultDict(int)
    for elem in poly:
        quantity[elem] += 1

    quantity = list(quantity.values())
    quantity.sort()
    print(quantity[-1]-quantity[0])
