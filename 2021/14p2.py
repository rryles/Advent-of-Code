#!/usr/bin/python3


import re
from typing import DefaultDict


with open('14.txt') as input:
    rules = dict()
    pair_count = DefaultDict(int)
    first_elem = None
    last_elem = None

    for line in input.readlines():
        if not line.rstrip():
            continue
        match = re.match(r"([A-Z])([A-Z]) -> ([A-Z])", line)
        if match:
            rules[(match.group(1, 2))] = match.group(3)
        else:
            poly = list(line.rstrip())
            prev = poly.pop(0)
            first_elem = prev
            last_elem = poly[-1]
            for elem in poly:
                pair_count[(prev, elem)] += 1
                prev = elem

    for step in range(40):
        new_pair_count = DefaultDict(int)
        for ((l, r), count) in pair_count.items():
            if (l, r) in rules:
                m = rules[(l, r)]
                new_pair_count[(l, m)] += count
                new_pair_count[(m, r)] += count
        pair_count = new_pair_count

    quantity = DefaultDict(int)
    for ((l, r), count) in pair_count.items():
        quantity[l] += count

    quantity[last_elem] += 1
    quantity = list(quantity.values())
    quantity.sort()
    print(quantity[-1]-quantity[0])
