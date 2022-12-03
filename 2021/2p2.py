#!/usr/bin/python3


with open('2.txt') as input:
    commands = input.readlines()
    depth = 0
    horizontal = 0
    aim = 0
    for command in commands:
        (direction, distance) = command.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += (aim * distance)
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    print(depth * horizontal)
