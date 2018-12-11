#!/usr/bin/env python

from collections import defaultdict
from collections import deque
import operator
import re


GRID_SIZE = 300
MAX_SIZE = 40


def get_hundreds_digit(power_level):
    x = str(power_level)
    if len(x) < 3:
        return 0
    else:
        return int(x[-3])

def find_max(power_levels):
    best = (0, 0)
    max_power_level = -10000
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            this_power_lvl = -10000

            if x > (GRID_SIZE - 2) or y > (GRID_SIZE - 2):
                break

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    this_power_lvl += power_levels[(i, j)]
            if this_power_lvl > max_power_level:
                max_power_level = this_power_lvl
                best = (x, y)
    return best, max_power_level


def find_max_with_size(power_levels):
    best = (0, 0)
    best_size = 0
    max_power_level = 0

    for x in range(1, GRID_SIZE + 1):
        for y in range(1, GRID_SIZE + 1):

            prev_size = 0
            prev_size_sum = 0

            for size in range(1, MAX_SIZE + 1):

                if x > (GRID_SIZE - size) or y > (GRID_SIZE - size):
                    break

                this_power_lvl = 0

                for i in range(x + prev_size, x + size):
                    for j in range(y + prev_size, y + size):
                        print(i, j, size, prev_size)
                        this_power_lvl += power_levels[(i, j)]
                this_power_lvl += prev_size_sum

                if this_power_lvl > max_power_level:
                    max_power_level = this_power_lvl
                    best = (x, y)
                    best_size = size

                prev_size = size
                prev_size_sum = this_power_lvl

    return best, best_size


def main():
    serial_number = 1308
    #serial_number = 18
    #serial_number = 8
    power_levels = dict()

    for x in range(1, GRID_SIZE + 1):
        for y in range(1, GRID_SIZE + 1):
            rack_id = x + 10
            power_lvl = rack_id * y
            power_lvl += serial_number
            power_lvl *= rack_id
            power_lvl = get_hundreds_digit(power_lvl)
            power_lvl -= 5
            power_levels[(x, y)] = power_lvl

    print(max(power_levels.items(), key=operator.itemgetter(1)))

    coord, max_power_level = find_max(power_levels)
    print('Part 1', coord)

    coord, size = find_max_with_size(power_levels)
    print('Part 2', coord, size)


if __name__ == "__main__":
    main()
