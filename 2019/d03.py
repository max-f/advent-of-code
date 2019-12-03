#!/usr/bin/env python

import numpy as np
from utils import utils

ORIGIN = np.array((0, 0))


def manhattan_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def build_wire(line):
    directions = {
        'R': np.array((1, 0)),
        'U': np.array((0, 1)),
        'L': np.array((-1, 0)),
        'D': np.array((0, -1))
    }

    wire = {}
    current = np.array(ORIGIN)
    step = 0
    for part in line.split(','):
        direction = part[0]
        x = int(part[1:])
        for _ in range(x):
            current += directions[direction]
            step += 1
            wire[tuple(current)] = step
    return wire


def find_intersections(wire1, wire2):
    unique_points_w1 = set(wire1.keys())
    unique_points_w2 = set(wire2.keys())
    intersections = unique_points_w1 & unique_points_w2
    return sorted(intersections, key=lambda p: manhattan_dist(p, ORIGIN))


def calculate(input_txt: str) -> (int, int):
    input_txt = input_txt.strip()
    line1, line2 = input_txt.split('\n')
    wire1 = build_wire(line1)
    wire2 = build_wire(line2)
    intersections = find_intersections(wire1, wire2)
    lowest_dist_p = intersections[0]
    distance = manhattan_dist(lowest_dist_p, ORIGIN)
    min_signal_delay = min([wire1[p] + wire2[p] for p in intersections])

    return distance, min_signal_delay


def main():
    input_txt = utils.get_input(3)
    p1, p2 = calculate(input_txt)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
