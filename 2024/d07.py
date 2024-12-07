#!/usr/bin/env python
import itertools

from utils import utils
from operator import add, mul
from itertools import product
from typing import Callable

"""
Code for https://adventofcode.com/2024/day/7
"""


def concat(a, b):
    return int(str(a) + str(b))


def evaluate_equation(numbers: list[list[int]], operators: list[Callable]):
    result = numbers[0]
    for i, op in enumerate(operators):
        result = op(result, numbers[i + 1])
    return result


def solve_equations(equations: list[list[int]], allowed_ops: list[Callable]):
    total = 0

    for equation in equations:
        test_value, *numbers = equation
        n_operators = len(numbers) - 1

        # Try all possible combinations of operators
        for ops in product(allowed_ops, repeat=n_operators):
            result = evaluate_equation(numbers, ops)
            if result == test_value:
                total += test_value
                break

    return total


def part1(equations: list[list[int]]) -> int:
    return solve_equations(equations, [add, mul])


def part2(equations: list[list[int]]) -> int:
    return solve_equations(equations, [add, mul, concat])


def main():
    input_txt = utils.get_input(7)
    equations = [utils.ints(s) for s in input_txt.strip().split("\n")]

    print(f"Part1: {part1(equations)}")
    print(f"Part2: {part2(equations)}")


if __name__ == "__main__":
    main()
