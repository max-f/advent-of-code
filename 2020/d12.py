#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/12
"""

DIRECTIONS = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}


def part1(lines: list[str]):
    rotations = "ESWN"
    dir_ = "E"
    pos = (0, 0)

    for line in lines:
        cmd = line[0]
        number = utils.ints(line)[0]
        if cmd == "F":
            pos = utils.tuple_add(pos, tuple(number * i for i in DIRECTIONS[dir_]))
        elif cmd in "LR":
            number = number // 90
            idx = rotations.index(dir_)
            m = 1 if cmd == "R" else -1
            idx += m * number
            dir_ = rotations[idx % 4]
        elif cmd in DIRECTIONS.keys():
            pos = utils.tuple_add(pos, tuple(number * i for i in DIRECTIONS[cmd]))

    return abs(pos[0]) + abs(pos[1])


def part2(lines: list[str]):
    rotations = {
        "L": {90: counterclockwise_90, 180: rotate, 270: clockwise_90},
        "R": {90: clockwise_90, 180: rotate, 270: counterclockwise_90},
    }

    pos = (0, 0)
    waypoint = (10, 1)

    for line in lines:
        cmd = line[0]
        number = utils.ints(line)[0]
        if cmd == "F":
            pos = utils.tuple_add(pos, tuple(number * i for i in waypoint))
        elif cmd in "LR":
            waypoint = rotations[cmd][number](waypoint)
        elif cmd in DIRECTIONS.keys():
            waypoint = utils.tuple_add(
                waypoint, tuple(number * i for i in DIRECTIONS[cmd])
            )

    return abs(pos[0]) + abs(pos[1])


def counterclockwise_90(pos):
    return -pos[1], pos[0]


def clockwise_90(pos):
    return pos[1], -pos[0]


def rotate(pos):
    return -pos[0], -pos[1]


def main():
    input_txt = utils.get_input(12).rstrip()
    lines = input_txt.split("\n")
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
