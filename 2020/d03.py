#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/3
"""


def part1(tree_map: str) -> int:
    return check_slope_for_trees(tree_map, 3, 1)


def part2(tree_map: str) -> int:
    slope_1 = check_slope_for_trees(tree_map, 1, 1)
    slope_2 = check_slope_for_trees(tree_map, 3, 1)
    slope_3 = check_slope_for_trees(tree_map, 5, 1)
    slope_4 = check_slope_for_trees(tree_map, 7, 1)
    slope_5 = check_slope_for_trees(tree_map, 1, 2)
    return slope_1 * slope_2 * slope_3 * slope_4 * slope_5


def check_slope_for_trees(tree_map: str, right: int, down: int) -> int:
    trees = 0
    x = 0
    lines = tree_map.split("\n")
    for i in range(0, len(lines) - 1, down):
        xs = list(lines[i])
        if xs[x] == "#":
            trees += 1
        x = (x + right) % len(xs)
    return trees


def main():
    input_txt = utils.get_input(3)
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
