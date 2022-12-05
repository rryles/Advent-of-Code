import re

p = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

score = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        m = p.match(line)
        if m:
            a_s = int(m.group(1))
            a_e = int(m.group(2))
            b_s = int(m.group(3))
            b_e = int(m.group(4))
            if a_s < b_s and a_e < b_e:
                pass
            elif a_s > b_s and a_e > b_e:
                pass
            else:
                score += 1
                print(a_s, a_e, b_s, b_e)
            

print(score)