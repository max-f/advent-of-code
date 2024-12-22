#!/usr/bin/env python

from collections import defaultdict

from utils import utils

FACTORS = {"MULT1": 64, "MULT2": 2048, "DIV": 32, "PRUNE": 16777216}


def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret % FACTORS["PRUNE"]


def one_step(n: int) -> int:
    n = prune(mix(n, n * FACTORS["MULT1"]))
    n = prune(mix(n, n // FACTORS["DIV"]))
    return prune(mix(n, n * FACTORS["MULT2"]))


def part1(secrets: list[int]) -> int:
    for _ in range(2000):
        secrets = tuple(map(one_step, secrets))
    return sum(secrets)


def calculate_deltas(secret: int) -> list[tuple[int, int]]:
    curr_price = secret % 10
    deltas = []
    for _ in range(2000):
        secret = one_step(secret)
        new_price = secret % 10
        deltas.append((new_price - curr_price, new_price))
        curr_price = new_price
    return deltas


def part2(secrets: list[int]) -> int:
    roi_patterns = defaultdict(int)
    for secret in secrets:
        deltas = calculate_deltas(secret)
        added = set()
        for idx in range(len(deltas) - 4):
            pat = tuple(d[0] for d in deltas[idx : idx + 4])
            if pat not in added:
                roi_patterns[tuple(pat)] += deltas[idx + 3][1]
                added.add(pat)

    return max(roi_patterns.values())


def main() -> None:
    input_txt = utils.get_input(22)
    initial_secrets = utils.ints(input_txt)
    initial_secrets2 = initial_secrets.copy()

    print(f"Part1: {part1(initial_secrets)}")
    print(f"Part2: {part2(initial_secrets2)}")


if __name__ == "__main__":
    main()
