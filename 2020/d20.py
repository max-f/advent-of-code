#!/usr/bin/env python

import math

from utils import utils

"""
Code for https://adventofcode.com/2020/day/20
"""


def part1(edges: dict[int, list[str]]) -> int:
    """
    Idea: compare edges of every grid with all other edges: if number of matches is only 2 -> corner grid.
    Due to commutativity of multiplication ("multiply edge IDs") it does not matter which corner grid is where
    At least for part 1...
    """
    corner_ids = set()

    for id_, all_edges in edges.items():
        all_other_edges = set(e for k, v in edges.items() if k is not id_ for e in v)
        matching_edges = calc_matches(all_edges, all_other_edges)
        if matching_edges == 2:
            corner_ids.add(id_)

    return math.prod(corner_ids)


def calc_matches(edges: list[str], all_other_edges: set[str]) -> int:
    return sum([1 for e in edges if e in all_other_edges or e[::-1] in all_other_edges])


def main():
    input_txt = utils.get_input(20).rstrip()
    single_tiles = input_txt.split("\n\n")

    edges = {}
    for tile in single_tiles:
        id_, grid = tile.split(':\n')
        id_ = int(id_.split()[-1])
        print(grid)

        lines = grid.split('\n')
        # clockwise edges
        up_edge = lines[0]
        ri_edge = ''.join(line[-1] for line in lines)
        do_edge = lines[-1][::-1]
        le_edge = ''.join(line[0] for line in lines)[::-1]
        t_edges = [up_edge, ri_edge, do_edge, le_edge]
        edges[id_] = t_edges

    print(part1(edges))


if __name__ == "__main__":
    main()
