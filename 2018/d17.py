#!/usr/bin/env python

import re
from collections import defaultdict

from utils import utils

BLOCKED = '#~'


def print_map(M):
    for y in range(len(M[0])):
        for x in range(len(M)):
            print(M[x][y], end='')
        print('\n')


def parse(line):
    return list(map(int, re.findall(r"\d+", line)))


def water_down(M, x, y):
    while True:
        if y < len(M[0]) - 1:
            next_tile = M[x][y + 1]
        else:
            return

        # Expanding downward
        if next_tile not in BLOCKED:
            M[x][y] = '|'
            y += 1
            continue

        # Reaching clay or staying water
        elif next_tile in BLOCKED:
            M[x][y] = '~'
            expanding = False

            # Go to the right side if possible
            if M[x + 1][y] not in BLOCKED:
                water_down(M, x + 1, y)
                expanding = True

            # Go to the left side if possible
            if M[x - 1][y] not in BLOCKED:
                water_down(M, x - 1, y)
                expanding = True

            # If expanding not possible: go up
            if not expanding and M[x][y - 1] not in BLOCKED:
                water_down(M, x, y - 1)


def main():
    lines = utils.get_input(48).split("\n")
    clay = defaultdict(set)
    max_clay = 0
    min_clay = 1000
    min_x = 1000
    max_x = 0

    for line in lines:
        if line[0] == 'x':
            x, y1, y2 = parse(line)
            clay[x].update(set(range(y1, y2 + 1)))
            if y1 < min_clay:
                min_clay = y1
            if y2 > max_clay:
                max_clay = y2
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

        else:
            y, x1, x2 = parse(line)
            for x in range(x1, x2 + 1):
                clay[x].add(y)
            if x1 < min_x:
                min_x = x1
            if x2 > max_x:
                max_x = x2
            if y < min_clay:
                min_clay = y
            if y > max_clay:
                max_clay = y

    # Add one free column to the left and right to eventually let water flow
    map_size_x = max_x - min_x + 2
    M = [['.' for y in range(0, max_clay + 1)] for x in range(map_size_x + 1)]
    print(min_x)

    for x in range(min_x, max_x + 1):
        for y in clay[x]:
            # Add one buffer to the left
            M[x - min_x + 1][y] = '#'

    print_map(M)
    water_down(M, 500 - min_x + 1, 0)
    print()
    print('*' * 20)
    print_map(M)


if __name__ == "__main__":
    main()
