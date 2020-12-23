#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/23
"""


class Cup:
    __slots__ = ["value", "next"]

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Value: {self.value}"


def part2(cup_labels: list[int]):
    cups = {cup: Cup(cup) for cup in cup_labels}
    for x, y in get_next_cups(cup_labels):
        cups[x].next = cups[y]

    start = cups[cup_labels[0]]
    for _ in range(10 ** 7):
        t1 = start.next
        t2 = t1.next
        t3 = t2.next

        destination_value = search_destination2(cup_labels, start.value, t1, t2, t3)
        destination = cups[destination_value]

        # Repoint references to insert t1-t3 at correct place and move start for next iteration
        start.next = t3.next
        start = t3.next
        t3.next = destination.next
        destination.next = t1

    return cups[1].next.value * cups[1].next.next.value


def get_next_cups(line):
    for i, x in enumerate(line):
        if i < len(line) - 1:
            yield x, line[i + 1]
        else:
            yield x, line[0]


def search_destination2(cup_labels, start_value, t1, t2, t3):
    while True:
        start_value -= 1
        if start_value == 0:
            start_value = len(cup_labels)
        if start_value not in (t1.value, t2.value, t3.value):
            return start_value


def part1(cups: list[int]) -> int:
    for _ in range(100):
        next_three = cups[1:4]

        idx = cups.index(search_destination(cups, next_three))
        before, after = cups[:idx], cups[idx + 1 :]
        cups = before[4:] + [cups[idx]] + next_three + after + [cups[0]]

    return cups


def search_destination(cups, next_three) -> int:
    destination = cups[0] - 1
    if destination == 0:
        destination = max(cups)
    while destination in next_three:
        destination -= 1
        if destination == 0:
            destination = max(cups)
    return destination


def main():
    input_txt = utils.get_input(23).rstrip()
    numbers = [int(x) for x in list(input_txt)]
    numbers2 = numbers.copy()

    print(f"Do sorting by hand - clockwise numbers after 1: {part1(numbers)}")

    numbers2.extend(list(range(10, 10 ** 6 + 1)))
    print(part2(numbers2))


if __name__ == "__main__":
    main()
