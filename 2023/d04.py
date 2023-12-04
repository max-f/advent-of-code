#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2023/day/4
"""


def part1(lines: list[str]) -> int:
    result = 0
    for line in lines:
        winning, mine = (utils.ints(numbers) for numbers in line.split("|"))
        winning = winning[1:]

        matching = set(winning).intersection(mine)
        result += int(2 ** (len(matching) - 1))

    return result


def part2(lines: list[str]) -> int:
    winnings = [1] * len(lines)
    for line in lines:
        winning, mine = (utils.ints(numbers) for numbers in line.split("|"))
        card_num = winning[0]
        winning = winning[1:]

        matching = set(winning).intersection(mine)
        winning_cards = len(matching)
        for i in range(card_num, card_num + winning_cards):
            winnings[i] += winnings[card_num - 1]

    return sum(winnings)


def main():
    input_txt = utils.get_input(4)
    lines = input_txt.strip().split("\n")

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
