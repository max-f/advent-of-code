#!/usr/bin/env python

from __future__ import annotations

from itertools import combinations
from typing import Tuple, List, FrozenSet
from copy import deepcopy
import numpy as np

from utils.utils import get_input, ints, tuple_add


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0] * 3

    def change_velocity(self, other: Moon) -> None:
        for idx in range(len(self.position)):
            ax = self.position[idx]
            other_ax = other.position[idx]
            if ax < other_ax:
                self.velocity[idx] += 1
                other.velocity[idx] -= 1
            if ax > other_ax:
                self.velocity[idx] -= 1
                other.velocity[idx] += 1
        return

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()

    def potential_energy(self) -> int:
        return sum(map(abs, self.position))

    def kinetic_energy(self) -> int:
        return sum(map(abs, self.velocity))

    def __repr__(self):
        return f'pos=<x={self.position[0]:03}, y={self.position[1]:03}, z={self.position[2]:03}>'

    def __eq__(self, other):
        return self.position == other.position and self.velocity == other.velocity

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.position, tuple(self.velocity)))


def simulate_step(moons: List[Moon]) -> None:
    all_pairs = list(combinations(moons, 2))
    for a, b in all_pairs:
        a.change_velocity(b)

    for moon in moons:
        moon.position = tuple_add(moon.position, moon.velocity)


def part1(moons: List[Moon]) -> int:
    for i in range(1000):
        simulate_step(moons)
        for m in moons:
            print(m)

    total_energy = 0
    for m in moons:
        total_energy += m.total_energy()
    return total_energy


def get_state_for_pos_idx(pos_idx,
                          moons: List[Moon]) -> FrozenSet[Tuple[int, int]]:
    return frozenset([(x.position[pos_idx], x.velocity[pos_idx])
                      for x in moons])


def find_loop(pos_idx, moons) -> int:
    count = 0
    states = {get_state_for_pos_idx(pos_idx, moons): count}
    while True:
        simulate_step(moons)
        count += 1
        state = get_state_for_pos_idx(pos_idx, moons)
        if state in states:
            old_step = states[state]
            print(f'Loop for {pos_idx}: {count - old_step}')
            return count - old_step
        if count % 100000 == 0:
            print(f'Step {count}..')


def main():
    input_txt = get_input(12)
    moons = []

    for line in input_txt.rstrip().split('\n'):
        moon_pos = tuple(ints(line))
        moon = Moon(moon_pos)
        moons.append(moon)

    p1 = part1(moons)
    print(f'Part 1: {p1}')

    loop_lengths = []
    for pos_idx in range(3):
        loop_length = find_loop(pos_idx, deepcopy(moons))
        loop_lengths.append(loop_length)
    print(loop_lengths)
    p2 = np.lcm.reduce(loop_lengths)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
