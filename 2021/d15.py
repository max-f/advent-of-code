#!/usr/bin/env python

from copy import deepcopy

import networkx as nx
from utils import utils

"""
Code for https://adventofcode.com/2021/day/15
"""


def neighbors(
    grid: dict[tuple[int, int], int],
    coord: tuple[int, int],
):
    x, y = coord

    for xd, yd in (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ):
        c = x + xd, y + yd
        if c in grid:
            yield c


def part1(grid: dict[tuple[int, int], int]) -> int:
    G = nx.DiGraph()
    for pair in grid:
        for n in neighbors(grid, pair):
            G.add_edge(pair, n, weight=grid[n])

    start = (0, 0)
    end = max(grid)
    shortest_path = nx.dijkstra_path(G, start, end)
    total = 0
    for node in shortest_path[1:]:
        total += grid[node]
    return total


def part2(grid: dict[tuple[int, int], int]) -> int:
    max_x, max_y = (value + 1 for value in max(grid))

    for x in range(max_x * 5):
        for y in range(max_y * 5):
            if (x, y) in grid:
                continue
            cost = (
                grid[x % max_x, y % max_y] - 1 + (x // max_x) + (y // max_y)
            ) % 9 + 1
            grid[x, y] = cost

    G = nx.DiGraph()
    for pair in grid:
        for n in neighbors(grid, pair):
            G.add_edge(pair, n, weight=grid[n])

    start = (0, 0)
    end = max(grid)
    shortest_path = nx.dijkstra_path(G, start, end)
    total = 0
    for node in shortest_path[1:]:
        total += grid[node]
    return total


def main():
    input_txt = utils.get_input(15)

    grid = {}
    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, value in enumerate(line):
            grid[x, y] = int(value)

    grid2 = deepcopy(grid)

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid2)}")


if __name__ == "__main__":
    main()
