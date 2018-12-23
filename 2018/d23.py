#!/usr/bin/env python

import re

from utils import utils


def parse(line):
    return list(map(int, re.findall(r'[0-9-]+', line)))


def manhattan_dist(bot1, bot2):
    x1, y1, z1 = bot1
    x2, y2, z2 = bot2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def main():
    lines = utils.get_input(23).split('\n')

    bots = dict()

    max_bot = None
    max_range = 0

    for line in lines:
        if line:
            x, y, z, r = parse(line)
            bots[(x, y, z)] = r
            if r > max_range:
                max_bot = (x, y, z)
                max_range = r

    max_in_range = 0
    for bot in bots.keys():
        d = manhattan_dist(bot, max_bot)
        if d <= max_range:
            max_in_range += 1

    print(f'Part 1: {max_in_range}')


if __name__ == "__main__":
    main()
