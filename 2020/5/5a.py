highest = 0

with open('input.txt') as f:
    for line in [l.strip() for l in f]:
        line = line.replace("F", "0")
        line = line.replace("B", "1")
        line = line.replace("L", "0")
        line = line.replace("R", "1")
        seat_id = int(line, 2)
        if seat_id > highest:
            highest = seat_id

print(highest)

