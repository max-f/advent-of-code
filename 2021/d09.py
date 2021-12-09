#!/usr/bin/env python

from math import prod

from utils import utils

"""
Code for https://adventofcode.com/2021/day/9
"""


def neighbors(board: list[list[int]], coord: tuple[int, int]):
    x, y = coord

    for xd, yd in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x2, y2 = x + xd, y + yd
        if 0 <= x2 < len(board[0]) and 0 <= y2 < len(board):
            yield (x2, y2), board[y2][x2]


def part2(board: list[list[int]], min_pos: list[tuple[int, int]]) -> int:
    basins = []

    for mp in min_pos:
        todo = [coord for coord, height in neighbors(board, mp) if height < 9]
        done = set(todo)
        size = 1
        while todo:
            x, y = todo.pop()
            size += 1
            height = board[y][x]
            for n, nh in neighbors(board, (x, y)):
                if height < nh < 9 and n not in done:
                    todo.append(n)
                    done.add(n)
        basins.append(size)

    basins.sort()
    return prod(basins[-3:])


def main():
    input_txt = utils.get_input(9)
    lines = input_txt.strip().split("\n")
    board = [[int(x) for x in line] for line in lines]

    mins = []
    min_pos = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            current = board[y][x]
            values = [value for pos, value in neighbors(board, (x, y))]

            if current < min(values):
                mins.append(current)
                min_pos.append((x, y))
    print(f"Part 1: {sum([x + 1 for x in mins])}")
    print(f"Part 2: {part2(board, min_pos)}")


if __name__ == "__main__":
    main()
