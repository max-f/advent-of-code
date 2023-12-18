#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2023/day/18
"""

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

DIRECTIONS2 = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def calculate_total_trench(corner_points, total_border_points):
    # Shoelace formula - area of simple polygon
    # https://en.wikipedia.org/wiki/Shoelace_formula
    A = (
        abs(
            sum(
                corner_points[i][0]
                * (
                    corner_points[(i + 1) % len(corner_points)][1]
                    - corner_points[i - 1][1]
                )
                for i in range(len(corner_points))
            )
        )
        / 2
    )

    # Pick's theorem resolved to i
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # A = i + b / 2 - 1
    i = int(A - total_border_points / 2 + 1)

    return i + total_border_points


def part1(lines) -> int:
    corner_points = []

    total_border_points = 0
    pos = (0, 0)
    for line in lines:
        corner_points.append(pos)
        direction, n, _ = line.split(" ")
        n = int(n)
        total_border_points += n

        pos = tuple(
            sum(x) for x in zip(pos, tuple(n * y for y in DIRECTIONS[direction]))
        )

    return calculate_total_trench(corner_points, total_border_points)


def part2(lines) -> int:
    corner_points = []
    total_border_points = 0
    pos = (0, 0)

    for line in lines:
        corner_points.append(pos)
        _, _, color = line.split(" ")
        color = color.strip("()")
        n = int(color[1:-1], 16)
        direction = int(color[-1], 16)
        total_border_points += n

        pos = tuple(
            sum(x) for x in zip(pos, tuple(n * y for y in DIRECTIONS2[direction]))
        )

    return calculate_total_trench(corner_points, total_border_points)


def main():
    input_txt = utils.get_input(18).strip()
    lines = input_txt.split("\n")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
