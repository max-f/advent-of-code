#!/usr/bin/env python

import re

from utils import utils

ITERATIONS = 100000
RANGE = 80


def print_data(positions, n, min_x, max_x, min_y, max_y):
    print()
    print()
    print("#" * 30)
    print("Iteration: ", n + 1)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print("\n")


def main():
    data = utils.get_input(10)
    data = data.split("\n")[:-1]
    positions = []
    velocities = []

    pattern = r"^.*<([- 0-9]+),([- 0-9]+).*<([- 0-9]+),([- 0-9]+)>.*$"
    regex = re.compile(pattern)

    for i, line in enumerate(data):
        match = regex.match(line)
        if match:
            pos_x = int(match.group(1))
            pos_y = int(match.group(2))
            vel_x = int(match.group(3))
            vel_y = int(match.group(4))
            positions.append((pos_x, pos_y))
            velocities.append((vel_x, vel_y))
        else:
            print("WARN: ", line)

    print("Length pos: ", len(positions))
    print("Length vel: ", len(velocities))

    for n in range(ITERATIONS):
        new_pos = []
        for i, (p_x, p_y) in enumerate(positions):
            v_x, v_y = velocities[i][0], velocities[i][1]
            new_pos.append((p_x + v_x, p_y + v_y))
        positions = new_pos
        min_x = min([x for x, y in positions])
        max_x = max([x for x, y in positions])
        min_y = min([y for x, y in positions])
        max_y = max([y for x, y in positions])

        if min_x + RANGE >= max_x and min_y + RANGE >= max_y:
            print_data(positions, n, min_x, max_x, min_y, max_y)


if __name__ == "__main__":
    main()
