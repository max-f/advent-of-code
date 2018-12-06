#!/usr/bin/env python

from utils import utils
from sys import maxsize


def create_grid(min_x, max_x, min_y, max_y, locations):
    grid = dict()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if (x, y) in locations:
                grid[(x, y)] = locations[(x, y)]
            else:
                grid[(x, y)] = find_nearest_location(x, y, locations)
    return grid


def find_nearest_location(x, y, locations):
    nearest = -1
    min_distance = maxsize
    for k, v in locations.items():
        distance = calc_distance(x, y, k[0], k[1])
        if distance < min_distance:
            min_distance = distance
            nearest = v
        elif distance == min_distance:
            min_distance = distance
            nearest = -1
    return nearest


def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part_two(max_x, max_y, locations):
    points = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            total_d = 0
            for k, _ in locations.items():
                total_d += calc_distance(x, y, k[0], k[1])
            if total_d < 10000:
                points += 1
    return points


def main():
    data = utils.get_input(6).split("\n")[:-1]

    locations = dict()
    max_x = 0
    max_y = 0
    for i, d in enumerate(data):
        x, y = d.split(", ")
        x = int(x)
        if x > max_x:
            max_x = x
        y = int(y)
        if y > max_y:
            max_y = y
        locations[(int(x), int(y))] = i
    print("WuuT: ", max_x, max_y)
    grid_one = create_grid(-400, 800, -400, 800, locations)
    grid_two = create_grid(-450, 850, -450, 850, locations)
    counts_one = [0] * len(locations)
    counts_two = [0] * len(locations)
    for k, v in grid_one.items():
        if v == -1:
            continue
        counts_one[v] += 1
    for k, v in grid_two.items():
        if v == -1:
            continue
        counts_two[v] += 1
    didnt_change = set(counts_one).intersection(set(counts_two))
    print("#" * 10)
    print(didnt_change)
    print(f"Part 1: {max(didnt_change)}")
    print(f"Part 2: {part_two(max_x, max_y, locations)}")


if __name__ == "__main__":
    main()
