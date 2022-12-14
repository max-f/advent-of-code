#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/14
"""

movement = [(0, 1), (-1, 1), (1, 1)]


def move(current, blocked, resting):
    for m in movement:
        new = utils.tuple_add(current, m)
        if new not in blocked and new not in resting:
            return new
    return current


def part1(sand_start, blocked):
    resting = set()
    max_y = max(blocked, key=lambda x: x[1])[1]

    touched_ground = False
    while not touched_ground:
        current = sand_start
        while True:
            new = move(current, blocked, resting)
            if new[1] >= max_y:
                touched_ground = True
                break
            elif new == current:
                resting.add(current)
                break
            else:
                current = new
    return len(resting)


def part2(sand_start, blocked):
    resting = set()
    max_y = max(blocked, key=lambda x: x[1])[1] + 2
    for x in range(500 - max_y - 1, 500 + max_y + 1):
        blocked.add((x, max_y))

    not_start = True
    while not_start:
        current = sand_start
        while True:
            new = move(current, blocked, resting)
            if new == sand_start:
                not_start = False
                resting.add(sand_start)
                break
            elif new == current:
                resting.add(current)
                break
            else:
                current = new
    return len(resting)


def main():
    input_txt = utils.get_input(14).strip()
    sand_start = (500, 0)
    blocked = set()

    for line in input_txt.strip().split("\n"):
        coords = line.split(" -> ")
        for i in range(len(coords) - 1):
            x1, y1 = map(int, coords[i].split(","))
            x2, y2 = map(int, coords[i + 1].split(","))
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    blocked.add((x1, y))
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    blocked.add((x, y1))

    print(f"Part 1: {part1(sand_start, blocked)}")
    print(f"Part 2: {part2(sand_start, blocked)}")


if __name__ == "__main__":
    main()
