#!/usr/bin/env python


from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2025/day/7
"""


def solve(lines):
    start = lines[0].index("S")
    beams = {start: 1}
    splits = 0

    for row in lines:
        if "^" not in row:
            continue

        next_beams = defaultdict(int)

        for i, n in beams.items():
            if row[i] == "^":
                splits += 1
                next_beams[i - 1] += n
                next_beams[i + 1] += n
            else:
                next_beams[i] += n
        beams = next_beams
    return splits, sum(beams.values())


def main():
    input_txt = utils.get_input(7)

    lines = input_txt.strip().splitlines()
    p1, p2 = solve(lines)
    print(f"Part1: {p1}")
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()
