#!/usr/bin/python3


with open('1.txt') as input:
    lines = input.readlines()
    depths = [int(line) for line in lines]
    last = depths.pop(0)
    count = 0
    for depth in depths:
        if depth > last:
            count += 1
        last = depth
    print(count)