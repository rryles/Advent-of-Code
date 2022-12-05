def try_slope(lines, right, down):

    position = 0
    trees = 0

    for line in lines[::down]:
        if line[position] == "#":
            trees += 1
        position += right
        if position >= len(line):
            position -= len(line)
    return trees

with open('input.txt') as f:
    lines = [l.strip() for l in f]
    product = 1
    product *= try_slope(lines, 1, 1)
    product *= try_slope(lines, 3, 1)
    product *= try_slope(lines, 5, 1)
    product *= try_slope(lines, 7, 1)
    product *= try_slope(lines, 1, 2)
    print(product)

