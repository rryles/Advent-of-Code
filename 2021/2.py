#!/usr/bin/python3


with open('2.txt') as input:
    commands = input.readlines()
    depth = 0
    horizontal = 0
    for command in commands:
        (direction, distance) = command.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
    print(depth * horizontal)
