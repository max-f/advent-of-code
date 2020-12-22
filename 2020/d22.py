#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/22
"""


def part1(player1, player2) -> int:
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.extend([p1, p2])
        else:
            player2.extend([p2, p1])

    win_stack = player1 if player1 else player2
    return sum(i * v for i, v in enumerate(win_stack[::-1], 1))


def combat(p1_stack: list[int], p2_stack: list[int]) -> tuple[int, list[int]]:
    previous = set()

    while p1_stack and p2_stack:
        cur = (tuple(p1_stack), tuple(p2_stack))
        if cur in previous:
            return 1, p1_stack
        previous.add(cur)

        p1 = p1_stack.pop(0)
        p2 = p2_stack.pop(0)
        if len(p1_stack) >= p1 and len(p2_stack) >= p2:
            winner, _ = combat(p1_stack.copy()[:p1], p2_stack.copy()[:p2])
            if winner == 1:
                p1_stack.extend([p1, p2])
            else:
                p2_stack.extend([p2, p1])

        elif p1 > p2:
            p1_stack.extend([p1, p2])
        else:
            p2_stack.extend([p2, p1])
    if p1_stack:
        return 1, p1_stack
    return 2, p2_stack


def part2(player1, player2) -> int:
    _, win_stack = combat(player1, player2)
    return sum(i * v for i, v in enumerate(win_stack[::-1], 1))


def main():
    input_txt = utils.get_input(22).rstrip()
    p1, p2 = input_txt.split("\n\n")

    player1 = []
    for line in p1.split("\n")[1:]:
        player1.append(int(line))

    player2 = []
    for line in p2.split("\n")[1:]:
        player2.append(int(line))

    print(part1(player1.copy(), player2.copy()))
    print(part2(player1, player2))


if __name__ == "__main__":
    main()
