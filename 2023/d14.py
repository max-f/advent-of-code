#!/usr/bin/env python

from utils import utils

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

    result = calc_result(grid)
    return result


def stringify(grid):
    return "\n".join("".join(row) for row in grid)


def do_one_cycle(grid):
    grid = slide_north(grid)

    # west
    grid = [row[::-1] for row in transpose(grid)]
    grid = slide_north(grid)

    # south
    grid = [row[::-1] for row in transpose(grid)]
    grid = slide_north(grid)

    # east
    grid = [row[::-1] for row in transpose(grid)]
    grid = slide_north(grid)

    grid = [row[::-1] for row in transpose(grid)]
    return grid


def calc_result(grid):
    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "O":
                result += len(grid) - y
    return result


def part2(grid: list[list[str]]) -> int:
    seen_configs = {}

    for idx in range(int(1e9)):
        config = stringify(grid)
        if config not in seen_configs:
            seen_configs[config] = idx
        else:
            cycle_length = idx - seen_configs[config]
            remaining = (int(1e9) - idx) % cycle_length

            for _ in range(remaining):
                grid = do_one_cycle(grid)
            break

        grid = do_one_cycle(grid)

    result = calc_result(grid)
    return result


def main():
    input_txt = utils.get_input(14)
    grid = [list(row) for row in input_txt.strip().split("\n")]
    grid2 = [list(row) for row in input_txt.strip().split("\n")]

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid2)}")


if __name__ == "__main__":
    main()
