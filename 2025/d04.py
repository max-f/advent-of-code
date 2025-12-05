#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2025/day/4
"""

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def count_neighbors(grid, pos):
    return sum(
        1
        for d in DIRECTIONS
        if (adj := utils.tuple_add(pos, d)) in grid and grid[adj] == "@"
    )


def part2(grid) -> int:
    grid = grid.copy()
    total_removed = 0

    while True:
        to_remove = []
        for pos, c in grid.items():
            if c != "@":
                continue
            other_rolls = count_neighbors(grid, pos)
            if other_rolls < 4:
                to_remove.append(pos)

        if not to_remove:
            break

        for pos in to_remove:
            grid[pos] = "."

        total_removed += len(to_remove)

    return total_removed


def part1(grid) -> int:
    accessible = 0
    for pos, c in grid.items():
        if c != "@":
            continue
        neighbor_rolls = count_neighbors(grid, pos)
        if neighbor_rolls < 4:
            accessible += 1
    return accessible


def main():
    input_txt = utils.get_input(4)
    lines = input_txt.strip().split("\n")

    grid = {(y, x): c for y, line in enumerate(lines) for x, c in enumerate(line)}
    print(f"Part1: {part1(grid)}")
    print(f"Part1: {part2(grid)}")


if __name__ == "__main__":
    main()
