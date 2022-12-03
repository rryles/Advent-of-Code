import re

p = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

score = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        m = p.match(line)
        if m:
            (c_min, c_max, letter, password) = m.group(1, 2, 3, 4)
            c_min = int(c_min) - 1
            c_max = int(c_max) - 1
            password = list(password)
            print(c_min, c_max, len(password))
            actual = [password[i] for i in [c_min, c_max]].count(letter)
            if 1 == actual:
                score = score + 1
            
print(score)