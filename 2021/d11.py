#!/usr/bin/env python

import itertools
from copy import deepcopy

from utils import utils

"""
Code for https://adventofcode.com/2021/day/11
"""


def neighbors(
    grid: dict[tuple[int, int], int],
    coord: tuple[int, int],
    flash: set[tuple[int, int]],
):
    x, y = coord

    for xd, yd in (
        (-1, -1),
        (1, -1),
        (1, 1),
        (-1, 1),
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ):
        c = x + xd, y + yd
        if c in grid and c not in flash:
            yield c


def check_flash(
    grid: dict[tuple[int, int], int],
    coord: tuple[int, int],
    flash: set[tuple[int, int]],
) -> None:
    if grid[coord] <= 9 or coord in flash:
        return

    flash.add(coord)

    for n in neighbors(grid, coord, flash):
        grid[n] += 1
        check_flash(grid, n, flash)


def part1(grid: dict[tuple[int, int], int]):
    total_flashes = 0
    for _ in range(100):
        flash = set()
        for coord in grid:
            grid[coord] += 1

        for coord in grid:
            check_flash(grid, coord, flash)

        for coord, value in grid.items():
            if value > 9:
                grid[coord] = 0

        total_flashes += len(flash)
    return total_flashes


def part2(grid: dict[tuple[int, int], int]):
    for i in itertools.count(1):
        flash = set()
        for coord in grid:
            grid[coord] += 1

        for coord in grid:
            check_flash(grid, coord, flash)

        for coord, value in grid.items():
            if value > 9:
                grid[coord] = 0

        if len(flash) == 100:
            return i
    return -1


def main():
    input_txt = utils.get_input(11)
    grid = {}
    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, value in enumerate(line):
            grid[x, y] = int(value)

    grid2 = deepcopy(grid)

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid2)}")


if __name__ == "__main__":
    main()
