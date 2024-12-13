#!/usr/bin/env python

from utils import utils
from pprint import pprint

from math import gcd


class Machine:
    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]):
        self.a = a
        self.b = b
        self.prize = prize
        self.prize2 = utils.tuple_add(prize, (10000000000000, 10000000000000))

    def __repr__(self):
        return f"Button A: {self.a[0]}, {self.a[1]} - Button B: {self.b[0]}, {self.b[1]} - Prize: {self.prize[0]}, {self.prize[1]}"

    def solve_dumb(self) -> tuple[int, int]:
        for x in range(100):
            for y in range(100):
                if x * self.a[0] + y * self.b[0] == self.prize[0] and x * self.a[1] + y * self.b[1] == self.prize[1]:
                    return x, y
        return -1, -1

    def solve(self) -> tuple[int, int]:
        return -1, -1


def part1(machines: list[Machine]) -> int:
    total = 0
    for m in machines:
        sol = m.solve_dumb()
        if sol != (-1, -1):
            total += sol[0] * 3 + sol[1]
    return total


def part2(machines: list[Machine]) -> int:
    total = 0
    for m in machines:
        sol = m.solve()
        if sol != (-1, -1):
            total += sol[0] * 3 + sol[1]
    return total


def main() -> None:
    input_txt = utils.get_input(75)

    machine_list = input_txt.strip().split("\n\n")
    machines = []
    for m in machine_list:
        m_lines = m.split("\n")
        a = tuple(utils.ints(m_lines[0]))
        b = tuple(utils.ints(m_lines[1]))
        prize = tuple(utils.ints(m_lines[2]))
        machine = Machine(a, b, prize)
        machines.append(machine)

    print(f"Part1: {part1(machines)}")
    print(f"Part2: {part2(machines)}")


if __name__ == "__main__":
    main()
