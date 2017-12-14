#!/usr/bin/env python

from utils import utils


def part_one(day: int) -> None:
    valid = 0

    input_str = utils.get_input(day)
    for line in input_str.split('\n'):
        words = line.split()
        if words and len(set(words)) == len(words):
            valid += 1
    print(valid)


def part_two(day: int) -> None:
    valid = 0

    input_str = utils.get_input(day)
    for line in input_str.split('\n'):
        words = line.split()
        if words and is_valid(words):
            valid += 1
    print(valid)


def is_valid(words: list) -> bool:
    for i, word_a in enumerate(words[:len(words)]):
        for word_b in words[i + 1:]:
            if sorted(word_a) == sorted(word_b):
                return False
    return True


def main():
    part_one(4)
    part_two(4)


if __name__ == '__main__':
    main()
