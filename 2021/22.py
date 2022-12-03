#!/usr/bin/python3

import re


if __name__ == "__main__":
    cubes = set()
    with open('22.txt') as input:
        for line in input.readlines():
            match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
            if match:
                (on_off, xmin, xmax, ymin, ymax, zmin, zmax) = match.groups()
                (xmin, xmax, ymin, ymax, zmin, zmax) = [int(i) for i in (xmin, xmax, ymin, ymax, zmin, zmax)]
                if any([amax < -50 for amax in (xmax, ymax, zmax)]):
                    continue
                if any([amin > 50 for amin in (xmin, ymin, zmin)]):
                    continue
                xmin = max(-50, xmin)
                ymin = max(-50, ymin)
                zmin = max(-50, zmin)

                xmax = min(50, xmax)
                ymax = min(50, ymax)
                zmax = min(50, zmax)

                if on_off == "on":
                    print(xmin, xmax, ymin, ymax, zmin, zmax)
                    for x in range(xmin, xmax + 1):
                        for y in range(ymin, ymax + 1):
                            for z in range(zmin, zmax + 1):
                                cubes.add((x, y, z))
                else:
                    for x in range(xmin, xmax + 1):
                        for y in range(ymin, ymax + 1):
                            for z in range(zmin, zmax + 1):
                                cubes.discard((x, y, z))
            print(len(cubes))
