#!/usr/bin/python3


with open('10.txt') as input:
    score = 0

    brackets = dict()
    brackets["("] = ")"
    brackets["["] = "]"
    brackets["{"] = "}"
    brackets["<"] = ">"

    b_score = dict()
    b_score[")"] = 3
    b_score["]"] = 57
    b_score["}"] = 1197
    b_score[">"] = 25137

    for line in input.readlines():
        stack = list()
        for c in line.rstrip():
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            else:
                if c != brackets[stack.pop()]:
                    score += b_score[c]
                    break

    print(score)
