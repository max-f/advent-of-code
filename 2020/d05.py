#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/5
"""


def part1(seats: str) -> tuple[int, set[int]]:
    maximum_seat_id = 0
    # only for p2
    all_seat_ids = set()

    for seat in seats.split("\n")[:-1]:
        binary_spacing = list(seat)
        rows = binary_spacing[:7]
        columns = binary_spacing[7:]
        rows_bin = [0 if x == "F" else 1 for x in rows]
        columns_bin = [0 if x == "L" else 1 for x in columns]
        dec_row_number = int("".join(str(i) for i in rows_bin), 2)
        dec_column_number = int("".join(str(i) for i in columns_bin), 2)
        seat_id = dec_row_number * 8 + dec_column_number

        all_seat_ids.add(seat_id)
        if seat_id > maximum_seat_id:
            maximum_seat_id = seat_id
    return maximum_seat_id, all_seat_ids


def part2(maximum: int, all_seat_ids: set[int]) -> int:
    minimum = min(all_seat_ids)
    for i in range(minimum, maximum):
        if i not in all_seat_ids and i - 1 in all_seat_ids and i + 1 in all_seat_ids:
            return i


def main():
    input_txt = utils.get_input(5)
    maximum, all_seat_ids = part1(input_txt)
    print(maximum)
    print(part2(maximum, all_seat_ids))


if __name__ == "__main__":
    main()
