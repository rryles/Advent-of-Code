#!/usr/bin/python3


def get_height(rows, r, c):
    if r < 0:
        return 9
    if r >= len(rows):
        return 9
    if c < 0:
        return 9
    if c >= len(rows[0]):
        return 9
    return rows[r][c]


with open('9.txt') as input:
    rows = list()
    for line in input.readlines():
        row = [int(c) for c in line.rstrip()]
        rows.append(row)

    minima = list()

    for r in range(len(rows)):
        for c in range(len(rows[0])):
            h = rows[r][c]
            if r > 0:
                if h >= rows[r-1][c]:
                    continue
            if c > 0:
                if h >= rows[r][c-1]:
                    continue
            if r+1 < len(rows):
                if h >= rows[r+1][c]:
                    continue
            if c+1 < len(rows[0]):
                if h >= rows[r][c+1]:
                    continue
            point = (r, c)
            minima.append(point)

    basins = list()

    for m in minima:
        todo = [m]
        basin_cells = set(todo)
        while todo:
            (r, c) = todo.pop()
            for (rn, cn) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                point = (rn, cn)
                if point not in basin_cells:
                    if get_height(rows, rn, cn) != 9:
                        basin_cells.add(point)
                        todo.append(point)
        basins.append(len(basin_cells))
    basins.sort()
    print(basins[-1]*basins[-2]*basins[-3])
