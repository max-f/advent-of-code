#!/usr/bin/env python

from utils import utils


def part1(input_txt: str) -> int:
    overall = 0
    lines = input_txt.split("\n")
    for module_mass in lines:
        module_mass = module_mass.rstrip("\n")
        if module_mass:
            overall += (int(module_mass) // 3) - 2
    return overall


def part2(input_txt: str) -> int:
    overall = 0
    lines = input_txt.split("\n")
    for module_mass in lines:
        module_mass = module_mass.rstrip("\n")
        if module_mass:
            overall += required_fuel(int(module_mass))
    return overall


def required_fuel(mass: int) -> int:
    fuel_tmp = (mass // 3) - 2
    if fuel_tmp <= 0:
        return 0
    else:
        return fuel_tmp + required_fuel(fuel_tmp)


def main():
    input_txt = utils.get_input(1)
    simple_mass = part1(input_txt)
    overall_recurring_mass = part2(input_txt)
    print(f"Part 1: {simple_mass}")
    print(f"Part 2: {overall_recurring_mass}")


if __name__ == "__main__":
    main()
