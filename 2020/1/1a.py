target = 2020
seen = set()

with open('input.txt') as f:
    for line in f:
        line = int(line.strip())
        if target - line in seen:
            print((target - line) * line)
        else:
            seen.add(line)
