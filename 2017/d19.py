#!/usr/bin/env python

from utils import utils
import numpy as np


def run_package(lines: list, start: tuple) -> None:
    letters = []
    to_visit = ['G', 'S', 'X', 'D', 'I', 'P', 'W', 'T', 'U']
    steps = 0
    pos = np.array(start)
    up = np.array((0, -1))
    down = np.array((0, 1))
    left = np.array((-1, 0))
    right = np.array((1, 0))
    d = down
    while True:
        if np.array_equal(d, up):
            next_p = pos + up
        elif np.array_equal(d, down):
            next_p = pos + down
        elif np.array_equal(d, left):
            next_p = pos + left
        elif np.array_equal(d, right):
            next_p = pos + right
        print(letters)
        print()
        next_c = lines[next_p[1]][next_p[0]]
        if next_c == '+':
            if np.array_equal(d, down) or np.array_equal(d, up):
                if (next_p + left)[0] > 0 and lines[next_p[1]][(next_p+left)[0]] == '-':
                    d = left
                    pos = next_p + left
                    steps += 2
                    continue
                else:
                    d = right
                    pos = next_p + right
                    steps += 2
                    continue
            if np.array_equal(d, left) or np.array_equal(d, right):
                if (next_p + up)[1] > 0 and lines[(next_p+up)[1]][next_p[0]] == '|':
                    d = up
                    pos = next_p + up
                    steps += 2
                    continue
                else:
                    d = down
                    pos = next_p + down
                    steps += 2
                    continue

        elif next_c.isalpha():
            letters.append(next_c)
            if letters == to_visit:
                steps += 1
                break
        pos = next_p
        steps += 1

    print(''.join(letters))
    print(steps + 1)


def main():
    lines = [x for x in utils.get_input(19).split('\n')]
    start = (0, 0)
    for x, char in enumerate(lines[0]):
        if char == '|':
            start = (x, 0)
    print(start)
    run_package(lines, start)


if __name__ == '__main__':
    main()
