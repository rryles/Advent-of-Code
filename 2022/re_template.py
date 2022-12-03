import re

p = re.compile(r"([A-C]) ([X-Z])")

score = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        m = p.match(line)
        if m:
            opponent = m.group(1)
            me = m.group(2)
            if opponent == "A":
                if line == "A X":
                    score = score + 1 + 3
                elif line == "A Y":
                    score = score + 2 + 6
                elif line == "A Z":
                    score = score + 3 + 0
            elif opponent == "B":
                if line == "B X":
                    score = score + 1 + 0
                elif line == "B Y":
                    score = score + 2 + 3
                elif line == "B Z":
                    score = score + 3 + 6
            elif opponent == "C":
                if line == "C X":
                    score = score + 1 + 6
                elif line == "C Y":
                    score = score + 2 + 0
                elif line == "C Z":
                    score = score + 3 + 3
            

print(score)