#!/usr/bin/env python

import networkx as nx

from utils import utils

DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

type Grid = dict[tuple[int, int], int]


def part1(grid: Grid) -> int:
    G = nx.DiGraph()

    for t in grid.keys():
        cur = grid[t]
        for pos in DIRS:
            neighbor = utils.tuple_add(t, pos)
            if neighbor in grid.keys():
                height_step = grid[neighbor] - cur
                if height_step == 1:
                    G.add_edge(t, neighbor)

    trailheads = [(y, x) for (y, x) in grid.keys() if grid[y, x] == 0]
    endpoints = set([(y, x) for (y, x) in grid.keys() if grid[y, x] == 9])

    total_score = 0
    for start in trailheads:
        descendants = nx.descendants(G, start)
        reachable = endpoints & descendants
        total_score += len(reachable)

    return total_score


def part2(grid: Grid) -> int:
    G = nx.DiGraph()

    for t in grid.keys():
        cur = grid[t]
        for pos in DIRS:
            neighbor = utils.tuple_add(t, pos)
            if neighbor in grid.keys():
                height_step = grid[neighbor] - cur
                if height_step == 1:
                    G.add_edge(t, neighbor)

    trailheads = [(y, x) for (y, x) in grid.keys() if grid[y, x] == 0]
    endpoints = [(y, x) for (y, x) in grid.keys() if grid[y, x] == 9]

    total = 0
    for start in trailheads:
        trailhead_paths = 0
        for end in endpoints:
            paths = list(nx.all_simple_paths(G, start, end))
            trailhead_paths += len(paths)
        total += trailhead_paths

    return total


def main() -> None:
    input_txt = utils.get_input(10)

    grid = {}
    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, c in enumerate(line):
            if c.isdigit():
                grid[y, x] = int(c)

    print(f"Part1: {part1(grid)}")
    print(f"Part2: {part2(grid)}")


if __name__ == "__main__":
    main()
