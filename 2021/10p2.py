#!/usr/bin/python3


with open('10.txt') as input:
    scores = list()

    brackets = dict()
    brackets["("] = ")"
    brackets["["] = "]"
    brackets["{"] = "}"
    brackets["<"] = ">"

    b_score = dict()
    b_score[")"] = 1
    b_score["]"] = 2
    b_score["}"] = 3
    b_score[">"] = 4

    for line in input.readlines():
        stack = list()
        for c in line.rstrip():
            if c in ("(", "[", "{", "<"):
                stack.append(c)
            else:
                if c != brackets[stack.pop()]:
                    break
        else:
            line_score = 0
            stack.reverse()
            for c in stack:
                line_score *= 5
                line_score += b_score[brackets[c]]
            scores.append(line_score)

    scores.sort()
    print(scores[len(scores)//2])
