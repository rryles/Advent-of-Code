import re


def check_byr(data):
    p = re.compile(r"(\d{4})")
    m = p.fullmatch(data)
    if not m:
        return False
    year = int(m.group(1))
    return 1920 <= year <= 2002


def check_iyr(data):
    p = re.compile(r"(\d{4})")
    m = p.fullmatch(data)
    if not m:
        return False
    year = int(m.group(1))
    return 2010 <= year <= 2020


def check_eyr(data):
    p = re.compile(r"(\d{4})")
    m = p.fullmatch(data)
    if not m:
        return False
    year = int(m.group(1))
    return 2020 <= year <= 2030


def check_hgt(data):
    p = re.compile(r"(\d+)(cm|in)")
    m = p.fullmatch(data)
    if not m:
        return False
    value = int(m.group(1))
    if m.group(2) == "cm":
        return 150 <= value <= 193
    else:
        return 59 <= value <= 76


def check_hcl(data):
    p = re.compile(r"#[0-9a-f]{6}")
    m = p.fullmatch(data)
    if not m:
        return False
    return True


def check_ecl(data):
    p = re.compile(r"amb|blu|brn|gry|grn|hzl|oth")
    m = p.fullmatch(data)
    if not m:
        return False
    return True


def check_pid(data):
    p = re.compile(r"\d{9}")
    m = p.fullmatch(data)
    if not m:
        return False
    return True


def validate(passport):
    p = re.compile(r"([a-z]{3}):(.+)")
    fields = dict()
    for line in passport:
        for field in line.split():
            m = p.match(field)
            if m:
                fields[m.group(1)] = m.group(2)
    if not all(k in fields for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return False
    return all([
        check_byr(fields["byr"]),
        check_iyr(fields["iyr"]),
        check_eyr(fields["eyr"]),
        check_hgt(fields["hgt"]),
        check_hcl(fields["hcl"]),
        check_ecl(fields["ecl"]),
        check_pid(fields["pid"])])

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

