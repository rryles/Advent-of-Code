def rucksack_score(line):
    line_len = len(line)
    half_len = line_len//2
    line_halves = (line[:half_len], line[half_len:])
    item_sets = [set(h) for h in line_halves]
    common = item_sets[0].intersection(item_sets[1])
    common = common.pop()
    if "a" <= common <= "z":
        return ord(common) - 96
    else:
        return ord(common) - 38
    return 0

score = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        score = score + rucksack_score(line)

print(score)