#!/usr/bin/python3


with open('1.txt') as input:
    lines = input.readlines()
    depths = [int(line) for line in lines]

    windows = [depths[i] + depths[i+1] + depths[i+2] for i in range(len(depths)-2)]

    last = windows.pop(0)
    count = 0
    for depth in windows:
        if depth > last:
            count += 1
        last = depth
    print(count)