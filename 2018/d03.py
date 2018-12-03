#!/usr/bin/env python

from collections import defaultdict
from utils import utils
import re


def create_rectangle_set(line):
    pattern = r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    regex = re.compile(pattern)
    match = regex.match(line)
    x = int(match.group(2))
    y = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    f_id = int(match.group(1))

    coordinates = set()
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            coordinates.add((i + y, j + x))
    return f_id, coordinates


def is_overlapping(all_rect, f_id):
    rect = all_rect[f_id]
    for f_id_2, rect2 in all_rect.items():
        if f_id != f_id_2 and rect & rect2:
            return True
    return False


def main():
    input_txt = utils.get_input(3)
    lines = input_txt.split("\n")
    all_pos = set()
    overlap = set()
    all_fabrics = dict()

    for line in lines:
        if line:
            f_id, fabric_rect = create_rectangle_set(line)
            overlap = overlap.union(fabric_rect & all_pos)
            all_pos = all_pos.union(fabric_rect)
            all_fabrics[f_id] = fabric_rect

    print(f"Part 1: {len(overlap)}")

    for f_id in all_fabrics.keys():
        if is_overlapping(all_fabrics, f_id):
            continue
        else:
            print(f"Part 2: {f_id}")
            return


if __name__ == "__main__":
    main()
