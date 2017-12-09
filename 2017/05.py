#!/usr/bin/env python

from utils import utils


def part_one(day: int) -> None:
    steps = 0
    idx = 0

    input_str = utils.get_input(day)
    instructions = list(map(int, input_str.rstrip().split('\n')))

    while (True):
        try:
            tmp_idx = idx
            idx += instructions[idx]
            instructions[tmp_idx] += 1
            steps += 1
        except IndexError:
            break
    print(steps)


def part_two(day: int) -> None:
    steps = 0
    idx = 0

    input_str = utils.get_input(day)
    # input_str = '0\n3\n0\n1\n-3'
    instructions = list(map(int, input_str.rstrip().split('\n')))

    while (True):
        try:
            offset = instructions[idx]
            tmp_idx = idx
            idx += instructions[idx]
            if offset >= 3:
                instructions[tmp_idx] -= 1
            else:
                instructions[tmp_idx] += 1
            steps += 1
        except IndexError:
            break
    # assert steps == 10
    print(steps)


def main():
    part_one(5)
    part_two(5)


if __name__ == '__main__':
    main()
