#!/usr/bin/env python

import bisect

from utils import utils

"""
Code for https://adventofcode.com/2025/day/5
"""


def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def is_element_of_range(number, ranges):
    starts = [start for start, _ in ranges]
    idx = bisect.bisect_right(starts, number) - 1

    if idx >= 0:
        start, end = ranges[idx]
        return start <= number <= end
    return False


def main():
    input_txt = utils.get_input(5)

    id_ranges, ingredients = input_txt.split("\n\n")
    range_lines = id_ranges.split("\n")
    ranges = [(int(x), int(y)) for line in range_lines for x, y in [line.split("-")]]
    merged_ranges = merge_ranges(ranges)

    p2 = sum((end - start) + 1 for start, end in merged_ranges)

    p1 = sum(
        1
        for s in ingredients.splitlines()
        if is_element_of_range(int(s), merged_ranges)
    )

    print(f"Part1: {p1}")
    print(f"Part2: {p2}")


if __name__ == "__main__":
    main()
