#!/usr/bin/env python

from utils import utils
from collections import defaultdict
from graphlib import TopologicalSorter

"""
Code for https://adventofcode.com/2024/day/5
"""


def is_valid(update: list[int], rules: dict[int, set[int]]) -> bool:
    for i, n1 in enumerate(update):
        for j, n2 in enumerate(update[i + 1:], i + 1):
            if n2 in rules[n1]:
                continue
            if n1 in rules[n2]:
                return False
    return True


def part1(updates: list[list[int]], rules: dict[int, set[int]]) -> int:
    total = 0
    for update in updates:
        if is_valid(update, rules):
            middle = update[len(update) // 2]
            print(middle)
            total += middle
    return total


def get_correct_order(update: list[int], rules: dict[int, set[int]]) -> list[int]:
    graph = {}
    for p in update:
        satisfy = set()
        for o in update:
            if p in rules[o]:
                satisfy.add(o)
        graph[p] = satisfy
    ts = TopologicalSorter(graph)
    return list(ts.static_order())


def part2(updates: list[list[int]], rules: dict[int, set[int]]) -> int:
    total = 0
    for update in updates:
        if is_valid(update, rules):
            continue
        corrected = get_correct_order(update, rules)
        middle = corrected[len(corrected) // 2]
        total += middle
    return total


def main():
    input_txt = utils.get_input(5)
    rule_l, updates = input_txt.split("\n\n")
    updates = updates.split("\n")
    updates = [utils.ints(s) for s in updates]

    rules = defaultdict(set)
    for r in rule_l.split("\n"):
        x, y = map(int, r.split("|"))
        rules[x].add(y)

    print(f"Part1: {part1(updates, rules)}")
    print(f"Part2: {part2(updates, rules)}")


if __name__ == "__main__":
    main()
