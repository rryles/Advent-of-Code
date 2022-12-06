score = 0
with open('input.txt') as f:
    yes = []
    for line in f:
        line = line.strip()
        if line:
            person = set()
            for q in line:
                person.add(q)
            yes.append(person)
        else:
            score += len(set.intersection(*yes))
            yes = []
            
    score += len(set.intersection(*yes))

print(score)