#!/usr/bin/env python
import networkx as nx

from utils import utils

DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def calc_perimeter(connected_component: set[tuple[int, int]]) -> int:
    perimeter = 0
    for pos in connected_component:
        for direction in DIRS:
            neighbor = utils.tuple_add(pos, direction)
            if neighbor not in connected_component:
                perimeter += 1
    return perimeter


def calc_sides(connected_component: set[tuple[int, int]]) -> int:
    seen = set()

    sides = 0
    for (y, x) in connected_component:
        for (dy, dx) in DIRS:
            if (y + dy, x + dx) in connected_component:
                continue

            # Find canonical starting point and trace edge
            cy, cx = y, x
            while (cy + dx, cx + dy) in connected_component and (cy + dy, cx + dx) not in connected_component:
                cy += dx
                cx += dy
            if (cy, cx, dy, dx) not in seen:
                seen.add((cy, cx, dy, dx))
                sides += 1
    return sides


def find_connected_components(grid: dict[tuple[int, int], str]) -> list[set[tuple[int, int]]]:
    G = nx.Graph()

    for t in grid.keys():
        cur = grid[t]
        for pos in DIRS:
            added_neighbor = False
            neighbor = utils.tuple_add(t, pos)
            if neighbor in grid.keys():
                if cur == grid[neighbor]:
                    G.add_edge(t, neighbor)
                    added_neighbor = True

            if not added_neighbor:
                G.add_node(t)

    connected_components = nx.connected_components(G)
    return list(connected_components)


def part1(connected_components: list[set[tuple[int, int]]]) -> int:
    return sum([(calc_perimeter(cc) * len(cc)) for cc in connected_components])


def part2(connected_components: list[set[tuple[int, int]]]) -> int:
    return sum([calc_sides(cc) * len(cc) for cc in connected_components])


def main() -> None:
    input_txt = utils.get_input(12)

    grid = {}
    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, c in enumerate(line):
            grid[y, x] = c

    connected_components = find_connected_components(grid)
    print(f"Part1: {part1(connected_components)}")
    print(f"Part2: {part2(connected_components)}")


if __name__ == "__main__":
    main()
