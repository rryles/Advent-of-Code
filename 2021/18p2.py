#!/usr/bin/python3


import re


def explode(before, lhs, rhs, after):
    m = re.search(r"(\d+)(\D*)$", before)
    if m:
        before = before[:m.start()] + str(lhs + int(m[1])) + m[2]

    m = re.search(r"(\d+)", after)
    if m:
        after = after[:m.start()] + str(rhs + int(m[1])) + after[m.end():]

    return before + "0" + after


def try_explode(snail):
    depth = 0
    for i in range(len(snail)):
        if snail[i] == "[":
            depth += 1
        elif snail[i] == "]":
            depth -= 1
        if depth > 4:
            before = snail[:i]
            match = re.match(r"\[(\d+),(\d+)\](.*)", snail[i:])
            if match:
                return (True, explode(before, int(match[1]), int(match[2]), match[3]))
    return (False, snail)


def try_split(snail):
    for m in re.finditer(r"\d+", snail):
        val = int(m[0])
        if val > 9:
            a = val // 2
            b = val - a
            return (True, snail[:m.start()] + "[{},{}]".format(a, b) + snail[m.end():])
    return (False, snail)


def reduce(snail):
    while True:
        (exploded, snail) = try_explode(snail)
        if exploded:
            continue
        (did_split, snail) = try_split(snail)
        if did_split:
            continue
        break
    return snail


def add(lhs, rhs):
    return "[{},{}]".format(lhs, rhs)


def add_reduce(lhs, rhs):
    return reduce(add(lhs, rhs))


def magnitude(snail):
    while True:
        m = re.search(r"\[(\d+),(\d+)\]", snail)
        if m:
            sub = str((3*int(m[1])) + (2*int(m[2])))
            snail = snail[:m.start()] + sub + snail[m.end():]
        else:
            return int(snail)


def test_explode1():
    (did, result) = try_explode("[[[[[9,8],1],2],3],4]")
    assert(did)
    assert(result == "[[[[0,9],2],3],4]")


def test_explode2():
    (did, result) = try_explode("[7,[6,[5,[4,[3,2]]]]]")
    assert(did)
    assert(result == "[7,[6,[5,[7,0]]]]")


def test_explode3():
    (did, result) = try_explode("[[6,[5,[4,[3,2]]]],1]")
    assert(did)
    assert(result == "[[6,[5,[7,0]]],3]")


def test_explode4():
    (did, result) = try_explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    assert(did)
    assert(result == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")


def test_explode5():
    (did, result) = try_explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    assert(did)
    assert(result == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")


def test_split1():
    (did, result) = try_split("[10,1]")
    assert(did)
    assert(result == "[[5,5],1]")


def test_split2():
    (did, result) = try_split("[11,2]")
    assert(did)
    assert(result == "[[5,6],2]")


def test_split3():
    (did, result) = try_split("[[[[0,7],4],[15,[0,13]]],[1,1]]")
    assert(did)
    assert(result == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")


def test_split4():
    (did, result) = try_split("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    assert(did)
    assert(result == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")


def test_reduce():
    assert(reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")


def test_add_reduce():
    assert(add_reduce("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")


def test_magnitude_simple():
    assert(magnitude("[9,1]") == 29)
    assert(magnitude("[1,9]") == 21)


def test_magnitude1():
    assert(magnitude("[[1,2],[[3,4],5]]") == 143)


if __name__ == "__main__":
    with open('18.txt') as input:
        lines = [line.rstrip() for line in input.readlines()]
        best = 0
        for i in range(len(lines)):
            for j in range(len(lines)):
                if i == j:
                    continue
                new = magnitude(add_reduce(lines[i], lines[j]))
                if new > best:
                    best = new
        print(best)
