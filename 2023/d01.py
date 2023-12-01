#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2023/day/1
"""

writtenToDigits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield (start, sub)
        start += len(sub)


def part1(lines: list[str]) -> int:
    all_digits = []
    for line in lines:
        digits = utils.ints(line)
        all_numbers = "".join([str(i) for i in digits])

        new_number = all_numbers[0] + all_numbers[-1]
        all_digits.append(int(new_number))

    return sum(all_digits)


def part2(lines: list[str]) -> int:
    all_digits = []
    searched_elements = [d for d in writtenToDigits.values()]
    searched_elements.extend(writtenToDigits.keys())
    for line in lines:
        all_found_for_line = []
        for element in searched_elements:
            all_found_for_line.extend(list(find_all(line, element)))

        all_found_for_line.sort(key=lambda x: x[0])
        first_digit = all_found_for_line[0][1]
        second_digit = all_found_for_line[-1][1]
        if first_digit in writtenToDigits:
            first_digit = str(writtenToDigits[first_digit])
        if second_digit in writtenToDigits:
            second_digit = str(writtenToDigits[second_digit])

        all_digits.append(int(f"{first_digit}{second_digit}"))
    return sum(all_digits)


def main():
    input_txt = utils.get_input(1)
    lines = input_txt.strip().split("\n")

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
