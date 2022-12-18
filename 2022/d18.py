#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/18
"""


def part1(cubes) -> int:
    sides = 0
    for cube in cubes:
        n = possible_neighbors(cube)
        sides += 6 - len(n.intersection(cubes))
    return sides


def part2(cubes) -> int:
    min_x = min(cubes, key=lambda c: c[0])
    max_x = max(cubes, key=lambda c: c[0])
    min_y = min(cubes, key=lambda c: c[1])
    max_y = max(cubes, key=lambda c: c[1])
    min_z = min(cubes, key=lambda c: c[2])
    max_z = max(cubes, key=lambda c: c[2])
    x_range = range(min_x[0], max_x[0] + 1)
    y_range = range(min_y[1], max_y[1] + 1)
    z_range = range(min_z[2], max_z[2] + 1)

    known_outside = set()

    def outside(t) -> bool:
        if t in cubes:
            return False

        visited = set()
        stack = [t]

        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            if cur in known_outside:
                known_outside.update(visited - cubes)
                return True
            elif (
                cur[0] not in x_range or cur[1] not in y_range or cur[2] not in z_range
            ):
                known_outside.update(visited - cubes)
                return True
            if cur not in cubes:
                stack += possible_neighbors(cur)
        return False

    result = 0
    for cube in cubes:
        for n in possible_neighbors(cube):
            if outside(n):
                result += 1
    return result


def possible_neighbors(t):
    neighbors = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    return set([utils.tuple_add(t, n) for n in neighbors])


def main():
    input_txt = utils.get_input(18).strip()
    cubes = set()
    for line in input_txt.split("\n"):
        cube = tuple(utils.ints(line))
        cubes.add(cube)

    print(f"Part 1: {part1(cubes)}")
    print(f"Part 2: {part2(cubes)}")


if __name__ == "__main__":
    main()
