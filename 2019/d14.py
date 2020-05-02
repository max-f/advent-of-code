#!/usr/bin/env python

from collections import defaultdict

from utils.utils import get_input
import re
import math

WANTED = "FUEL"
MAX_ORE = 10 ** 12

chem_store = defaultdict(int)
reactions_inverted = {}


def how_often_reaction(required_amount, resulting_amount):
    return math.ceil(required_amount / resulting_amount)


def backtrack(chem, n):
    if chem == "ORE":
        chem_store[chem] += n
        return
    elif chem_store[chem] >= n:
        chem_store[chem] -= n
        return
    else:
        # Find chem in reactions inverted and get necessary amounts of
        # reactants through recursion
        producing_reactions = {
            k: v for k, v in reactions_inverted.items() if k[-1] == chem
        }

        if len(producing_reactions) != 1:
            raise ValueError(
                f"There are multiple reactions producing the wanted chem {chem}"
            )
        # Subtract already present amount from chem_store
        still_required = n - chem_store[chem]
        chem_store[chem] = 0
        reactants = [
            (number, r) for number, r in list(producing_reactions.values())[0][1:]
        ]
        resulting_amount = list(producing_reactions.keys())[0][0]
        how_often = how_often_reaction(still_required, resulting_amount)
        chem_store[chem] += (resulting_amount * how_often) - still_required

        for reactant in reactants:
            reactant_amount = reactant[0]
            reactant_chem = reactant[-1]
            backtrack(reactant_chem, reactant_amount * how_often)


def part_1():
    backtrack(WANTED, 1)
    print(f"Part 1: {chem_store['ORE']}")


# Try to find amount of ORE with binary search
def part_2(lower_fuel, upper_fuel):
    global chem_store

    mid_fuel = (lower_fuel + upper_fuel) // 2
    backtrack(WANTED, mid_fuel)

    if upper_fuel - lower_fuel <= 1:
        print(f"Part 2: {mid_fuel}")
        return

    if chem_store["ORE"] > MAX_ORE:
        chem_store = defaultdict(int)
        part_2(lower_fuel, mid_fuel)
    elif chem_store["ORE"] < MAX_ORE:
        chem_store = defaultdict(int)
        part_2(mid_fuel, upper_fuel)


def main():
    input_txt = get_input(14)
    reactions = {}
    global reactions_inverted

    chemical_re = re.compile(r"(\d+) (\w+)")
    for id, line in enumerate(input_txt.strip().split("\n")):
        pre, post = line.split("=>")
        pre_chemicals = chemical_re.findall(pre)
        post = chemical_re.findall(post)

        if len(post) > 1:
            raise ValueError(f"Multiple chemicals as reaction product? -> {post}")

        out_number, out_name = post[0]
        in_chemicals = [(int(number), name) for number, name in pre_chemicals]
        reactions[tuple([id]) + tuple(in_chemicals)] = (int(out_number), out_name)
        reactions_inverted = {v: k for k, v in reactions.items()}

    part_1()
    part_2(1, 10 ** 11)


if __name__ == "__main__":
    main()
