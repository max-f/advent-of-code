#!/usr/bin/env python

from utils import utils
from typing import Callable

"""
Code for https://adventofcode.com/2023/day/13
"""


def transpose(grid):
    return [list(x) for x in zip(*grid)]


def find_mirror(pattern_grid):
    # iterate over possible horizontal mirror lines
    for idx in range(1, len(pattern_grid)):
        above = pattern_grid[:idx][::-1]  # mirrored above to compare
        below = pattern_grid[idx:]

        limit = min(len(above), len(below))
        above = above[:limit]
        below = below[:limit]
        if above == below:
            return idx
    return 0


def find_mirror_with_one_mismatch(pattern_grid):
    for idx in range(1, len(pattern_grid)):
        above = pattern_grid[:idx][::-1]  # mirrored above to compare
        below = pattern_grid[idx:]

        mismatch_count = (
            sum(
                sum(
                    0 if char_1 == char_2 else 1 for char_1, char_2 in zip(row_1, row_2)
                )
                for row_1, row_2 in zip(above, below)
            )
            == 1
        )
        if mismatch_count == 1:
            return idx
    return 0


def calculate_total(patterns: list[str], mirror_func: Callable[[list[list[str]]], int]):
    total = 0
    for pattern in patterns:
        grid = [list(row) for row in pattern.split("\n")]
        mirror_idx = mirror_func(grid)
        if mirror_idx:
            total += 100 * mirror_idx
        else:
            grid = transpose(grid)
            mirror_idx = mirror_func(grid)
            total += mirror_idx
    return total


def main():
    input_txt = utils.get_input(13)
    patterns = input_txt.strip().split("\n\n")

    total = calculate_total(patterns, find_mirror)
    total_2 = calculate_total(patterns, find_mirror_with_one_mismatch)

    print(f"Part 1: {total}")
    print(f"Part 2: {total_2}")


if __name__ == "__main__":
    main()
