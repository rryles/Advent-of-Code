import re
from collections import deque


p = re.compile(r"move (\d+) from (\d+) to (\d+)")

stacks = [
    deque("LNWTD"),
    deque("HPC"),
    deque("WPHNDGMJ"),
    deque("CWSNTQL"),
    deque("PHCN"),
    deque("THNDMWQB"),
    deque("MBRJGSL"),
    deque("ZNWGVBRT"),
    deque("WGDNPL"),
]

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        m = p.match(line)
        if m:
            count = int(m.group(1))
            origin = int(m.group(2)) - 1
            destination = int(m.group(3)) - 1
            
            temp = deque()

            for _ in range(count):
                temp.append(stacks[origin].pop())
            for _ in range(count):
                stacks[destination].append(temp.pop())
            
message = "".join([s.pop() for s in stacks])
print (message)