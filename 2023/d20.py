#!/usr/bin/env python

from utils import utils
from pprint import pprint
from collections import defaultdict
from collections import deque

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
        self.state = 'off'

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


def part1(lines) -> int:
    return 0


def part2(lines) -> int:
    return 0


def main():
    input_txt = utils.get_input(75).strip()
    modules = {}
    broadcast_targets = []

    # create modules
    for line in input_txt.split('\n'):
        name, targets = line.split(' -> ')
        targets = targets.split(', ')
        match name[0]:
            case '%':
                modules[name[1:]] = FlipFlopModule(name[1:], targets)
            case '&':
                modules[name[1:]] = ConjunctionModule(name[1:], targets)
            case _:
                modules[name] = BroadcastModule(name, targets)
                broadcast_targets = targets

    # main logic to send pulses through modules
    total_low = total_high = 0
    for _ in range(4):
        # pprint(modules)
        total_low += 1
        q = deque([('broadcaster', name, 0) for name in broadcast_targets])

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
                    module.state = 'on' if module.state == 'off' else 'off'
                    outgoing = 1 if module.state == 'on' else 0
                    for t in module.targets:
                        q.append((target, t, outgoing))

            else:
                module.memory[origin] = pulse_type
                outgoing = 0 if all(x for x in module.memory.values()) else 1
                for t in module.targets:
                    q.append((target, t, outgoing))
            print(total_low, total_high)

    # print('After 3 iterations:')
    # pprint(modules)
    # print(total_low)
    # print(total_high)
    print(total_low * total_high)


# print(f"Part 1: {part1(lines)}")
# print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
