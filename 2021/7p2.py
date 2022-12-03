#!/usr/bin/python3


def individual_cost(position, target):
    distance = abs(target-position)
    return (distance * (distance + 1)) // 2


def total_cost(positions, target):
    return sum([individual_cost(pos, target) for pos in positions])


with open('7.txt') as input:
    positions = sorted([int(x) for x in input.readline().split(",")])

    target = sum(positions)//len(positions)
    cost = total_cost(positions, target)

    done = False
    while not done:
        print(target, cost)
        alt_target = target + 1
        alt_cost = total_cost(positions, alt_target)
        if alt_cost < cost:
            target = alt_target
            cost = alt_cost
        else:
            done = True

    done = False
    while not done:
        print(target, cost)
        alt_target = target - 1
        alt_cost = total_cost(positions, alt_target)
        if alt_cost < cost:
            target = alt_target
            cost = alt_cost
        else:
            done = True

    print(target, cost)
