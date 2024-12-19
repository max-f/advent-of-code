#!/usr/bin/env python

from utils import utils
import functools


def part1(patterns, towels) -> int:
    @functools.cache
    def is_possible(pattern):
        if not pattern:
            return True
        return any(
            is_possible(pattern[len(p) :]) for p in patterns if pattern.startswith(p)
        )

    return sum(1 for t in towels if is_possible(t))


def part2(patterns, towels) -> int:
    @functools.cache
    def is_possible(pattern):
        if not pattern:
            return 1
        return sum(
            is_possible(pattern[len(p) :]) for p in patterns if pattern.startswith(p)
        )

    return sum(is_possible(t) for t in towels)


def main() -> None:
    input_txt = utils.get_input(19)
    pattern_line, design_lines = input_txt.strip().split("\n\n")
    patterns = utils.words(pattern_line)
    towels = [s for s in design_lines.split("\n")]

    print(f"Part1: {part1(patterns, towels)}")
    print(f"Part2: {part2(patterns, towels)}")


if __name__ == "__main__":
    main()
