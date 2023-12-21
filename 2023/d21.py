#!/usr/bin/env python

from utils import utils
from collections import deque

"""
Code for https://adventofcode.com/2023/day/21
"""

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}


def find_start(lines):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                return i, j


def part1(lines) -> int:
    visited = set()
    reached = set()
    n, m = len(lines), len(lines[0])

    starting_point = find_start(lines)

    queue = deque([(starting_point, 0)])
    total_steps = 64
    while queue:
        pos, steps = queue.popleft()

        if (pos, steps) in visited:
            continue
        visited.add((pos, steps))

        if steps == total_steps:
            reached.add(pos)
            continue
        for direction in DIRECTIONS:
            new_pos = tuple(
                sum(x) for x in zip(pos, tuple(y for y in DIRECTIONS[direction]))
            )
            if (new_pos, steps + 1) in visited:
                continue
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= m:
                continue
            if lines[new_pos[0]][new_pos[1]] == "#":
                continue
            queue.append((new_pos, steps + 1))
    return len(reached)


def main():
    input_txt = utils.get_input(21).strip()
    lines = input_txt.split("\n")

    print(f"Part 1: {part1(lines)}")
    # print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
