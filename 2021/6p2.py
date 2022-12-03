#!/usr/bin/python3


with open('6.txt') as input:
    timercount = [0] * 9
    for timer in [int(x) for x in input.readline().split(",")]:
        timercount[timer] += 1

    print(sum(timercount))
    for day in range(256):
        births = timercount.pop(0)
        timercount.append(births)
        timercount[6] += births

    print(sum(timercount))
