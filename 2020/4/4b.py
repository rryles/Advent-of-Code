import re

p = re.compile(r"([a-z]{3}):(.+)")


def validate(passport):
    fields = dict()
    for line in passport:
        for field in line.split():
            m = p.match(field)
            if m:
                fields[m.group(1)] = m.group(2)
    if not all(k in fields for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return False
    return True 

count = 0

with open('input.txt') as f:
    passport = []
    for line in [l.strip() for l in f]:
        if line:
            passport.append(line)
        else:
            if validate(passport):
                count += 1
            passport = []
    if passport:
        if validate(passport):
            count += 1
print(count)

