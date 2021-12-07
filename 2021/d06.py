#!/usr/bin/env python
import copy

from utils import utils
from collections import defaultdict
from copy import deepcopy

"""
Code for https://adventofcode.com/2021/day/6
"""


def part1(lantern_fish: list[int]) -> int:
    for _ in range(80):
        new_fish_list = []
        for i, fish_counter in enumerate(lantern_fish):
            if not fish_counter:
                new_fish_list.append(8)
                lantern_fish[i] = 6
            else:
                lantern_fish[i] -= 1
        lantern_fish.extend(new_fish_list)

    return len(lantern_fish)


def part2(lantern_fish: list[int]) -> int:
    fish_counts = [lantern_fish.count(i) for i in range(9)]
    for _ in range(256):
        new_fish_count = fish_counts.pop(0)
        fish_counts[6] += new_fish_count
        fish_counts.append(new_fish_count)
    return sum(fish_counts)


def main():
    input_txt = utils.get_input(6)
    lantern_fish = utils.ints(input_txt)
    lantern_fish2 = copy.deepcopy(lantern_fish)
    print(f"Part 1: {part1(lantern_fish)}")
    print(f"Part 2: {part2(lantern_fish2)}")


if __name__ == "__main__":
    main()
