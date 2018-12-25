#!/usr/bin/env python

import re
from copy import deepcopy

from utils import utils


def parse(line):
    pattern = '^(\d+).* (\d+) .* (\d+) (\w+) damage.* (\d+)$'
    regex = re.compile(pattern)
    match = regex.match(line)
    if not match:
        return None
    units = int(match.group(1))
    hit_points = int(match.group(2))
    attack = int(match.group(3))
    attack_type = match.group(4)
    initiative = int(match.group(5))

    weak_pattern = r'.*weak to ([a-z, ]*)(;|\))'
    weak_regex = re.compile(weak_pattern)
    weak = []
    match_weak = weak_regex.match(line)
    if match_weak:
        weak = match_weak.group(1).split(', ')

    immune_pattern = r'.*immune to ([a-z, ]*)(;|\))'
    immune_regex = re.compile(immune_pattern)
    immune = []
    match_immune = immune_regex.match(line)
    if match_immune:
        immune = match_immune.group(1).split(', ')

    return units, hit_points, attack, attack_type, initiative, weak, immune


class Group():
    def __init__(self,
                 units,
                 hit_points,
                 attack,
                 attack_type,
                 initiative,
                 type,
                 weak=None,
                 immune=None):
        self.units = units
        self.hit_points = hit_points
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative
        self.type = type
        self.weak = weak
        self.immune = immune

    def power(self):
        """
        Calculate effective power.
        """
        return self.units * self.attack

    def __lt__(self, other):
        """
        Enable sorting for target selection priority.
        """
        if self.power() == other.power():
            return self.initiative < other.initiative
        return self.power() < other.power()

    def get_target(self, groups):
        for g in groups:
            if g 

    def attack_damage(self, other):
        if self.attack_type in other.weak:
            return self.power() * 2
        elif self.attack_type in other.immune:
            return 0
        return self.power()

    def attack(self, other):
        damage = self.attack_damage(other)
        losses = damage // other.hit_points
        modified = deepcopy(other)
        if losses >= modified.hit_points:
            modified.units = 0
        else:
            modified.units -= losses


def tick(groups):
    for group in sorted(groups):
        max_dmg = None



def main():
    immune_data, infection_data = utils.get_input(24).split('\n\n')
    immune_lines = immune_data.split('\n')
    infection_lines = infection_data.split('\n')

    groups = []

    # Immune system
    for i, line in enumerate(immune_lines[1:]):
        parse_result = parse(line)
        if parse_result:
            units, hit_points, attack, attack_type, initiative, weak, immune = parse_result
            group = Group(units, hit_points, attack, attack_type, initiative, type=0,
                          weak, immune)
            groups.append(group)

    # Infection
    for i, line in enumerate(infection_lines[1:]):
        parse_result = parse(line)
        if parse_result:
            units, hit_points, attack, attack_type, initiative, weak, immune = parse_result
            group = Group(units, hit_points, attack, attack_type, initiative, type=1,
                          weak, immune)
            groups.append(group)

    print(len(immune_system))
    print(len(infection))

    tick(immune_sytem, infection)


if __name__ == "__main__":
    main()
