#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2021/day/8
"""


def part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        codes = utils.words(line)
        total += sum(
            [
                1
                for code in codes
                if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7
            ]
        )
    return total


def part2(lines: list[str]) -> int:
    total = 0
    for line in lines:
        numbers = dict()
        deduct_start, output = line.split(" | ")
        a = utils.words(deduct_start)
        b = utils.words(output)

        # Fill in 1, 4, 7, 8 first
        for number in a:
            chars = frozenset(number)
            if len(number) == 2:
                numbers[1] = chars
            elif len(number) == 3:
                numbers[7] = chars
            elif len(number) == 4:
                numbers[4] = chars
            elif len(number) == 7:
                numbers[8] = chars
        # Check for the rest
        for number in a:
            # check for 2, 3, 5
            chars = frozenset(number)
            if len(chars) == 5:
                if len(chars & numbers[4]) == 2:
                    numbers[2] = chars
                elif len(chars & (numbers[4] - numbers[1])) == 2:
                    numbers[5] = chars
                else:
                    numbers[3] = chars
            # check for 0, 6, 9
            elif len(chars) == 6:
                if len(chars & numbers[1]) == 1:
                    numbers[6] = chars
                elif len(chars & numbers[4]) == 4:
                    numbers[9] = chars
                else:
                    numbers[0] = chars

        # print(numbers)
        store = {v: k for k, v in numbers.items()}
        # Calculate result
        line_result = 0
        for number in b:
            chars = frozenset(number)
            line_result = line_result * 10 + store[chars]
        total += line_result

    return total


def main():
    input_txt = utils.get_input(8)
    lines = input_txt.strip().split("\n")
    part1_lines = [line.split(" | ")[-1] for line in lines]
    print(f"Part 1: {part1(part1_lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
