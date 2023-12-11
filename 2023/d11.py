#!/usr/bin/env python

from pprint import pprint

from utils import utils

"""
Code for https://adventofcode.com/2023/day/11
"""


def read_and_process_grid(lines):
    grid = lines

    empty_rows = [i for i, row in enumerate(grid) if "#" not in row]
    empty_cols = [j for j, col in enumerate(zip(*grid)) if "#" not in col]

    galaxies = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))

    return galaxies, empty_rows, empty_cols


def main():
    input_txt = utils.get_input(11)
    lines = input_txt.strip().split("\n")
    pprint(lines)
    galaxies, empty_rows, empty_cols = read_and_process_grid(lines)
    pprint(galaxies)
    pprint(empty_rows)
    pprint(empty_cols)

    p1, p2 = 0, 0
    for i, (ax, ay) in enumerate(galaxies):
        for bx, by in galaxies[i + 1 :]:
            p1 += abs(ax - bx) + abs(ay - by)
            p2 += abs(ax - bx) + abs(ay - by)
            for y in empty_rows:
                if ay < y < by or by < y < ay:
                    p1 += 1
                    p2 += 999999
            for x in empty_cols:
                if ax < x < bx or bx < x < ax:
                    p1 += 1
                    p2 += 999999

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
