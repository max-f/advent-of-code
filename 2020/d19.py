#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/19
"""


def calc_valid_messages(rules: dict, messages: list[str]) -> int:
    return sum(
        1
        for message in messages
        if matches(rules, message, list(reversed(rules[0][0])))
    )


def matches(rules: dict, message: str, stack: list):
    if len(stack) > len(message):
        return False
    if not message or not stack:
        return not message and not stack

    rule_idx = stack.pop()
    if isinstance(rules[rule_idx], list):
        return any(
            [
                matches(rules, message, stack + list(reversed(rule)))
                for rule in rules[rule_idx]
            ]
        )
    elif message[0] == rules[rule_idx]:
        return matches(rules, message[1:], stack.copy())
    return False


def main():
    input_txt = utils.get_input(19).rstrip()
    rules, text = input_txt.split("\n\n")

    all_rules = {}
    for rule_line in rules.split("\n"):
        idx, rule = rule_line.split(": ")
        if "|" in rule:
            or_rules = rule.split("|")
            or_rules = [utils.ints(x) for x in or_rules]
            all_rules[int(idx)] = or_rules
        elif '"' in rule:
            char = rule.strip('"')
            all_rules[int(idx)] = char
        else:
            and_rules = utils.ints(rule)
            all_rules[int(idx)] = [and_rules]

    messages = text.split("\n")
    print(calc_valid_messages(all_rules, messages))

    all_rules[8] = [[42], [42, 8]]
    all_rules[11] = [[42, 31], [42, 11, 31]]
    print(calc_valid_messages(all_rules, messages))


if __name__ == "__main__":
    main()
