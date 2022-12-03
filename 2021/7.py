#!/usr/bin/python3


with open('7.txt') as input:
    positions = sorted([int(x) for x in input.readline().split(",")])

    target = positions[len(positions)//2]

    print(sum([abs(target-pos) for pos in positions]))
