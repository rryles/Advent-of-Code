#!/usr/bin/python3


"""
Unscambled digits

0: abc efg (6)
1:   c  f  (2)
2: a cde g (5)
3: a cd fg (5)
4:  bcd f  (4)
5: ab d fg (5)
6: ab defg (6)
7: a c  f  (3)
8: abcdefg (7)
9: abcd fg (6)

==============

1:   c  f  (2)

7: a c  f  (3)

4:  bcd f  (4)

2: a cde g (5)
3: a cd fg (5)
5: ab d fg (5)

0: abc efg (6)
6: ab defg (6)
9: abcd fg (6)

8: abcdefg (7)
"""


def to_set(segments):
    result = set()
    for c in segments:
        result.add(c)
    return frozenset(result)


def parse(line):
    (ten, four) = line.split(" | ")
    ten = [to_set(segs) for segs in ten.split()]
    four = [to_set(segs) for segs in four.split()]
    return (ten, four)


def decode(ten, four):
    decoder = dict()
    encoder = dict()

    for t in ten:
        if len(t) == 2:
            decoder[t] = 1
            encoder[1] = t
        elif len(t) == 3:
            decoder[t] = 7
            encoder[7] = t
        elif len(t) == 4:
            decoder[t] = 4
            encoder[4] = t
        elif len(t) == 7:
            decoder[t] = 8
            encoder[8] = t

    zero_nine = list()

    for t in ten:
        if len(t) == 6:
            if not encoder[1].issubset(t):  # Doesn't contain cf so must be 6
                decoder[t] = 6
                encoder[6] = t
            else:
                zero_nine.append(t)
        elif len(t) == 5:
            if len(t.union(encoder[4])) == 7:
                decoder[t] = 2
                encoder[2] = t
            elif len(t.union(encoder[1])) == 5:
                decoder[t] = 3
                encoder[3] = t
            else:
                decoder[t] = 5
                encoder[5] = t

    for t in zero_nine:
        if len(t.union(encoder[4])) == 7:
            decoder[t] = 0
            encoder[0] = t
        else:
            decoder[t] = 9
            encoder[9] = t

    decoded = [decoder[d] for d in four]
    result = decoded[0] * 1000
    result += decoded[1] * 100
    result += decoded[2] * 10
    result += decoded[3]
    print(result)
    return result


with open('8.txt') as input:
    total = 0
    for line in input.readlines():
        (ten, four) = parse(line)
        total += decode(ten, four)

    print(total)
