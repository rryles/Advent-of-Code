#!/usr/bin/python3


from typing import DefaultDict


def count_routes(neighbours, at="start", visited=set(["start"]), revisited=None):
    if at == "end":
        return 1

    routes = 0

    for neighbour in neighbours[at]:
        if neighbour == "start":
            continue

        if neighbour.isupper() or (neighbour not in visited):
            routes += count_routes(neighbours, neighbour, visited.union(set([neighbour])), revisited)
        elif not revisited:
            routes += count_routes(neighbours, neighbour, visited.union(set([neighbour])), neighbour)

    return routes


with open('12.txt') as input:
    neighbours = DefaultDict(list)

    for line in input.readlines():
        (a, b) = line.rstrip().split("-")
        neighbours[a].append(b)
        neighbours[b].append(a)

    print(count_routes(neighbours))
