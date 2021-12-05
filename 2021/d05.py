#!/usr/bin/env python

from utils import utils
from collections import defaultdict

"""
Code for https://adventofcode.com/2021/day/5
"""


def part1(lines) -> int:
    covered = defaultdict(int)

    for s1, s2 in lines:
        x1, y1 = s1
        x2, y2 = s2
        if x1 != x2 and y1 != y2:
            continue
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                line_tuple = (x, y)
                covered[line_tuple] += 1
    return sum(count > 1 for count in covered.values())


def part2(lines) -> int:
    covered = defaultdict(int)

    for s1, s2 in lines:
        x1, y1 = s1
        x2, y2 = s2
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    line_tuple = (x, y)
                    covered[line_tuple] += 1
        else:
            if x1 > x2 and y1 > y2:
                for i in range(x1 - x2 + 1):
                    line_tuple = (x2 + i, y2 + i)
                    covered[line_tuple] += 1
            elif x1 > x2 and y1 < y2:
                for i in range(x1 - x2 + 1):
                    line_tuple = (x2 + i, y2 - i)
                    covered[line_tuple] += 1
            elif x1 < x2 and y1 < y2:
                for i in range(x2 - x1 + 1):
                    line_tuple = (x1 + i, y1 + i)
                    covered[line_tuple] += 1
            elif x1 < x2 and y1 > y2:
                for i in range(x2 - x1 + 1):
                    line_tuple = (x1 + i, y1 - i)
                    covered[line_tuple] += 1
    return sum(count > 1 for count in covered.values())


def main():
    input_txt = utils.get_input(5)
    lines = []
    for line_def in input_txt.strip().split("\n"):
        x1, y1, x2, y2 = utils.ints(line_def)
        lines.append(((x1, y1), (x2, y2)))
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
