#!/usr/bin/python3


if __name__ == "__main__":
    positions = [1, 3]
    scores = [0, 0]
    rolls = 0
    player = 0
    while all([score < 1000 for score in scores]):
        roll = (rolls + 1, rolls + 2, rolls + 3)
        rolls += 3
        roll = sum(roll)
        positions[player] += (roll % 10)
        while positions[player] > 10:
            positions[player] -= 10
        scores[player] += positions[player]
        player = 1 - player
    print(positions)
    print(scores)
    print(rolls)
    print(rolls * min(scores))
