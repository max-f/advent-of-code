#!/usr/bin/env python

from collections import deque

from utils import utils

"""
Code for https://adventofcode.com/2023/day/16
"""

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def get_new_directions(grid, pos, direction) -> list[tuple[int, int]]:
    if grid[pos] == "/":
        return [(-direction[1], -direction[0])]
    elif grid[pos] == "\\":
        return [(direction[1], direction[0])]
    elif grid[pos] == "-" and direction[0]:
        return [WEST, EAST]
    elif grid[pos] == "|" and direction[1]:
        return [NORTH, SOUTH]
    else:
        return [direction]


def beam_walk(grid, start, direction) -> int:
    queue = deque([(start, direction)])
    visited = set()

    while queue:
        pos, direction = queue.popleft()
        if (pos, direction) in visited or pos not in grid:
            continue
        visited.add((pos, direction))
        new_directions = get_new_directions(grid, pos, direction)
        for new_direction in new_directions:
            queue.append((utils.tuple_add(pos, new_direction), new_direction))
    return len(set(pos for pos, _ in visited))


def part1(grid) -> int:
    return beam_walk(grid, (0, 0), EAST)


def part2(grid) -> int:
    n = max(i for i, _ in grid)
    m = max(j for _, j in grid)

    result = 0
    for i in range(n):
        result = max(result, beam_walk(grid, (i, m - 1), WEST))
        result = max(result, beam_walk(grid, (i, 0), EAST))
    for j in range(m):
        result = max(result, beam_walk(grid, (0, j), SOUTH))
        result = max(result, beam_walk(grid, (n - 1, j), NORTH))
    return result


def main():
    input_txt = utils.get_input(16).strip()
    grid = {}
    for i, line in enumerate(input_txt.split("\n")):
        for j, c in enumerate(line):
            grid[i, j] = c

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
