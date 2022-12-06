score = 0
with open('input.txt') as f:
    yes = set()
    for line in f:
        line = line.strip()
        if line:
            for q in line:
                yes.add(q)
        else:
            score += len(yes)
            yes = set()
            
score += len(yes)

print(score)