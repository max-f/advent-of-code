#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/15
"""


def manhattan_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def valid(x, y, sensors):
    for t, dist in sensors.items():
        current_dist = manhattan_dist(t, (x, y))
        if current_dist <= dist:
            return False
    return True


def part1(sensors, beacons):
    result = 0
    y = int(2e6)
    for x in range(-int(1e7), int(1e7)):
        if not valid(x, y, sensors) and (x, y) not in beacons:
            result += 1
    return result


def part2():
    pass


def main():
    input_txt = utils.get_input(15).strip()
    beacons = set()
    sensors = {}

    for line in input_txt.strip().split("\n"):
        s1, s2, b1, b2 = utils.ints(line)
        beacons.add((b1, b2))
        dist = manhattan_dist((s1, s2), (b1, b2))
        sensors[s1, s2] = dist

    print(f"Part 1: {part1(sensors, beacons)}")


if __name__ == "__main__":
    main()
