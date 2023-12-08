#!/usr/bin/env python

import math
import re
from itertools import cycle

from utils import utils

"""
Code for https://adventofcode.com/2023/day/8
"""


def part1(seq, move_map) -> int:
    current = 'AAA'
    for i, move in enumerate(cycle(seq)):
        if current == 'ZZZ':
            return i
        left, right = move_map[current]
        current = left if move == 'L' else right


def calc_step_count(seq, move_map, start):
    current = start
    for i, move in enumerate(cycle(seq)):
        if current.endswith('Z'):
            return i
        left, right = move_map[current]
        current = left if move == 'L' else right


def part2(seq, move_map):
    steps = [
        calc_step_count(seq, move_map, start)
        for start in move_map
        if start.endswith("A")
    ]
    return math.lcm(*steps)


def main():
    input_txt = utils.get_input(8)
    seq, map_stuff = input_txt.strip().split("\n\n")
    map_lines = map_stuff.split("\n")
    move_map = {}
    for line in map_lines:
        start, left, right = re.findall(r"[a-zA-Z0-9]+", line)
        move_map[start] = (left, right)

    print(f"Part1: {part1(seq, move_map)}")
    print(f"Part2: {part2(seq, move_map)}")


if __name__ == "__main__":
    main()
