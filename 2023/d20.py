#!/usr/bin/env python

from collections import defaultdict
from collections import deque
from math import lcm

from utils import utils

"""
Code for https://adventofcode.com/2023/day/20
"""


class Module:
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets

    def __repr__(self):
        return f"{self.name} {{type: broadcaster, targets: {self.targets} }}"


class FlipFlopModule(Module):
    def __init__(self, name, targets):
        super().__init__(name, targets)
        self.state = "off"

    def __repr__(self):
        return f"{self.name} {{type: %, targets: {self.targets}, state: {self.state} }}"


class ConjunctionModule(Module):
    def __init__(self, name, targets):
        super().__init__(name, targets)
        self.memory = defaultdict(int)

    def __repr__(self):
        return f"{self.name} {{type: &, targets: {self.targets}, memory: {str(self.memory)} }}"


class BroadcastModule(Module):
    def __init__(self, name, targets):
        super().__init__(name, targets)


def part1(lines: list[str]) -> int:
    modules = {}
    broadcast_targets = []

    # create modules
    for line in lines:
        name, targets = line.split(" -> ")
        targets = targets.split(", ")
        match name[0]:
            case "%":
                modules[name[1:]] = FlipFlopModule(name[1:], targets)
            case "&":
                modules[name[1:]] = ConjunctionModule(name[1:], targets)
            case _:
                modules[name] = BroadcastModule(name, targets)
                broadcast_targets = targets

    # Need to set initial memory for conjunction modules
    for name, module in modules.items():
        for t in module.targets:
            if t in modules and isinstance(modules[t], ConjunctionModule):
                modules[t].memory[name] = 0

    # main logic to send pulses through modules
    total_low = total_high = 0
    for _ in range(1000):
        total_low += 1
        q = deque([("broadcaster", name, 0) for name in broadcast_targets])

        while q:
            origin, target, pulse_type = q.popleft()

            if not pulse_type:
                total_low += 1
            else:
                total_high += 1

            if target not in modules:
                continue

            module = modules[target]

            if isinstance(module, FlipFlopModule):
                if not pulse_type:
                    module.state = "on" if module.state == "off" else "off"
                    out_pulse = 1 if module.state == "on" else 0
                    for t in module.targets:
                        q.append((module.name, t, out_pulse))

            else:
                module.memory[origin] = pulse_type
                out_pulse = 0 if all(x == 1 for x in module.memory.values()) else 1
                for t in module.targets:
                    q.append((module.name, t, out_pulse))

    return total_low * total_high


def part2(lines) -> int:
    modules = {}
    broadcast_targets = []

    # create modules
    for line in lines:
        name, targets = line.split(" -> ")
        targets = targets.split(", ")
        match name[0]:
            case "%":
                modules[name[1:]] = FlipFlopModule(name[1:], targets)
            case "&":
                modules[name[1:]] = ConjunctionModule(name[1:], targets)
            case _:
                modules[name] = BroadcastModule(name, targets)
                broadcast_targets = targets

    # Need to set initial memory for conjunction modules
    for name, module in modules.items():
        for t in module.targets:
            if t in modules and isinstance(modules[t], ConjunctionModule):
                modules[t].memory[name] = 0

    # The rx module in question is fed in by a single conjunction module which in turn is fed in by
    # a series of conjunction modules. We need to find the loop lengths of the second level conjunction modules
    # to find the earliest 'sync' between them => the least common multiple of all those loop lengths
    (feed_in,) = [name for name, module in modules.items() if "rx" in module.targets]
    feed_in_second_level = [
        name for name, module in modules.items() if feed_in in module.targets
    ]

    loop_lengths = {name: 0 for name in feed_in_second_level}

    # main logic to send pulses through modules
    idx = 1
    while True:
        q = deque([("broadcaster", name, 0) for name in broadcast_targets])

        while q:
            origin, target, pulse_type = q.popleft()

            if target not in modules:
                continue

            module = modules[target]

            if isinstance(module, FlipFlopModule):
                if not pulse_type:
                    module.state = "on" if module.state == "off" else "off"
                    out_pulse = 1 if module.state == "on" else 0
                    for t in module.targets:
                        q.append((module.name, t, out_pulse))

            else:
                module.memory[origin] = pulse_type
                out_pulse = 0 if all(x == 1 for x in module.memory.values()) else 1
                if module.name in loop_lengths and out_pulse:
                    loop_lengths[module.name] = idx
                for t in module.targets:
                    q.append((module.name, t, out_pulse))

        if all(loop_lengths.values()):
            break
        idx += 1
    return lcm(*loop_lengths.values())


def main():
    lines = utils.get_input(20).strip().split("\n")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
