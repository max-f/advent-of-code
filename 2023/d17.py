#!/usr/bin/env python

import heapq

from utils import utils

"""
Code for https://adventofcode.com/2023/day/17
"""

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def directions_to_explore(prev_direction):
    for dx, dy in DIRECTIONS:
        if (dx, dy) != prev_direction and (dx, dy) != (-prev_direction[0], -prev_direction[1]):
            yield dx, dy


def get_min_heat_path(grid, start, end, min_same, max_same):
    queue = [(0, *start, 0, 0)]
    visited = set()

    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, px, py) in visited:
            continue
        visited.add((x, y, px, py))

        for dx, dy in directions_to_explore((px, py)):
            cx, cy, current_heat = x, y, heat
            for same_steps in range(1, max_same + 1):
                cx += dx
                cy += dy
                if (cx, cy) in grid:
                    current_heat += grid[cx, cy]
                    if same_steps >= min_same:
                        heapq.heappush(queue, (current_heat, cx, cy, dx, dy))


def part1(grid) -> int:
    return get_min_heat_path(grid, (0, 0), max(grid), 1, 3)


def part2(grid) -> int:
    return get_min_heat_path(grid, (0, 0), max(grid), 4, 10)


def main():
    input_txt = utils.get_input(17).strip()
    grid = {}
    for i, line in enumerate(input_txt.split("\n")):
        for j, c in enumerate(line):
            grid[i, j] = int(c)

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
