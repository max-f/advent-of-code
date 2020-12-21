#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/21
"""


def solve(a_to_is: dict) -> None:
    while not is_solved(a_to_is):
        for all_, ingredients in a_to_is.items():
            if not ingredients:
                continue
            elif isinstance(ingredients, str):
                continue
            elif isinstance(ingredients, set):
                if len(ingredients) == 1:
                    ing = ingredients.pop()
                    a_to_is[all_] = ing
                    remove(a_to_is, ing)


def is_solved(a_to_is: dict) -> bool:
    solved = [True if not x or isinstance(x, str) else False for x in a_to_is.values()]
    return all(solved)


def remove(a_to_is: dict, ingredient: str) -> None:
    for all_, ingredients in a_to_is.items():
        if isinstance(ingredients, set) and ingredient in ingredients:
            ingredients.remove(ingredient)


def part1(a_to_is: dict, lines: list[str]) -> int:
    total = 0
    for line in lines:
        if "(contains" in line:
            p1, p2 = line.split("(contains")
            ingredients = utils.words(p1)
            total += sum([1 for ing in ingredients if ing not in a_to_is.values()])
        else:
            ingredients = utils.words(line)
            total += sum([1 for ing in ingredients if ing not in a_to_is.values()])
    return total


def part2(a_to_is: dict) -> str:
    dangerous_ingredients = [v for k, v in sorted(a_to_is.items())]
    return ",".join(dangerous_ingredients)


def main():
    input_txt = utils.get_input(21).rstrip()
    lines = input_txt.split("\n")

    a_to_is = {}

    for line in lines:
        if "(contains" in line:
            p1, p2 = line.split("(contains")
            ingredients = utils.words(p1)
            allergens_ = utils.words(p2)
            for all_ in allergens_:
                if all_ in a_to_is:
                    a_to_is[all_] &= set(ingredients)
                else:
                    a_to_is[all_] = set(ingredients)

    solve(a_to_is)
    print(part1(a_to_is, lines))
    print(part2(a_to_is))


if __name__ == "__main__":
    main()
