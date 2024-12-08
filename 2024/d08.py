#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations

from utils import utils

"""
Code for https://adventofcode.com/2024/day/8
"""

type AntennaDict = dict[int, list[tuple[int, int]]]


def is_valid_pos(pos, max_x, max_y) -> bool:
    return 0 <= pos[0] < max_y and 0 <= pos[1] < max_x


def part1(antennas: AntennaDict, max_x: int, max_y: int) -> int:
    antinodes = set()

    def calc_antinode_pos(a1: tuple[int, int], a2: tuple[int, int]) -> None:
        y1, x1 = a1
        y2, x2 = a2
        new_x = x2 + (x2 - x1)
        new_y = y2 + (y2 - y1)
        if is_valid_pos((new_y, new_x), max_x, max_y):
            antinodes.add((new_y, new_x))

    for antenna_type in antennas.values():
        for a1, a2 in permutations(antenna_type, 2):
            calc_antinode_pos(a1, a2)
    return len(antinodes)


def part2(antennas: AntennaDict, max_x: int, max_y: int) -> int:
    antinodes = set()

    def calc_antinode_pos(a1: tuple[int, int], a2: tuple[int, int]) -> None:
        y1, x1 = a1
        y2, x2 = a2
        new_x = x2 + (x2 - x1)
        new_y = y2 + (y2 - y1)
        antinodes.add((y2, x2))
        while is_valid_pos((new_y, new_x), max_x, max_y):
            antinodes.add((new_y, new_x))
            new_x += x2 - x1
            new_y += y2 - y1

    for antenna_type in antennas.values():
        for a1, a2 in permutations(antenna_type, 2):
            calc_antinode_pos(a1, a2)

    return len(antinodes)


def main():
    input_txt = utils.get_input(8)
    lines = input_txt.strip().split("\n")
    max_x = len(lines[0])
    max_y = len(lines)

    antennas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                antennas[c].append((i, j))

    print(f"Part1: {part1(antennas, max_x, max_y)}")
    print(f"Part2: {part2(antennas, max_x, max_y)}")


if __name__ == "__main__":
    main()
