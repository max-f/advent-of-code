#!/usr/bin/env python

from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2020/day/24
"""

directions = {
    "e": (1, 0, -1),
    "se": (0, 1, -1),
    "sw": (-1, 1, 0),
    "w": (-1, 0, 1),
    "nw": (0, -1, 1),
    "ne": (1, -1, 0),
}


def part2(map_):
    for _ in range(100):
        to_be_checked = {t for t, v in map_.items() if v}
        for t in list(to_be_checked):
            to_be_checked.update(utils.tuple_add(t, d) for d in directions.values())

        new_map = defaultdict(bool)
        for t in to_be_checked:
            number_of_black_neighbors = calc_black_neighbors(map_, t)
            is_black = map_[t]
            if is_black and number_of_black_neighbors in (1, 2):
                new_map[t] = True
            elif not is_black and number_of_black_neighbors == 2:
                new_map[t] = True
        map_ = new_map

    print(sum(1 for t, v in map_.items() if v))


def calc_black_neighbors(map_, t):
    return sum([map_[utils.tuple_add(t, d)] for d in directions.values()])


def main():
    input_txt = utils.get_input(24).rstrip()
    lines = input_txt.split("\n")

    map_ = defaultdict(bool)

    for line in lines:
        start = (0, 0, 0)
        i = 0
        while i < len(line):
            if line[i] in directions:
                start = utils.tuple_add(start, directions[line[i]])
                i += 1
            elif line[i : i + 2] in directions:
                start = utils.tuple_add(start, directions[line[i : i + 2]])
                i += 2
            else:
                raise ValueError

        map_[start] = not map_[start]

    print(sum(1 for k, v in map_.items() if v))
    part2(map_)


if __name__ == "__main__":
    main()
