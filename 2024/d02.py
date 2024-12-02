#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2024/day/2
"""


def _validate_report(report: list[int]) -> bool:
    if len(report) <= 1:
        return True

    is_increasing = report[1] > report[0]

    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        abs_difference = abs(difference)

        if abs_difference < 1 or abs_difference > 3:
            return False

        if (is_increasing and difference <= 0) or (
            not is_increasing and difference >= 0
        ):
            return False

    return True


def check_report(report: list[int]) -> bool:
    return _validate_report(report)


def check_report_with_skip(report: list[int], skip_index: int) -> bool:
    report = report[:skip_index] + report[skip_index + 1 :]
    return _validate_report(report)


def check_report_with_one_mistake(report: list[int]) -> bool:
    if len(report) <= 1:
        return True
    for i in range(len(report)):
        if check_report_with_skip(report, i):
            return True
    return check_report_with_skip(report, -1)


def part1(reports: list[list[int]]) -> int:
    return sum(check_report(report) for report in reports)


def part2(reports: list[list[int]]) -> int:
    return sum(check_report_with_one_mistake(report) for report in reports)


def main():
    input_txt = utils.get_input(2)
    numbers = [utils.ints(line) for line in input_txt.strip().split("\n")]

    print(f"Part1: {part1(numbers)}")
    print(f"Part2: {part2(numbers)}")


if __name__ == "__main__":
    main()
