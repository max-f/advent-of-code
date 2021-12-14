#!/usr/bin/env python

from collections import Counter
from collections import defaultdict

from utils import utils

"""
Code for https://adventofcode.com/2021/day/14
"""


def part1(start, rules):
    for _ in range(10):
        new_poly = []
        for window in utils.sliding_window(start, 2):
            pair = "".join(window)
            new_poly.extend([window[0], rules[pair]])
        new_poly.append(start[-1])
        start = new_poly

    poly = "".join(start)
    quantities = Counter(poly).most_common()
    return quantities[0][1] - quantities[-1][1]


def part2(start, rules):
    pairs = defaultdict(int)
    for window in utils.sliding_window(start, 2):
        pair = "".join(window)
        pairs[pair] += 1

    chars = defaultdict(int)
    for c in start:
        chars[c] += 1

    for _ in range(40):
        new_dict = pairs.copy()
        for pair, count in pairs.items():
            c1, c2 = pair
            c3 = rules[pair]
            new_dict[c1 + c2] -= count
            new_dict[c1 + c3] += count
            new_dict[c3 + c2] += count
            chars[c3] += count
        pairs = new_dict

    return max(chars.values()) - min(chars.values())


def main():
    input_txt = utils.get_input(14)
    start, rule_lines = input_txt.split("\n\n")

    rules = defaultdict(str)
    for rule in rule_lines.splitlines():
        pair, result = rule.split(" -> ")
        rules[pair] = result

    print(f"Part 1: {part1(list(start), rules)}")
    print(f"Part 2: {part2(list(start), rules)}")


if __name__ == "__main__":
    main()
