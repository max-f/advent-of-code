#!/usr/bin/env python
import itertools
from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2021/day/22
"""


def part1(areas):
    cubes = set()
    for area in areas:
        x1, x2, y1, y2, z1, z2 = utils.ints(area)
        a = [list(range(x1, x2 + 1)), list(range(y1, y2 + 1)), list(range(z1, z2 + 1))]
        triples = set(itertools.product(*a))
        if area[:2] == "on":
            cubes |= triples
        else:
            cubes -= triples
    return len(cubes)


def part2(areas):
    pass


def main():
    input_txt = utils.get_input(98)
    lines = input_txt.splitlines()
    # TODO: change to 20
    only_fifty = lines[:10]

    print(f"Part 1: {part1(only_fifty)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
