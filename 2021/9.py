#!/usr/bin/python3


with open('9.txt') as input:
    rows = list()
    for line in input.readlines():
        row = [int(c) for c in line.rstrip()]
        rows.append(row)

    risk_level = 0

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
            risk_level += h + 1

    print(risk_level)
