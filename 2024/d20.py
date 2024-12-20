#!/usr/bin/env python

import networkx as nx

from utils import utils

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def taxicab_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(grid, G, start, end, distance_cutoff) -> int:
    normal_path = nx.shortest_path_length(G, start, end, weight="weight")

    start_paths = nx.single_source_dijkstra_path_length(G, start, weight="weight")
    end_paths = nx.single_source_dijkstra_path_length(G, end, weight="weight")

    valid_cheats = set()

    possible_cheat_start_and_end_points = [v for v in grid.keys() if grid[v] in ".SE"]
    for p in possible_cheat_start_and_end_points:
        for q in possible_cheat_start_and_end_points:
            if p == q:
                continue
            taxicab = taxicab_distance(p, q)
            if taxicab > distance_cutoff:
                continue
            if p in start_paths and q in end_paths:
                if start_paths[p] + end_paths[q] + taxicab <= normal_path - 100:
                    valid_cheats.add(tuple(sorted([p, q])))

    return len(valid_cheats)


def part1(grid, G, start, end):
    return solve(grid, G, start, end, 2)


def part2(grid, G, start, end):
    return solve(grid, G, start, end, 20)


def create_graph(grid):
    G = nx.Graph()
    for pos in grid:
        if grid[pos] in ".SE":
            for d in DIRECTIONS:
                new_pos = utils.tuple_add(pos, d)
                if new_pos in grid and grid[new_pos] in ".SE":
                    G.add_edge(pos, new_pos, weight=1)
    return G


def main() -> None:
    input_txt = utils.get_input(20)
    lines = input_txt.strip().split("\n")

    start = end = None
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[y, x] = c
            if c == "S":
                start = (y, x)
            elif c == "E":
                end = (y, x)

    G = create_graph(grid)

    print(f"Part1: {part1(grid, G, start, end)}")
    print(f"Part2: {part2(grid, G, start, end)}")


if __name__ == "__main__":
    main()
