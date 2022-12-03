#!/usr/bin/python3


with open('6.txt') as input:
    timers = [int(x) for x in input.readline().split(",")]

    for day in range(80):
        for i in range(len(timers)):
            if timers[i] == 0:
                timers[i] = 6
                timers.append(8)
            else:
                timers[i] -= 1

    print(len(timers))
