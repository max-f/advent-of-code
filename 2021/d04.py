#!/usr/bin/env python

from copy import deepcopy

from utils import utils

"""
Code for https://adventofcode.com/2021/day/4
"""


class Board(object):
    def __init__(self, board_input: str, done=False):
        self.done = done
        self.board = [[None for _ in range(5)] for _ in range(5)]
        rows = board_input.strip().split("\n")
        all_row_entries = [utils.ints(row) for row in rows]
        # TODO: only 5x5 boards
        for x in range(5):
            for y in range(5):
                self.board[x][y] = Number(all_row_entries[x][y])

    def check_number(self, number: int) -> None:
        for x in range(5):
            for y in range(5):
                if self.board[x][y].value == number:
                    self.board[x][y].checked = True

    def calc_remaining_unchecked(self) -> int:
        remaining_sum = 0
        for x in range(5):
            for y in range(5):
                number = self.board[x][y]
                if not number.checked:
                    remaining_sum += number.value
        return remaining_sum

    def is_done(self) -> bool:
        # Check if all entries of one row or one column are checked
        for i in range(5):
            if all(number.checked for number in self.board[i]):
                return True
            if all(number.checked for number in [self.board[x][i] for x in range(5)]):
                return True

        return False


class Number(object):
    def __init__(self, value, checked=False):
        self.value = value
        self.checked = checked

    def __repr__(self):
        return f"Number {self.value}, checked={self.checked}"


def part1(numbers, boards) -> int:
    for number in numbers:
        for board in boards:
            board.check_number(number)
            if board.is_done():
                return number * board.calc_remaining_unchecked()


def part2(numbers, boards) -> int:
    for number in numbers:
        for board in boards:
            if board.done:
                continue

            board.check_number(number)
            if board.is_done():
                board.done = True
                if all(bingo_board.done for bingo_board in boards):
                    return number * board.calc_remaining_unchecked()


def main():
    input_txt = utils.get_input(4)
    sections = input_txt.split("\n\n")

    drawn_numbers = utils.ints(sections[0])
    boards_input = sections[1:]
    boards = [Board(board_input) for board_input in boards_input]
    boards2 = deepcopy(boards)

    print(f"Part 1: {part1(drawn_numbers, boards)}")
    print(f"Part 2: {part2(drawn_numbers, boards2)}")


if __name__ == "__main__":
    main()
