#!/usr/bin/python3

"""
x, y, z
x, -z, y
x, -y, -z
x, z, -y

y, z, x
y, -x, z
y, -z, -x
y, x, -z

z, x, y
z, -y, x
z, -x, -y
z, y, -x

-x, y, -z
-x, -z, -y
-x, -y, z
-x, z, y

-y, z, -x
-y, -x, -z
-y, -z, x
-y, x, z

-z, x, -y
-z, -y, -x
-z, -x, y
-z, y, x
"""

import re


class Scanner:
    orientations = (
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
        ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
        ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
        ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
        ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
        ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
        ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
        ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
        ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
        ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
        ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
        ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
        ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
        ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
        ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
        ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
        ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
        ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
        ((0, 0, -1), (0, 1, 0), (1, 0, 0))
        )

    def __init__(self, name):
        self.name = name
        self.beacon_obs = list()
        self.position = None
        self.orientation = None
        self.aligned = False
        self._rotated_beacons = None
        self._absolute_beacons = None
        self.tried = False

    def rotated_beacons(self):

        def rot(matrix, x, y, z):
            xr = (matrix[0][0] * x) + (matrix[0][1] * y) + (matrix[0][2] * z)
            yr = (matrix[1][0] * x) + (matrix[1][1] * y) + (matrix[1][2] * z)
            zr = (matrix[2][0] * x) + (matrix[2][1] * y) + (matrix[2][2] * z)
            return (xr, yr, zr)

        if (not self.aligned) or (not self._rotated_beacons):
            self._rotated_beacons = [rot(self.orientation, x, y, z) for (x, y, z) in self.beacon_obs]
        return self._rotated_beacons

    def absolute_beacons(self):
        if (not self.aligned) or (not self._absolute_beacons):
            self._absolute_beacons = [(x + self.position[0], y + self.position[1], z + self.position[2]) for (x, y, z) in self.rotated_beacons()]
        return self._absolute_beacons

    def align_to(self, other):
        abs_other = other.absolute_beacons()
        for orientation in Scanner.orientations:
            self.orientation = orientation
            rotated = self.rotated_beacons()
            for source in rotated:
                for target in abs_other:
                    self.position = (target[0] - source[0], target[1] - source[1], target[2] - source[2])
                    abs_ours = self.absolute_beacons()
                    matched = 0
                    for ours in abs_ours:
                        if ours in abs_other:
                            matched += 1
                    if matched >= 12:
                        self.aligned = True
                        return True

        return self.aligned


if __name__ == "__main__":
    # Parse input
    scanners = list()
    with open('19.txt') as input:
        for line in input.readlines():
            match_scanner = re.match(r"--- (.+) ---", line)
            match_coords = re.match(r"(-?\d+),(-?\d+),(-?\d+)", line)
            if match_scanner:
                scanners.append(Scanner(match_scanner[1]))
            elif match_coords:
                (x, y, z) = [int(coord) for coord in match_coords.group(1, 2, 3)]
                scanners[-1].beacon_obs.append((x, y, z))

    # Find pairs of scanners to align to each other
    all_aligned = False
    scanners[0].position = (0, 0, 0)
    scanners[0].orientation = Scanner.orientations[0]
    scanners[0].aligned = True
    while not all_aligned:
        all_aligned = True
        for i in scanners:
            if not i.aligned:
                all_aligned = False
                continue
            if i.tried:
                continue
            for j in scanners:
                if j.aligned:
                    continue
                # print("Trying {} to {}".format(j.name, i.name))
                if j.align_to(i):
                    print("Aligned {} to {}".format(j.name, i.name))
            i.tried = True

    # Create set of all beacon locations
    beacons = set()
    for scanner in scanners:
        for beacon in scanner.absolute_beacons():
            beacons.add(beacon)
    print("Number of beacons: {}".format(len(beacons)))

    # Find largest Manhattan distance between scanners
    largest = 0
    for i in scanners:
        for j in scanners:
            distance = sum([abs(i.position[axis] - j.position[axis]) for axis in range(3)])
            largest = max(largest, distance)
    print("Max distance: {}".format(largest))
