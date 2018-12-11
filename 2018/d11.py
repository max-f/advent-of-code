#!/usr/bin/env python

from collections import defaultdict, deque
import operator
import re

import numpy as np

GRID_SIZE = 300
MAX_SIZE = 50
ARBITRARY_LOW = -10000


class Grid:
    def __init__(self, serial_number):
        self.power_levels = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rack_id = (x + 1) + 10
                power_lvl = (y + 1) * rack_id
                power_lvl += serial_number
                power_lvl *= rack_id
                power_lvl = get_hundreds_digit(power_lvl)
                power_lvl -= 5
                self.power_levels[(x, y)] = power_lvl

    def find_max(self, size):
        best_cell = (0, 0)
        max_power_lvl = ARBITRARY_LOW

        for x in range(GRID_SIZE - size + 1):
            for y in range(GRID_SIZE - size + 1):
                current_power_lvl = ARBITRARY_LOW

                current_power_lvl = np.sum(
                    self.power_levels[x : x + size, y : y + size]
                )
                if current_power_lvl > max_power_lvl:
                    max_power_lvl = current_power_lvl
                    best_cell = (x + 1, y + 1)
        return best_cell, max_power_lvl

    def find_general_max(self):
        best_cell = (0, 0)
        best_size = 0
        max_power_lvl = ARBITRARY_LOW
        for size in range(MAX_SIZE):
            current_cell, current_power_lvl = self.find_max(size)
            if current_power_lvl > max_power_lvl:
                best_cell = current_cell
                best_size = size
                max_power_lvl = current_power_lvl
        return best_cell, best_size


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
