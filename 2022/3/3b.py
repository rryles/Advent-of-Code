def group_score(lines):
    print(lines)
    item_sets = [set(h) for h in lines]
    common = item_sets[0].intersection(item_sets[1], item_sets[2])
    print(common)
    common = common.pop()
    if "a" <= common <= "z":
        return ord(common) - 96
    else:
        return ord(common) - 38
    return 0

score = 0
with open('input.txt') as f:
    lines = []
    for line in f:
        line = line.strip()
        lines.append(line)
    
    while(lines):
        elves = (lines.pop(0), lines.pop(0), lines.pop(0))
        score = score + group_score(elves)

print(score)