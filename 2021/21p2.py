#!/usr/bin/python3


from typing import DefaultDict


if __name__ == "__main__":
    state = DefaultDict(int)
    state[((1, 0), (3, 0))] = 1
    turn = 0
    wins = [0, 0]
    while state:
        new_state = DefaultDict(int)
        player = turn % 2
        for (s, c) in state.items():
            for r1 in range(1, 4):
                for r2 in range(1, 4):
                    for r3 in range(1, 4):
                        r = r1 + r2 + r3
                        (position, score) = s[player]
                        other = s[1-player]
                        position += r
                        if position > 10:
                            position -= 10
                        score += position
                        if score >= 21:
                            wins[player] += c
                        else:
                            if player == 0:
                                new_state[((position, score), other)] += c
                            else:
                                new_state[(other, (position, score))] += c
        turn += 1
        state = new_state
    print(max(wins))
