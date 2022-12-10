#!/usr/bin/env python

from utils import utils
from pprint import pprint

"""
Code for https://adventofcode.com/2022/day/9
"""

adjacent = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (0, 0),
]

moves = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def part1(input_txt: str) -> int:
    total_visited = set()
    t, h = ((0, 0), (0, 0))
    total_visited.add(t)

    for line in input_txt.strip().split("\n"):
        direction, count = line.split()
        for _ in range(int(count)):
            h_old = h
            h = utils.tuple_add(h, moves[direction])
            neighboring = set([utils.tuple_add(h, a) for a in adjacent])
            if t not in neighboring:
                t = h_old
                total_visited.add(t)

    return len(total_visited)


def part3(input_txt: str) -> int:
    total_visited = set()
    total_visited.add((0, 0))
    knots = [[0, 0] for _ in range(10)]

    def update_knot(i: int) -> None:
        hx, hy = knots[i - 1]
        tx, ty = knots[i]
        dx = tx - hx
        dy = ty - hy
        if dx == 0 or dy == 0:
            if abs(dx) >= 2:
                knots[i][0] += 1 if dx < 0 else -1
            if abs(dy) >= 2:
                knots[i][1] += 1 if dy < 0 else -1
        elif (abs(dx), abs(dy)) != (1, 1):
            knots[i][0] += 1 if dx < 0 else -1
            knots[i][1] += 1 if dy < 0 else -1

    for line in input_txt.strip().split("\n"):
        direction, count = line.split()
        for _ in range(int(count)):
            dx, dy = moves[direction]
            knots[0][0] += dx
            knots[0][1] += dy
            for i in range(1, 10):
                update_knot(i)
            total_visited.add(tuple(knots[-1]))

    return total_visited


def main():
    input_txt = utils.get_input(9).strip()

    print(f"Part1: {part1(input_txt)}")
    print(f"Part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
