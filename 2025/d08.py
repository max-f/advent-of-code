#!/usr/bin/env python


import heapq
from math import sqrt, prod

from utils import utils

"""
Code for https://adventofcode.com/2025/day/8
"""


def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def main():
    input_txt = utils.get_input(8)
    lines = input_txt.strip().splitlines()

    coords = set(tuple(utils.ints(line)) for line in lines)

    all_distances = {}
    for p1 in coords:
        for p2 in coords:
            if p1 < p2:
                all_distances[(p1, p2)] = euclidean_distance(p1, p2)

    # part 1: n = 1000
    lowest_k = heapq.nsmallest(500000, all_distances.items(), key=lambda x: x[1])
    coord_to_comp = {}
    components = []

    for (p1, p2), dist in lowest_k:
        comp1 = coord_to_comp.get(p1)
        comp2 = coord_to_comp.get(p2)

        if comp1 and comp2 and comp1 is comp2:
            continue

        size1 = len(comp1) if comp1 else 1
        size2 = len(comp2) if comp2 else 1
        if size1 + size2 == len(coords):
            part2_result = p1[0] * p2[0]
            print(f"Part2: {part2_result}")

        if comp1 and comp2:
            for p in comp2:
                coord_to_comp[p] = comp1
            comp1.update(comp2)
            components.remove(comp2)
        elif comp1:
            comp1.add(p2)
            coord_to_comp[p2] = comp1
        elif comp2:
            comp2.add(p1)
            coord_to_comp[p1] = comp2
        else:
            new_comp = {p1, p2}
            components.append(new_comp)
            coord_to_comp[p1] = new_comp
            coord_to_comp[p2] = new_comp

    top_3_sizes = sorted([len(c) for c in components], reverse=True)[:3]
    result = prod(top_3_sizes)
    print(f"Part1: {result}")


if __name__ == "__main__":
    main()
