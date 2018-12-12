#!/usr/bin/env python

from utils import utils


# Don't need all those generations as at certain iteration the difference
# between generations becomes constant
GENERATIONS_ALL = 50_000_000_000
GENERATIONS = 1500
# GENERATIONS = 20
RULE_FRAME = [-2, -1, 0, 1, 2]


def main():
    data = utils.get_input(12).split("\n")[:-1]
    start_pots = data[0].lstrip("initial state: ")
    rule_lines = data[2:]

    rules = dict()
    for rule in rule_lines:
        rule = rule.split(" => ")
        print(rule)
        if rule[-1] == "#":
            rules[rule[0]] = rule[1]

    current_pots = {i for i, c in enumerate(start_pots) if c == "#"}
    diff_before = 0
    iterations = 0

    for gen in range(GENERATIONS):
        new_pots = set()
        start = min(current_pots)
        end = max(current_pots)
        for idx in range(start - 4, end + 5):
            pattern = ["#" if idx + k in current_pots else "." for k in RULE_FRAME]
            pattern_str = "".join(pattern)
            if pattern_str in rules:
                new_pots.add(idx)
        diff = abs(sum(new_pots) - sum(current_pots))
        current_pots = new_pots

        # Break when difference between generations gets constant
        if diff == diff_before:
            iterations = gen + 1
            break
        diff_before = diff

    print(f"Part 1: {sum(current_pots)}")

    result = (GENERATIONS_ALL - iterations) * diff_before + sum(current_pots)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
