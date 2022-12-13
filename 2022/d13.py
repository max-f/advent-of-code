#!/usr/bin/env python

from utils import utils
import functools

"""
Code for https://adventofcode.com/2022/day/13
"""


def compare_element(x1, x2) -> int:
    if isinstance(x1, list) and not isinstance(x2, list):
        x2 = [x2]
    elif not isinstance(x1, list) and isinstance(x2, list):
        x1 = [x1]

    elif isinstance(x1, int) and isinstance(x2, int):
        if x1 < x2:
            return -1
        elif x1 == x2:
            return 0
        else:
            return 1

    for x11, x22 in zip(x1, x2):
        result = compare_element(x11, x22)
        if result != 0:
            return result

    n = len(x1)
    m = len(x2)

    if n < m:
        return -1
    elif n == m:
        return 0
    else:
        return 1


def part2(pairs) -> int:
    pairs.append([[2]])
    pairs.append([[6]])

    sorted_pairs = sorted(pairs, key=functools.cmp_to_key(compare_element))
    x, y = [i for i in range(len(sorted_pairs)) if sorted_pairs[i] in [[[2]], [[6]]]]
    return (x + 1) * (y + 1)


def main():
    input_txt = utils.get_input(13).strip()
    indices = []
    pairs = []

    for idx, pair in enumerate(input_txt.strip().split("\n\n")):
        pairing = pair.split('\n')
        p1 = eval(pairing[0])
        p2 = eval(pairing[1])
        pairs.extend([p1, p2])

        if compare_element(p1, p2) == -1:
            indices.append(idx + 1)

    print(f"Part 1: {sum(indices)}")
    print(f"Part 2: {part2(pairs)}")


if __name__ == "__main__":
    main()
