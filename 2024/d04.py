#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2024/day/4
"""

WORD = "XMAS"
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def check_direction(
    grid: dict[tuple[int, int], str],
    start_pos: tuple[int, int],
    direction: tuple[int, int],
    word: str,
) -> bool:
    y, x = start_pos
    dy, dx = direction

    for char in word:
        if (y, x) not in grid or grid[(y, x)] != char:
            return False
        y += dy
        x += dx
    return True


def check_xmas(grid: dict[tuple[int, int], str], start_pos: tuple[int, int]) -> bool:
    y, x = start_pos

    if grid[start_pos] == "A":
        d1_mas = grid[y - 1, x - 1] == "M" and grid[y + 1, x + 1] == "S"
        d1_sam = grid[y - 1, x - 1] == "S" and grid[y + 1, x + 1] == "M"

        d2_mas = grid[y - 1, x + 1] == "M" and grid[y + 1, x - 1] == "S"
        d2_sam = grid[y - 1, x + 1] == "S" and grid[y + 1, x - 1] == "M"

        return (d1_mas or d1_sam) and (d2_mas or d2_sam)
    return False


def part1(grid: dict[tuple[int, int], str]) -> int:
    max_y = max(y for y, _ in grid.keys())
    max_x = max(x for _, x in grid.keys())

    count = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            for direction in DIRECTIONS:
                if check_direction(grid, (y, x), direction, WORD):
                    count += 1
    return count


def part2(grid: dict[tuple[int, int], str]) -> int:
    max_y = max(y for y, _ in grid.keys())
    max_x = max(x for _, x in grid.keys())

    count = 0
    for y in range(1, max_y):
        for x in range(1, max_x):
            if check_xmas(grid, (y, x)):
                count += 1
    return count


def main():
    input_txt = utils.get_input(4)
    grid = {}
    for i, line in enumerate(input_txt.split("\n")):
        for j, c in enumerate(line):
            grid[i, j] = c

    print(f"Part1: {part1(grid)}")
    print(f"Part2: {part2(grid)}")


if __name__ == "__main__":
    main()
