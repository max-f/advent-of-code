#!/usr/bin/env python

import re
from collections.abc import Callable
from functools import partial

from utils import utils

"""
Code for https://adventofcode.com/2020/day/18
"""


def calc_sum(lines: list[str], eval_inner: Callable[[str], str]) -> int:
    return sum([int(evaluate(line, eval_inner)) for line in lines])


def evaluate(expr: str, eval_inner: Callable[[str], str]) -> str:
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', partial(remove_parentheses, eval_inner=eval_inner), expr)
    return eval_inner(expr)


def remove_parentheses(match, eval_inner: Callable[[str], str]):
    inner_expr = match.group(1)
    return eval_inner(inner_expr)


def evaluate_inner1(expr: str) -> str:
    while '+' in expr or '*' in expr:
        expr = re.sub(r'^(\d+)\s*\+\s*(\d+)', lambda match: str(int(match.group(1)) + int(match.group(2))), expr)
        expr = re.sub(r'^(\d+)\s*\*\s*(\d+)', lambda match: str(int(match.group(1)) * int(match.group(2))), expr)
    return expr


def evaluate_inner2(expr: str) -> str:
    while '+' in expr:
        expr = re.sub(r'(\d+)\s*\+\s*(\d+)', lambda match: str(int(match.group(1)) + int(match.group(2))), expr)
    while '*' in expr:
        expr = re.sub(r'(\d+)\s*\*\s*(\d+)', lambda match: str(int(match.group(1)) * int(match.group(2))), expr)
    return expr


def main():
    input_txt = utils.get_input(18).rstrip()
    lines = input_txt.split('\n')
    print(calc_sum(lines, evaluate_inner1))
    print(calc_sum(lines, evaluate_inner2))


if __name__ == "__main__":
    main()
