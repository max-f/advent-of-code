#!/usr/bin/env python

from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2023/day/3
"""

ADJACENT_OFFSETS = {
    (0, 1),
    (1, 0),
    (1, 1),
    (-1, 0),
    (0, -1),
    (-1, -1),
    (1, -1),
    (-1, 1),
}


class Number:
    def __init__(self, value: str):
        self.value = value
        self.positions: list[tuple[int, int]] = []
        self.adjacent_pos: tuple[int, int] = ()

    def __repr__(self) -> str:
        return f"{self.value} at {self.positions}"


def is_adjacent(grid: dict, number: Number) -> bool:
    return any(
        utils.tuple_add(pos, adj) in grid
        and grid[utils.tuple_add(pos, adj)].strip(".").isalnum()
        for pos in number.positions
        for adj in ADJACENT_OFFSETS
    )


def get_numbers_in_line(grid: dict, grid_size: int, y: int) -> list[Number]:
    numbers = []
    x = 0
    while x < grid_size:
        if grid[x, y].isdigit():
            number = Number(grid[x, y])
            number.positions.append((x, y))
            x += 1
            while x < grid_size and grid[x, y].isdigit():
                number.value += grid[x, y]
                number.positions.append((x, y))
                x += 1
            numbers.append(number)
        else:
            x += 1
    return numbers


def part1(grid: dict, grid_size: int) -> int:
    adjacent_numbers = [
        n
        for y in range(grid_size)
        for n in get_numbers_in_line(grid, grid_size, y)
        if is_adjacent(grid, n)
    ]
    return sum(int(n.value) for n in adjacent_numbers)


def is_star_adjacent(grid: dict, number: Number) -> tuple[int, int] | None:
    for pos in number.positions:
        for adj in ADJACENT_OFFSETS:
            evaluate = utils.tuple_add(pos, adj)
            if evaluate in grid and grid[evaluate] == "*":
                return evaluate
    return None


def part2(grid: dict, grid_size: int) -> int:
    pairings = defaultdict(list)

    for y in range(grid_size):
        for n in get_numbers_in_line(grid, grid_size, y):
            star_adjacent = is_star_adjacent(grid, n)
            if star_adjacent:
                n.adjacent_pos = star_adjacent
                pairings[star_adjacent].append(n)

    return sum(
        int(v[0].value) * int(v[1].value) for v in pairings.values() if len(v) == 2
    )


def main():
    input_txt = utils.get_input(3)
    grid = defaultdict(str)
    grid_size = 0

    for y, line in enumerate(input_txt.strip().split("\n")):
        grid_size = grid_size or len(line)
        for x, c in enumerate(line):
            if c.strip():
                grid[x, y] = c

    print(f"Part1: {part1(grid, grid_size)}")
    print(f"Part2: {part2(grid, grid_size)}")


if __name__ == "__main__":
    main()
