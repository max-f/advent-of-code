#!/usr/bin/env python

from utils import utils
from pprint import pprint


COLUMNS = 5


def test_is_lock(pattern) -> bool:
    return all(char == "#" for char in pattern[0])


def parse(pattern, is_lock=True):
    counts = {}
    start_row = 1 if is_lock else 0
    end_row = len(pattern) - 1 if not is_lock else len(pattern)

    for col in range(COLUMNS):
        count = sum(1 for row in range(start_row, end_row) if pattern[row][col] == "#")
        counts[col] = count

    return counts


def part1(patterns):
    locks = []
    keys = []
    for pattern in patterns:
        is_lock = test_is_lock(pattern)
        if is_lock:
            locks.append(parse(pattern))
        else:
            keys.append(parse(pattern, is_lock=False))

    result = 0
    for lock in locks:
        for key in keys:
            valid = True
            for i in range(COLUMNS):
                if key[i] + lock[i] > 5:
                    valid = False
                    break
            if valid:
                result += 1
    return result


def main() -> None:
    input_txt = utils.get_input(25)
    patterns = input_txt.strip().split("\n\n")
    patterns = [[line.strip() for line in p.split("\n")] for p in patterns]

    print(f"Part1: {part1(patterns)}")


if __name__ == "__main__":
    main()
