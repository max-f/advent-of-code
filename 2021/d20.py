#!/usr/bin/env python

from collections import defaultdict
from copy import deepcopy

from utils import utils

"""
Code for https://adventofcode.com/2021/day/20
"""


def enhance(algo, lit_pixels, env_lit):
    new_lit_pixels = defaultdict(bool)
    min_x = min(x for x, y in lit_pixels)
    max_x = max(x for x, y in lit_pixels)
    min_y = min(y for x, y in lit_pixels)
    max_y = max(y for x, y in lit_pixels)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            idx = []
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    coord = (x + dx, y + dy)
                    idx_digit = lit_pixels[coord] or (
                        env_lit
                        and not (
                            min_x <= coord[0] <= max_x and min_y <= coord[1] <= max_y
                        )
                    )
                    idx.append(idx_digit)

            bin_idx = "0b" + "".join(["1" if x else "0" for x in idx])
            value = algo[int(bin_idx, 2)]
            if value:
                new_lit_pixels[x, y] = True

    env_lit = not env_lit if algo[0] else False
    return new_lit_pixels, env_lit


def part1(algo, lit_pixels):
    env_lit = False
    for _ in range(2):
        lit_pixels, env_lit = enhance(algo, lit_pixels, env_lit)
    return len(lit_pixels)


def part2(algo, lit_pixels):
    env_lit = False
    for _ in range(50):
        lit_pixels, env_lit = enhance(algo, lit_pixels, env_lit)
    return len(lit_pixels)


def main():
    input_txt = utils.get_input(20)
    lines = input_txt.splitlines()
    algo_line = lines[0]

    algo = [True if c == "#" else False for c in algo_line]
    image_lines = lines[2:]

    lit_pixels = defaultdict(bool)
    for y, line in enumerate(image_lines):
        for x, c in enumerate(line):
            if c == "#":
                lit_pixels[x, y] = True

    lit_pixels2 = deepcopy(lit_pixels)

    print(f"Part 1: {part1(algo, lit_pixels)}")
    print(f"Part 2: {part2(algo, lit_pixels2)}")


if __name__ == "__main__":
    main()
