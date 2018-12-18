#!/usr/bin/env python

import re
from copy import deepcopy

from utils import utils

ITERATIONS = 1000000000


def print_map(M):
    print()
    print('*' * 30)
    for y in range(len(M[0])):
        for x in range(len(M)):
            c = M[x][y]
            print(c, end='')
        print('\n')


def get_adjacent(M, x, y):
    adjacent_types = []
    adjacent = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1),
                (-1, 1)]
    for dx, dy in adjacent:
        new_x = x + dx
        new_y = y + dy
        if new_x >= 0 and new_x < len(M) and new_y >= 0 and new_y < len(M[0]):
            adjacent_types.append(M[new_x][new_y])
    return adjacent_types


def take_snapshot(M):
    entry = '\n'.join(''.join(column) for column in M)
    return entry


def main():
    lines = utils.get_input(18).split('\n')

    map_size_y = len(lines)
    map_size_x = len(lines[0])
    M = [["" for y in range(map_size_y)] for x in range(map_size_x)]
    cache = []

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            M[x][y] = c

    for i in range(1000000000):
        M_new = deepcopy(M)
        for x in range(len(M)):
            for y in range(len(M[0])):
                c = M[x][y]
                adjacent_types = get_adjacent(M, x, y)
                if c == '.' and len([a for a in adjacent_types if a == '|'
                                     ]) >= 3:
                    M_new[x][y] = '|'
                if c == '|' and len([a for a in adjacent_types if a == '#'
                                     ]) >= 3:
                    M_new[x][y] = '#'
                if c == '#' and ('#' not in adjacent_types
                                 or '|' not in adjacent_types):
                    M_new[x][y] = '.'
        M = M_new

        if i == 9:
            number_wooded = len(
                [a for column in M for a in column if a == '|'])
            number_lumberyards = len(
                [a for column in M for a in column if a == '#'])
            print(f'Part 1: {number_wooded * number_lumberyards}')

        key = take_snapshot(M)

        if key in cache:
            cache_hit_idx = cache.index(key)
            loop_size = i - cache_hit_idx
            loop_step = (ITERATIONS - (cache_hit_idx + 1)) % loop_size
            loop_step_idx = cache_hit_idx + loop_step
            cache_entry = cache[loop_step_idx]
            number_wooded = len(re.findall('[|]', cache_entry))
            number_lumberyards = len(re.findall('[#]', cache_entry))
            print(f'Part 2: {number_wooded * number_lumberyards}')
            return
        cache.append(key)


if __name__ == "__main__":
    main()
