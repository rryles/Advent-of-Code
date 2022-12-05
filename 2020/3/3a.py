position = 0
trees = 0

with open('input.txt') as f:
    
    for line in f:
        line = line.strip()
        if line[position] == "#":
            trees += 1
        position += 3
        if position >= len(line):
            position -= len(line)

print(trees)