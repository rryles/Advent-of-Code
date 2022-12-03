elves = []
with open('input.txt') as f:
    elf = []
    for line in f:
        line = line.strip()
        if line != "":
            elf.append(int(line))
        else:
            elves.append(elf)
            elf = []

calories = [sum(elf) for elf in elves]

print(sorted(calories)[-1])