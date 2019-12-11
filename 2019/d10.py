#!/usr/bin/env python

from utils import utils
from typing import Tuple, Set
from pprint import pprint
from math import isclose, sqrt
from collections import defaultdict


# StackOverflow :F
def distance(a: Tuple[int, int], b: Tuple[int, int]):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def is_between(a, c, b):
    return isclose(distance(a, c) + distance(c, b), distance(a, b))


def part1(asteroids: Set) -> Tuple[Tuple[int, int], int]:
    detected = defaultdict(int)
    for t1 in asteroids:
        for t2 in asteroids:
            if t1 == t2:
                continue
            if not any(is_between(t1, x, t2) for x in asteroids - {t1, t2}):
                detected[t1] += 1
    return max(detected.keys()), max(detected.values())


def part2(asteroids, best) -> None:
    destroyed = set()
    detected = calculate_detected_asteroids(asteroids, best)

    pass


def calculate_detected_asteroids(asteroids, best) -> Set:
    detected = set()
    for other in asteroids:
        if other == best:
            continue
        if not any(is_between(best, x, other) for x in asteroids - {best, other}):
            detected.add(other)
    return detected


def main():
    grid_lines = utils.get_input(10).strip().split('\n')
    asteroids = set()
    for y, s in enumerate(grid_lines):
        for x, c in enumerate(s):
            if c == '#':
                asteroids.add((x, y))

    best_asteroid, detected = part1(asteroids)
    print(f"Part 1: {detected}")
    print(best_asteroid)

    # print("Part 2")
    # part2(input_txt)


if __name__ == "__main__":
    main()
