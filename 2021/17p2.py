#!/usr/bin/python3

"""
x velocity must be between 21 and 283
y velocity must be between -107 and 106
"""

hits = 0

for init_xv in range(21, 284):
    for init_yv in range(-107, 107):
        x = 0
        y = 0
        xv = init_xv
        yv = init_yv
        while True:
            x += xv
            y += yv
            if xv > 0:
                xv -= 1
            yv -= 1
            if y < -107:
                break
            if 230 <= x <= 283:
                if -107 <= y <= -57:
                    hits += 1
                    break

print(hits)
