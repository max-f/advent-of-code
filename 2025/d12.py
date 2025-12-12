#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2025/day/12
"""


def main():
    input_txt = utils.get_input(12)
    parts = input_txt.strip().split("\n\n")
    present_patterns = parts[:-1]
    regions = parts[-1].split("\n")

    covered = [pattern.count("#") for pattern in present_patterns]
    certain_count, impossible_count, uncertain_count = 0, 0, 0

    for region in regions:
        dimensions, present_refs = region.split(": ")
        present_refs = utils.ints(present_refs)

        total_presents = sum(present_refs)

        x, y = utils.lmap(int, dimensions.split("x"))
        minimal_space_required = sum(n * c for n, c in zip(present_refs, covered))

        if minimal_space_required > x * y:
            impossible_count += 1
        elif total_presents <= (x // 3) * (y // 3):
            certain_count += 1
        else:
            uncertain_count += 1

    print(f"yes: {certain_count}")
    print(f"no: {impossible_count}")
    print(f"undecided: {uncertain_count}")


if __name__ == "__main__":
    main()
