#!/usr/bin/env python
from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2021/day/25
"""

x_size, y_size = 0, 0


def next_step(coord, value):
    x, y = coord
    if value == ">":
        return (x + 1) % x_size, y
    else:
        return x, (y + 1) % y_size


def move_cucumbers(grid, other_grid):
    changed = False
    grid_new = grid.copy()
    for k, v in grid.items():
        next_coord = next_step(k, v)
        if next_coord not in grid and next_coord not in other_grid:
            changed = True
            grid_new.pop(k)
            grid_new[next_coord] = v
    return grid_new, changed


def part1(grid_east, grid_south):
    counter = 0
    changed = True

    while changed:
        grid_east, changed_east = move_cucumbers(grid_east, grid_south)
        grid_south, changed_south = move_cucumbers(grid_south, grid_east)
        changed = changed_east or changed_south

        counter += 1
        # print_grid(grid_east, grid_south)

    return counter


def print_grid(grid_east, grid_south):
    grid = ""

    for y in range(0, y_size):
        for x in range(0, x_size):
            coord = x, y
            if coord in grid_east:
                grid += ">"
            elif coord in grid_south:
                grid += "v"
            else:
                grid += "."
        grid += "\n"
    print(grid)


def main():
    input_txt = utils.get_input(25)
    lines = input_txt.splitlines()
    global x_size
    global y_size
    y_size = len(lines)
    x_size = len(lines[0])

    grid_east = defaultdict(str)
    grid_south = defaultdict(str)
    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, char in enumerate(line):
            if char == ">":
                grid_east[x, y] = char
            elif char == "v":
                grid_south[x, y] = char
    print(f"Part 1: {part1(grid_east, grid_south)}")


if __name__ == "__main__":
    main()
