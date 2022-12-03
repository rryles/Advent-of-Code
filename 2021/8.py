#!/usr/bin/python3


with open('8.txt') as input:
    count = 0
    for line in input.readlines():
        (_, outputs) = line.split(" | ")
        outputs = outputs.split()
        for output in outputs:
            if len(output) in (2, 4, 3, 7):
                count += 1

    print(count)
