#!/usr/bin/env python

from utils import utils
from pprint import pprint

"""
Code for https://adventofcode.com/2023/day/14
"""


def transpose(grid):
    return [list(x) for x in zip(*grid)]


def slide_north(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                new_y = y
                for y1 in range(y - 1, -1, -1):
                    if grid[y1][x] == "#" or grid[y1][x] == "O":
                        break
                    new_y = y1
                if new_y != y:
                    grid[new_y][x] = "O"
                    grid[y][x] = "."
    return grid



def part1(grid: list[list[str]]) -> int:
    grid = slide_north(grid)
    pprint(grid)

    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                result += len(grid) - y

    return result


def part2(grid: list[list[str]]) -> int:
    for _ in range(1):
        grid = slide_north(grid)

        # west
        grid = transpose(grid)
        grid = slide_north(grid)

        # south
        grid = transpose(grid)
        grid = slide_north(grid)

        # east
        grid = transpose(grid)
        grid = slide_north(grid)

        grid = transpose(grid)

    pprint(grid)
    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                result += len(grid) - y

    pprint(grid)
    return result




def main():
    input_txt = utils.get_input(77)
    grid = [list(row) for row in input_txt.strip().split("\n")]
    grid2 = [list(row) for row in input_txt.strip().split("\n")]

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid2)}")


if __name__ == "__main__":
    main()
