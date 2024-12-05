#!/usr/bin/env python

from utils import utils
from collections import defaultdict
from graphlib import TopologicalSorter

"""
Code for https://adventofcode.com/2024/day/5
"""


type RuleDict = dict[int, set[int]]


def parse_rules(rule_list: str) -> RuleDict:
    rules = defaultdict(set)
    for r in rule_list.split("\n"):
        x, y = map(int, r.split("|"))
        rules[x].add(y)
    return rules


def get_middle_value(nums: list[int]) -> int:
    return nums[len(nums) // 2]


def is_valid(update: list[int], rules: dict[int, set[int]]) -> bool:
    for i, n1 in enumerate(update):
        for n2 in update[i + 1 :]:
            if n2 in rules[n1]:
                continue
            if n1 in rules[n2]:
                return False
    return True


def part1(updates: list[list[int]], rules: RuleDict) -> int:
    return sum(
        get_middle_value(update) for update in updates if is_valid(update, rules)
    )


def get_correct_order(update: list[int], rules: RuleDict) -> list[int]:
    # Use topological sort on a DAG where an edge between n1 -> n2 indicates that n1 has to come before n2.
    graph = {n1: {n2 for n2 in update if n1 in rules[n2]} for n1 in update}
    ts = TopologicalSorter(graph)
    return list(ts.static_order())


def part2(updates: list[list[int]], rules: dict[int, set[int]]) -> int:
    total = 0
    for update in updates:
        if is_valid(update, rules):
            continue
        corrected = get_correct_order(update, rules)
        total += get_middle_value(corrected)
    return total


def main():
    input_txt = utils.get_input(5)
    rule_list, updates_list = input_txt.split("\n\n")
    updates = [utils.ints(s) for s in updates_list.split("\n")]
    rules = parse_rules(rule_list)

    print(f"Part1: {part1(updates, rules)}")
    print(f"Part2: {part2(updates, rules)}")


if __name__ == "__main__":
    main()
