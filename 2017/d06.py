#!/usr/bin/env python

import numpy as np

from utils import utils


def part_two(day: int) -> None:
    configs = dict()
    input_str = utils.get_input(day)
    xs = [int(x) for x in input_str.split()]

    n = 0
    configs[tuple(xs)] = n

    while True:
        max_idx = np.argmax(xs)
        config = redistribute(max_idx, xs)
        n += 1
        if config in configs:
            print(n - configs[config])
            break
        configs[config] = n


def part_one(day: int) -> None:
    configs = set()
    input_str = utils.get_input(day)
    xs = [int(x) for x in input_str.split()]
    configs.add(tuple(xs))
    n = 0

    while True:
        max_idx = np.argmax(xs)
        config = redistribute(max_idx, xs)
        n += 1
        if config in configs:
            break
        configs.add(config)

    print(n)


def redistribute(idx: int, xs: list) -> tuple:
    # Hello side effects! :F
    banks = xs[idx]
    xs[idx] = 0
    while banks > 0:
        if idx == len(xs) - 1:
            idx = 0
        else:
            idx += 1
        xs[idx] += 1
        banks -= 1
    return tuple(xs)


def main():
    part_one(6)
    part_two(6)


if __name__ == '__main__':
    main()
