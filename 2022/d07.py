#!/usr/bin/env python

from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2022/day/7
"""

SLASH = "/"


def part1(dir_sizes: dict[str, int]) -> int:
    return sum([size for size in dir_sizes.values() if size <= 100000])


def part2(dir_sizes: dict[str, int]) -> int:
    free_up = 30000000 - (70000000 - dir_sizes[SLASH])
    minimal_size = min([size for size in dir_sizes.values() if size > free_up])
    return minimal_size


def main():
    input_txt = utils.get_input(7).strip()
    dirs = defaultdict(int)

    cwd = []
    for line in input_txt.split("\n"):
        if line.startswith("$ cd"):
            _, _, name = line.split(" ")
            if name == "..":
                cwd.pop()
            elif name == SLASH:
                cwd = ['']
            else:
                cwd.append(name)

        if line[0].isdigit():
            (size,) = utils.ints(line)
            name = ""
            for fold in cwd:
                if name != SLASH:
                    name += SLASH
                name += fold
                dirs[name] += size

    print(f"Part1: {part1(dirs)}")
    print(f"Part2: {part2(dirs)}")


if __name__ == "__main__":
    main()
