#!/usr/bin/python3

import re
from bitarray import bitarray


if __name__ == "__main__":
    commands = []
    xset = set()
    yset = set()
    zset = set()
    with open('22.txt') as input:
        for line in input.readlines():
            match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
            if match:
                (on_off, xmin, xmax, ymin, ymax, zmin, zmax) = match.groups()
                (xmin, xmax, ymin, ymax, zmin, zmax) = [int(i) for i in (xmin, xmax, ymin, ymax, zmin, zmax)]
                xmax += 1
                ymax += 1
                zmax += 1
                command = (on_off == "on", xmin, xmax, ymin, ymax, zmin, zmax)
                commands.append(command)
                xset.add(xmin)
                xset.add(xmax)
                yset.add(ymin)
                yset.add(ymax)
                zset.add(zmin)
                zset.add(zmax)
    xlist = [i for i in xset]
    xlist.sort()
    ylist = [i for i in yset]
    ylist.sort()
    zlist = [i for i in zset]
    zlist.sort()
    x_to_index = dict()
    for i in range(len(xlist)):
        x_to_index[xlist[i]] = i
    y_to_index = dict()
    for i in range(len(ylist)):
        y_to_index[ylist[i]] = i
    z_to_index = dict()
    for i in range(len(zlist)):
        z_to_index[zlist[i]] = i

    cuboids_on = [[bitarray(len(zlist)) for y in range(len(ylist))] for x in range(len(xlist))]
    for x in range(len(xlist)):
        for y in range(len(ylist)):
            cuboids_on[x][y].setall(0)

    for command in commands:
        ixmin = x_to_index[command[1]]
        ixmax = x_to_index[command[2]]
        iymin = y_to_index[command[3]]
        iymax = y_to_index[command[4]]
        izmin = z_to_index[command[5]]
        izmax = z_to_index[command[6]]
        for x in range(ixmin, ixmax):
            for y in range(iymin, iymax):
                cuboids_on[x][y][izmin:izmax] = command[0]
        print(command)
    on = 0
    for x in range(len(xlist)):
        for y in range(len(ylist)):
            for z in range(len(zlist)):
                if cuboids_on[x][y][z]:
                    xsize = xlist[x+1] - xlist[x]
                    ysize = ylist[y+1] - ylist[y]
                    zsize = zlist[z+1] - zlist[z]
                    on += (xsize * ysize * zsize)

    print(on)
