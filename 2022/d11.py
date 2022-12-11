#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/11
"""


def part1() -> int:
    pass


def part2() -> None:
    pass


class Monkey:
    def __init__(self, ident, items, operation, test, ttt, ttf):
        self.ident = ident
        self.items = items
        self.operation = operation
        self.test = test
        self.ttt = ttt
        self.ttf = ttf
        self.inspections = 0

    def round(self, monkeys, modulo):
        for i, item in enumerate(self.items):
            self.inspections += 1
            # new_worry = self.operation(worry) // 3
            new_worry = self.operation(item) % modulo
            if self.test(new_worry):
                monkeys[self.ttt].items.append(new_worry)
            else:
                monkeys[self.ttf].items.append(new_worry)

        self.items = []

    def __repr__(self):
        return f"monkey {self.ident} - inspections: {self.inspections} - items: {self.items}"

def main():
    #input_txt = utils.get_input(11).strip()

    # hard coded right now :(

    monkey0 = Monkey(0,
                     [66, 59, 64, 51],
                     lambda x: x * 3,
                     lambda x: x % 2 == 0,
                     1,
                     4
    )
    monkey1 = Monkey(1,
                     [67, 61],
                     lambda x: x * 19,
                     lambda x: x % 7 == 0,
                     3,
                     5
    )
    monkey2 = Monkey(2,
                     [86, 93, 80, 70, 71, 81, 56],
                     lambda x: x + 2,
                     lambda x: x % 11 == 0,
                     4,
                     0
    )
    monkey3 = Monkey(3,
                     [94],
                     lambda x: x * x,
                     lambda x: x % 19 == 0,
                     7,
                     6
    )
    monkey4 = Monkey(4,
                     [71, 92, 64],
                     lambda x: x + 8,
                     lambda x: x % 3 == 0,
                     5,
                     1
    )
    monkey5 = Monkey(5,
                     [58, 81, 92, 75, 56],
                     lambda x: x + 6,
                     lambda x: x % 5 == 0,
                     3,
                     6
    )
    monkey6 = Monkey(6,
                     [82, 98, 77, 94, 86, 81],
                     lambda x: x + 7,
                     lambda x: x % 17 == 0,
                     7,
                     2
    )
    monkey7 = Monkey(7,
                     [54, 95, 70, 93, 88, 93, 63, 50],
                     lambda x: x + 4,
                     lambda x: x % 13 == 0,
                     2,
                     0
    )

    monkeys = {0: monkey0, 1: monkey1, 2: monkey2, 3: monkey3, 4: monkey4,
               5: monkey5, 6: monkey6, 7: monkey7}


    modulo = 1
    for i in [2, 7, 11, 19, 3, 5, 17, 13]:
        modulo *= i

    for _ in range(10000):
        for key, monkey in monkeys.items():
            monkey.round(monkeys, modulo)

    most_inspections = sorted([m for m in monkeys.values()], key=lambda m: m.inspections)
    print(most_inspections[-1].inspections * most_inspections[-2].inspections)

    # print(f"Part1: {part1()}")
    # print(f"Part2:")


if __name__ == "__main__":
    main()
