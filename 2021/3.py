#!/usr/bin/python3


with open('3.txt') as input:
    lines = [line.rstrip() for line in input.readlines()]
    bits = len(lines[0])
    counters = [0] * bits
    for line in lines:
        for bit in range(bits):
            if line[bit] == "1":
                counters[bit] += 1

    gamma = 0
    epsilon = 0

    for bit in range(bits):
        gamma *= 2
        epsilon *= 2
        if counters[bit] * 2 > len(lines):
            gamma += 1
        else:
            epsilon += 1
    print (gamma*epsilon)
