#!/usr/bin/env python


import itertools

from utils import utils

"""
Code for https://adventofcode.com/2025/day/9
"""


def part2(points):
    min_x = min(points, key=lambda p: p[0])
    min_y = min(points, key=lambda p: p[1])
    max_x = max(points, key=lambda p: p[0])
    max_y = max(points, key=lambda p: p[1])
    print(min_x, min_y, max_x, max_y)


def main():
    input_txt = utils.get_input(9)
    lines = input_txt.strip().splitlines()

    points = [tuple(utils.ints(line)) for line in lines]

    max_points = -1
    all_pairs = itertools.combinations(points, 2)
    for p1, p2 in all_pairs:
        x1, y1 = p1
        x2, y2 = p2
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        max_points = max(max_points, area)

    print(f"Part1: {max_points}")
    print(f"Part 2: {part2(points)}")


if __name__ == "__main__":
    main()
