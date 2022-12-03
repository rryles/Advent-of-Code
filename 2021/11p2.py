#!/usr/bin/python3


def get_energy(octopuses, row, col):
    if row < 0:
        return 0
    if col < 0:
        return 0
    if row >= len(octopuses):
        return 0
    if col >= len(octopuses[0]):
        return 0
    return octopuses[row][col]


with open('11.txt') as input:
    flashes = 0
    step = 0

    octopuses = list()

    for line in input.readlines():
        row = [int(c) for c in line.rstrip()]
        octopuses.append(row)

    while flashes < (len(octopuses) * len(octopuses[0])):
        step += 1
        flashes = 0
        # Increment all energy levels
        for r in range(len(octopuses)):
            for c in range(len(octopuses[0])):
                octopuses[r][c] += 1

        # check for flashes
        flashing = True
        while flashing:
            flashing = False
            for r in range(len(octopuses)):
                for c in range(len(octopuses[0])):
                    if octopuses[r][c] > 9:
                        octopuses[r][c] = 0
                        flashes += 1
                        flashing = True
                        for (rdelta, cdelta) in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                            nr = r + rdelta
                            nc = c + cdelta
                            if get_energy(octopuses, nr, nc) != 0:
                                octopuses[nr][nc] += 1
        print(flashes)

    print(step)
