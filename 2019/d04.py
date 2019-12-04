#!/usr/bin/env python

from utils import utils


def part1(start, end) -> int:
    total = 0
    for x in range(start, end + 1):
        xs = str(x)
        if sorted(xs) == list(xs):
            same = False
            increase = True
            for pair in utils.sliding_window(xs, 2):
                if pair[0] > pair[1]:
                    increase = False
                    break
                if pair[0] == pair[1]:
                    same = True
            if same and increase:
                total += 1
    return total


def part2(start, end) -> int:
    total = 0
    for x in range(start, end + 1):
        xs = str(x)
        if sorted(xs) == list(xs):
            same = False
            increase = True
            for i in range(0, len(xs)):
                j = i + 1
                if j == len(xs):
                    break
                if xs[i] > xs[j]:
                    increase = False
                    break
                if xs[i] == xs[j] and (i == 0 or xs[i - 1] != xs[i]) and (
                        j == len(xs) - 1 or xs[j + 1] != xs[j]):
                    same = True
            if same and increase:
                total += 1
    return total


def main():
    input_txt = utils.get_input(4)
    start, end = [int(x) for x in input_txt.split('-')]
    p1 = part1(start, end)
    p2 = part2(start, end)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
