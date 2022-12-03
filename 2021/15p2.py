#!/usr/bin/python3


from queue import PriorityQueue


def get_neighbours(cave, current):
    if current[0] > 0:
        yield (current[0] - 1, current[1])
    if current[0] + 1 < len(cave):
        yield (current[0] + 1, current[1])
    if current[1] > 0:
        yield (current[0], current[1] - 1)
    if current[1] + 1 < len(cave[0]):
        yield (current[0], current[1] + 1)


def wrap(x):
    while x > 9:
        x -= 9
    return x


with open('15.txt') as input:
    tile = list()
    cave = list()
    dist = list()
    visited = set()

    for line in input.readlines():
        row = [int(c) for c in line.rstrip()]
        tile.append(row)
        for _ in range(5):
            dist.append([float('inf')]*(len(row)*5))

    for tile_row in range(5):
        for r in range(len(tile)):
            row = list()
            for tile_col in range(5):
                row.extend([wrap(risk + tile_row + tile_col) for risk in tile[r]])
            cave.append(row)

    dist[0][0] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        (d, current_vertex) = pq.get()
        visited.add(current_vertex)

        for neighbour in get_neighbours(cave, current_vertex):
            if neighbour not in visited:
                old_cost = dist[neighbour[0]][neighbour[1]]
                new_cost = dist[current_vertex[0]][current_vertex[1]] + cave[neighbour[0]][neighbour[1]]
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    dist[neighbour[0]][neighbour[1]] = new_cost

    print(dist[-1][-1])
