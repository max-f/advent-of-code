#!/usr/bin/env python

import re

from utils import utils
from collections import deque

"""
Code for https://adventofcode.com/2025/day/10
"""

LIGHT_PATTERN = r"\[([.#]+)\]"
BUTTON_PATTERN = r"\(([\d,]+)\)"
WIRING_PATTERN = r"\{([\d,]+)\}"


class Machine:
    def __init__(self, target: tuple[bool, ...], buttons: list[set[int]]):
        self.target = target
        self.buttons = buttons

    def __repr__(self):
        return f"lights: {self.target} - buttons: {self.buttons}"

    @classmethod
    def from_line(cls, line: str) -> "Machine":
        light_match = re.search(LIGHT_PATTERN, line)
        # lights = {i: c == '#' for i, c in enumerate(light_match.group(1))}
        target = tuple(c == "#" for c in light_match.group(1))
        buttons = [set(utils.ints(b)) for b in re.findall(BUTTON_PATTERN, line)]
        return cls(target, buttons)

    def turn_on(self) -> int:
        n_lights = len(self.target)

        # lights off at start!
        initial = tuple(False for _ in range(n_lights))
        target = self.target

        if initial == target:
            return 0

        visited = {initial}
        queue = deque([(initial, 0)])

        while queue:
            state, presses = queue.popleft()

            for button in self.buttons:
                # xor works for light on/off + button toggling
                new_state = tuple(val ^ (i in button) for i, val in enumerate(state))
                if new_state == target:
                    return presses + 1

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, presses + 1))

        return 0


def main():
    input_txt = utils.get_input(10)
    machines = [Machine.from_line(line) for line in input_txt.strip().splitlines()]
    result = sum(m.turn_on() for m in machines)
    print(f"Part1: {result}")


if __name__ == "__main__":
    main()
