import re
from collections import defaultdict


cache = dict()
rules = dict()


def full_contents(outer_colour):
    if outer_colour in cache:
        return cache[outer_colour]
    fc = defaultdict(int)

    for rule in rules[outer_colour]:
        (inner_count, inner_colour) = rule
        fc[inner_colour] += inner_count
        for (inner_inner_colour, inner_inner_count) in full_contents(inner_colour).items():
            fc[inner_inner_colour] += inner_count * inner_inner_count

    cache[outer_colour] = fc
    return fc


with open('input.txt') as f:
    
    p_rule = re.compile(r"(.+) bags contain (.+)\.")
    p_cont = re.compile(r"(\d+) (.+) bags?")
    for line in [l.strip() for l in f]:
        m = p_rule.fullmatch(line)
        if m:
            contents = []
            for c in m.group(2).split(", "):
                m_cont = p_cont.fullmatch(c)
                if m_cont:
                    r = (int(m_cont.group(1)), m_cont.group(2))
                    contents.append(r)
            rules[m.group(1)] = contents
        
count = 0

for colour in rules:
    contents = full_contents(colour)
    if contents["shiny gold"]:
        count += 1

print(count)


