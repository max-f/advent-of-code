#!/usr/bin/env python

from utils import utils
from collections import defaultdict
import operator
import copy


def walk_one(infected: defaultdict) -> None:
    moves = {
        0:   (0, -1),
        90:  (1, 0),
        180: (0, 1),
        270: (-1, 0)
    }
    result = 0
    p = (0, 0)
    angle = 0

    for _ in range(10000):
        if infected[p]:
            angle = (angle + 90) % 360
            infected[p] = False
            p = add(p, moves[angle])
        else:
            angle = (angle - 90) % 360
            infected[p] = True
            result += 1
            p = add(p, moves[angle])
    print('Part 1: ', result)


def walk_two(infected: defaultdict) -> None:
    moves = {
        0:   (0, -1),
        90:  (1, 0),
        180: (0, 1),
        270: (-1, 0)
    }

    result = 0
    p = (0, 0)
    angle = 0

    for _ in range(10000000):
        if not infected[p]:
            angle = (angle - 90) % 360
            infected[p] = 'W'
            p = add(p, moves[angle])
        elif infected[p] == 'W':
            infected[p] = '#'
            result += 1
            p = add(p, moves[angle])
        elif infected[p] == '#':
            angle = (angle + 90) % 360
            infected[p] = 'F'
            p = add(p, moves[angle])
        elif infected[p] == 'F':
            angle = (angle + 180) % 360
            del infected[p]
            p = add(p, moves[angle])
    print('Part 2: ', result)


def add(a, b):
    return tuple(map(operator.add, a, b))


def main():
    input_str = utils.get_input(22)
    infected = defaultdict(bool)
    zx, zy = (12, 12)

    for i, line in enumerate(input_str.strip().split('\n')):
        for j, c in enumerate(line.strip()):
            if c == '#':
                infected[j - zx, i - zy] = c
    infected_one = copy.copy(infected)
    walk_one(infected_one)
    walk_two(infected)


if __name__ == '__main__':
    main()
