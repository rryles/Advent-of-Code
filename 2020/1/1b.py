TARGET = 2020


def sum2(seen, target):
    seen = set(seen)
    while(seen):
        a = seen.pop()
        if target - a in seen:
            return a * (target - a)
    return None


seen = set()
with open('input.txt') as f:
    for line in f:
        line = int(line.strip())
        seen.add(line)
    
    while(seen):
        a = seen.pop()
        if b := sum2(seen, TARGET - a):
            print(a * b)
