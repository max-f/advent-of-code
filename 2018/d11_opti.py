#!/usr/bin/env python

from collections import defaultdict
from collections import deque
import operator
import re


GRID_SIZE = 300
MAX_SIZE = 50


class Grid:
    def __init__(self, serial_number):
        self.power_levels = dict()

        for x in range(1, GRID_SIZE + 1):
            for y in range(1, GRID_SIZE + 1):
                rack_id = x + 10
                power_lvl = rack_id * y
                power_lvl += serial_number
                power_lvl *= rack_id
                power_lvl = get_hundreds_digit(power_lvl)
                power_lvl -= 5
                self.power_levels[(x, y)] = power_lvl

    def find_max(self, size):
        best_cell = (0, 0)
        max_power_lvl = -10000

        for x in range(1, GRID_SIZE + 1):
            for y in range(1, GRID_SIZE + 1):
                this_power_lvl = -10000

                if x > (GRID_SIZE - size - 1) or y > (GRID_SIZE - size - 1):
                    break

                for i in range(x, x + size):
                    for j in range(y, y + size):
                        this_power_lvl += self.power_levels[(i, j)]
                if this_power_lvl > max_power_lvl:
                    max_power_lvl = this_power_lvl
                    best_cell = (x, y)
        return best_cell, max_power_lvl

    def find_general_max(self):
        best = (0, 0)
        best_size = 0
        max_power_level = -10000

        for x in range(1, GRID_SIZE + 1):
            for y in range(1, GRID_SIZE + 1):

                prev_size = 0
                prev_size_sum = 0

                for size in range(1, MAX_SIZE + 1):

                    if x > (GRID_SIZE - size) or y > (GRID_SIZE - size):
                        print("broken")
                        break

                    this_power_lvl = prev_size_sum

                    next_up = set()
                    for i in range(x, size + 1):
                        next_up.add((i, y + prev_size))
                    for j in range(y, size + 1):
                        next_up.add((x + prev_size, j))

                    for cell in next_up:
                        this_power_lvl += self.power_levels[cell]

                    if this_power_lvl > max_power_level:
                        max_power_level = this_power_lvl
                        best = (x, y)
                        best_size = size

                    prev_size = size
                    prev_size_sum = this_power_lvl

        print(max_power_level)
        return best, best_size


def get_hundreds_digit(power_level):
    x = str(power_level)
    if len(x) < 3:
        return 0
    else:
        return int(x[-3])


def main():
    serial_number = 1308
    # serial_number = 18
    # serial_number = 8

    grid = Grid(serial_number)
    best_cell, max_power_lvl = grid.find_max(3)
    print(f"Part 1: {best_cell}")

    best_cell, best_size = grid.find_general_max()
    print(f"Part 2: {best_cell[0]},{best_cell[1]},{best_size}")


if __name__ == "__main__":
    main()
