#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/8
"""


def part1(grid, max_x, max_y) -> int:
    total_visible = 0
    for x, y in grid:
        if x in (0, max_x) or y in (0, max_y):
            total_visible += 1
            continue

        else:
            height = grid[x, y]
            neighbors_left = set([grid[xn, y] for xn in range(0, x)])
            neighbors_right = set([grid[xn, y] for xn in range(x + 1, max_x + 1)])
            neighbors_down = set([grid[x, yn] for yn in range(0, y)])
            neighbors_up = set([grid[x, yn] for yn in range(y + 1, max_y + 1)])

            if height > max(neighbors_right) or height > max(neighbors_left) or height > max(
                    neighbors_down) or height > max(neighbors_up):
                total_visible += 1
    return total_visible


def part2(grid, max_x, max_y) -> int:
    max_scenic_score = 0
    for x, y in grid:
        height = grid[x, y]

        neighbors_left = []
        for xn in reversed(range(0, x)):
            neighbors_left.append(grid[xn, y])
            if grid[xn, y] >= height:
                break

        neighbors_right = []
        for xn in range(x + 1, max_x + 1):
            neighbors_right.append(grid[xn, y])
            if grid[xn, y] >= height:
                break

        neighbors_up = []
        for yn in reversed(range(0, y)):
            neighbors_up.append(grid[x, yn])
            if grid[x, yn] >= height:
                break

        neighbors_down = []
        for yn in range(y + 1, max_y + 1):
            neighbors_down.append(grid[x, yn])
            if grid[x, yn] >= height:
                break

        scenic_score = len(neighbors_left) * len(neighbors_right) * len(neighbors_up) * len(neighbors_down)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

    return max_scenic_score


def main():
    input_txt = utils.get_input(8).strip()

    grid = {}
    max_x, max_y = 0, 0

    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, value in enumerate(line):
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            grid[x, y] = int(value)

    print(f"Part1: {part1(grid, max_x, max_y)}")
    print(f"Part2: {part2(grid, max_x, max_y)}")


if __name__ == "__main__":
    main()
