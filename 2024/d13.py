#!/usr/bin/env python

from z3 import Solver, Int, sat

from utils import utils


class Machine:
    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]):
        self.a = a
        self.b = b
        self.prize = prize
        self.prize2 = utils.tuple_add(prize, (10000000000000, 10000000000000))

    def __repr__(self):
        return f"Button A: {self.a[0]}, {self.a[1]} - Button B: {self.b[0]}, {self.b[1]} - Prize: {self.prize[0]}, {self.prize[1]}"

    def solve(self, use_prize2: bool = False) -> tuple[int, int]:
        target = self.prize2 if use_prize2 else self.prize
        solver = Solver()
        x = Int("x")
        y = Int("y")
        solver.add(self.a[0] * x + self.b[0] * y == target[0])
        solver.add(self.a[1] * x + self.b[1] * y == target[1])
        solver.add(x >= 0)
        solver.add(y >= 0)

        if solver.check() == sat:
            model = solver.model()
            x_val = model[x].as_long()
            y_val = model[y].as_long()
            return x_val, y_val

        return -1, -1


def part1(machines: list[Machine]) -> int:
    return sum(
        solution[0] * 3 + solution[1]
        for m in machines
        if (solution := m.solve(use_prize2=False)) != (-1, -1)
    )


def part2(machines: list[Machine]) -> int:
    return sum(
        solution[0] * 3 + solution[1]
        for m in machines
        if (solution := m.solve(use_prize2=True)) != (-1, -1)
    )


def main() -> None:
    input_txt = utils.get_input(13)

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
