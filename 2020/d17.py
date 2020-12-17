#!/usr/bin/env python

import itertools

from utils import utils

"""
Code for https://adventofcode.com/2020/day/17
"""


def calc(active_cubes, neighborhood_func) -> int:
    for _ in range(6):
        complete_neighborhood = set()
        for active_cube in active_cubes:
            complete_neighborhood |= neighborhood_func(active_cube)

        new_active = set()
        for t in complete_neighborhood:
            neighbors = neighborhood_func(t)
            neighbors.remove(t)
            if t in active_cubes:
                if 2 <= len(active_cubes & neighbors) <= 3:
                    new_active.add(t)
            else:
                if len(active_cubes & neighbors) == 3:
                    new_active.add(t)
        active_cubes = new_active
    return len(active_cubes)


def get_neighborhood_3d(cube: tuple[int, int, int]):
    x_neighbors = (cube[0] - 1, cube[0], cube[0] + 1)
    y_neighbors = (cube[1] - 1, cube[1], cube[1] + 1)
    z_neighbors = (cube[2] - 1, cube[2], cube[2] + 1)
    return set(itertools.product(x_neighbors, y_neighbors, z_neighbors))


def get_neighborhood_4d(cube: tuple[int, int, int, int]):
    x_neighbors = (cube[0] - 1, cube[0], cube[0] + 1)
    y_neighbors = (cube[1] - 1, cube[1], cube[1] + 1)
    z_neighbors = (cube[2] - 1, cube[2], cube[2] + 1)
    w_neighbors = (cube[3] - 1, cube[3], cube[3] + 1)
    return set(itertools.product(x_neighbors, y_neighbors, z_neighbors, w_neighbors))


def main():
    input_txt = utils.get_input(17).rstrip()
    active = set()
    for y, line in enumerate(input_txt.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0))
    part2_active = {t + (0,) for t in active}
    print(calc(active, get_neighborhood_3d))
    print(calc(part2_active, get_neighborhood_4d))


if __name__ == "__main__":
    main()
