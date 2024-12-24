#!/usr/bin/env python

from utils import utils
from itertools import combinations
import operator
import re


OPERATIONS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}


def binary_to_decimal(dictionary):
    z_keys = sorted([k for k in dictionary.keys() if k.startswith("z")])
    print("Z wires in order:", z_keys)
    binary_str = "".join(str(dictionary[k]) for k in reversed(z_keys))
    print("Binary string:", binary_str)
    return int(binary_str, 2) if binary_str else 0


def part1(initial_values, gates):
    wires_with_values = initial_values.copy()

    while True:
        made_progress = False
        for wire1, wire2, op, output_wire in gates:
            if output_wire in wires_with_values:
                continue

            if wire1 in wires_with_values and wire2 in wires_with_values:
                result = OPERATIONS[op](
                    wires_with_values[wire1], wires_with_values[wire2]
                )
                wires_with_values[output_wire] = result
                made_progress = True

        if not made_progress:
            break

    return binary_to_decimal(wires_with_values)


def main() -> None:
    input_txt = utils.get_input(24)
    initial_values_lines, gate_lines = input_txt.strip().split("\n\n")

    initial_values = dict()
    for line in initial_values_lines.split("\n"):
        wire, value = line.split(":")
        initial_values[wire] = int(value)

    gates = []
    pattern = r"^(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)$"
    for line in gate_lines.split("\n"):
        match = re.match(pattern, line)
        if match:
            wire1, operator, wire2, wire3 = match.groups()
            gates.append((wire1, wire2, operator.strip(), wire3))


    print(f"Part1: {part1(initial_values, gates)}")
    # print(f"Part2: {part2(G)}")


if __name__ == "__main__":
    main()
