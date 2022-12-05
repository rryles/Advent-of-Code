seats = set()

with open('input.txt') as f:
    for line in [l.strip() for l in f]:
        line = line.replace("F", "0")
        line = line.replace("B", "1")
        line = line.replace("L", "0")
        line = line.replace("R", "1")
        seat_id = int(line, 2)
        seats.add(seat_id)

for prev in seats:
    if (prev + 1 not in seats) and (prev + 2 in seats):
        print(prev + 1)

