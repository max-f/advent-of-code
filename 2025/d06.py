#!/usr/bin/env python


import math
import re
from itertools import groupby

from utils import utils

"""
Code for https://adventofcode.com/2025/day/6
"""

OPS = {"*": math.prod, "+": sum}


def convert(val):
    return int(val) if val.isdigit() else val


def part1(input_txt: str) -> int:
    matrix = [re.findall(r"[0-9+*]+", line) for line in input_txt.strip().splitlines()]
    transposed = [[convert(x) for x in col] for col in zip(*matrix)]

    return sum(OPS[calc[-1]](calc[:-1]) for calc in transposed)


def part2(input_txt: str) -> int:
    lines = input_txt.strip().splitlines()
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    *num_lines, op_line = padded_lines
    all_ops = op_line.split()

    columns = ["".join(col) for col in zip(*num_lines)]
    # empty strings are separators:
    # ['1  ', '24 ', '356', '   ', '369', '248', '8  ', '   ', ' 32', '581', '175', '   ', '623', '431', '  4']
    groups = [list(g) for k, g in groupby(columns, key=lambda x: x.strip() != "") if k]

    return sum(
        OPS[op]([int(x) for x in numbers]) for op, numbers in zip(all_ops, groups)
    )


def main():
    input_txt = utils.get_input(6)

    print(f"Part1: {part1(input_txt)}")
    print(f"Part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
