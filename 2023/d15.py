#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

from utils import utils

"""
Code for https://adventofcode.com/2023/day/15
"""


def hash_value(s) -> int:
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def part1(s) -> int:
    return sum(hash_value(seq) for seq in s.split(','))


def part2(s) -> int:
    boxes = defaultdict(dict)
    for seq in s.split(','):
        if '=' in seq:
            label, lens = seq.split('=')
            box_number = hash_value(label)
            boxes[box_number][label] = int(lens)
        elif '-' in seq:
            label = seq[:-1]
            box_number = hash_value(label)
            boxes[box_number].pop(label, None)
    pprint(boxes)

    result = 0
    for i, box in boxes.items():
        for j, lens in enumerate(box.values()):
            result += (1 + i) * (j + 1) * lens

    return result


def main():
    input_txt = utils.get_input(15).strip()

    print(f"Part 1: {part1(input_txt)}")
    print(f"Part 2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
