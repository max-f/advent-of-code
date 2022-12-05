#!/usr/bin/env python

from utils import utils
from collections import defaultdict
from copy import deepcopy

"""
Code for https://adventofcode.com/2022/day/5
"""


def part1(stack: dict[int, list[str]], moves: str) -> str:
    for line in moves.splitlines():
        times, s1, s2 = utils.ints(line)
        for _ in range(times):
            elem = stack[s1].pop()
            stack[s2].append(elem)

    return get_end(stack)


def part2(stack: dict[int, list[str]], moves: str) -> str:
    for line in moves.splitlines():
        how_many, s1, s2 = utils.ints(line)
        elem = stack[s1][-how_many:]
        del stack[s1][-how_many:]
        stack[s2].extend(elem)

    return get_end(stack)


def get_end(stack: dict[int, list[str]]) -> str:
    end = [stack[x][-1] for x in range(1, len(stack) + 1)]
    return "".join(end)


def main():
    input_txt = utils.get_input(5)
    stacks, moves = input_txt.split("\n\n")
    stack = defaultdict(list)
    for line in stacks.split("\n"):
        for i, c in enumerate(line):
            if c.isupper():
                stack[(i // 4) + 1].append(c)
    for k, v in stack.items():
        stack[k] = v[::-1]
    stack2 = deepcopy(stack)

    print(f"Part1: {part1(stack, moves)}")
    print(f"Part2: {part2(stack2, moves)}")


if __name__ == "__main__":
    main()
