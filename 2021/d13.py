#!/usr/bin/env python

import re

from utils import utils

"""
Code for https://adventofcode.com/2021/day/13
"""


def solution(dots: set[tuple[int, int]], folds: list[tuple[str, int]]) -> None:
    for i, fold in enumerate(folds):
        axis, p = fold
        new_dots = set()
        for x, y in dots:
            if axis == "x" and x > p:
                new_dot = ((2 * p - x), y)
                new_dots.add(new_dot)
            elif axis == "y" and y > p:
                new_dot = (x, (2 * p - y))
                new_dots.add(new_dot)
            else:
                new_dots.add((x, y))
        dots = new_dots
        if i == 0:
            print(f"Part 1: {len(new_dots)}")

    x_max = max(x for x, _ in dots)
    y_max = max(y for _, y in dots)

    print("Part 2:")
    for y in range(y_max + 1):
        print("".join("█" if (x, y) in dots else " " for x in range(x_max + 1)))


def main():
    input_txt = utils.get_input(13)
    dot_lines, fold_lines = input_txt.split("\n\n")
    dots = set()
    for dot in dot_lines.splitlines():
        x, y = dot.split(",")
        dots.add((int(x), int(y)))

    folds = []
    fold_regex = re.compile(r".*([xy])=(\d+)")
    for fold in fold_lines.splitlines():
        match = fold_regex.match(fold)
        folds.append((match.group(1), int(match.group(2))))

    solution(dots, folds)


if __name__ == "__main__":
    main()
