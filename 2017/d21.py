#!/usr/bin/env python

from utils import utils
import numpy as np

#
# Cheated by looking at Scioshy's great solution :<
#

def substitute(pattern: np.ndarray, rules: dict, times: int) -> None:
    size = pattern[0].size
    for _ in range(times):
        if size % 2 == 0:
            new_size = to_3(size)
            new_pattern = np.empty((new_size, new_size), dtype=bool)
            for i in range(0, size, 2):
                for j in range(0, size, 2):
                    new_pattern[to_3(i):to_3(i) + 3, to_3(j):to_3(j) + 3] = rules[pattern[i:i+2, j:j+2].tobytes()]
        else:
            new_size = to_4(size)
            new_pattern = np.empty((new_size, new_size), dtype=bool)
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    new_pattern[to_4(i):to_4(i) + 4, to_4(j):to_4(j) + 4] = rules[pattern[i:i+3, j:j+3].tobytes()]
        size = new_size
        pattern = new_pattern
    print(np.count_nonzero(pattern))


def to_3(x: int) -> int:
    return (x // 2) * 3


def to_4(x: int) -> int:
    return (x // 3) * 4


def main():
    start = np.array([[False, True, False],
                      [False, False, True],
                      [True, True, True]])
    input_str = utils.get_input(21)
    rules = dict()
    for rule in input_str.strip().split('\n'):
        pattern, new_pattern = rule.strip().split(' => ')

        pattern = np.array([[c == '#' for c in row] for row in pattern.split('/')])
        new_pattern = np.array([[c == '#' for c in row] for row in new_pattern.split('/')])

        flipped = np.fliplr(pattern)
        rules[pattern.tobytes()] = new_pattern
        rules[flipped.tobytes()] = new_pattern

        for _ in range(3):
            pattern, flipped = np.rot90(pattern), np.rot90(flipped)
            rules[pattern.tobytes()] = new_pattern
            rules[flipped.tobytes()] = new_pattern

    substitute(start, rules, 5)
    substitute(start, rules, 18)


if __name__ == '__main__':
    main()
