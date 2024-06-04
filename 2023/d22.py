#!/usr/bin/env python

from collections import deque

from utils import utils

"""
Code for https://adventofcode.com/2023/day/22
"""


def blocks_overlap(block1: list[int], block2: list[int]) -> bool:
    return max(block1[0], block2[0]) <= min(block1[3], block2[3]) and max(block1[1], block2[1]) <= min(block1[4],
                                                                                                       block2[4])


def setup(lines: list[str]) -> tuple[list[list[int]], dict[int, set[int]], dict[int, set[int]]]:
    bricks = [list(map(int, line.replace('~', ",").split(","))) for line in lines]
    bricks.sort(key=lambda x: x[2])

    # move bricks down
    for idx, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:idx]:
            if blocks_overlap(brick, check):
                # there is an overlap between a block down below and this one - we need to adjust max_z
                max_z = max(check[5] + 1, max_z)

        # Adjust z coordinates to it's "resting place"
        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    # Re-sort cause some bricks might have fallen further down than others
    bricks.sort(key=lambda x: x[2])

    # Initial idea of solving p1
    # Delete bricks one by one and test bricks further up if they would fall down - if none would then we can count that brick for part 1
    # result = 0
    # for idx, brick in enumerate(bricks):
    #     # copy new array & remove current brick from it
    #     bricks_copy = deepcopy(bricks)
    #     del bricks_copy[idx]

    #         # check if any of the next bricks would fall down
    #         bricks_with_same_z_level = [b for b in bricks_copy if b[5] == brick[5]]
    #         next_bricks = [b for b in bricks_copy[idx:] if b[2] == brick[2] + 1]
    #         if not next_bricks or any(
    #                 [blocks_overlap(support_brick, falling_brick) for support_brick in bricks_with_same_z_level for
    #                  falling_brick in next_bricks]):
    #             result += 1

    # Create dictionaries for directions of support
    a_supports_b = {i: set() for i in range(len(bricks))}
    b_supported_by_a = {i: set() for i in range(len(bricks))}

    for i, lower in enumerate(bricks):
        for j, upper in enumerate(bricks[i + 1:], start=i + 1):
            if blocks_overlap(lower, upper) and lower[5] + 1 == upper[2]:
                a_supports_b[i].add(j)
                b_supported_by_a[j].add(i)

    return bricks, a_supports_b, b_supported_by_a


def part1(bricks: list[list[int]], a_supports_b: dict[int, set[int]], b_supported_by_a: dict[int, set[int]]) -> int:
    result = 0
    for i in range(len(bricks)):
        if all(len(b_supported_by_a[j]) >= 2 for j in a_supports_b[i]):
            result += 1

    return result


def part2(bricks: list[list[int]], a_supports_b: dict[int, set[int]], b_supported_by_a: dict[int, set[int]]) -> int:
    overall_other_blocks_falling = 0
    for idx, _ in enumerate(bricks):
        q = deque(brick_idx for brick_idx in a_supports_b[idx] if len(b_supported_by_a[brick_idx]) == 1)
        falling = set(q)
        falling.add(idx)

        while q:
            brick_idx = q.popleft()
            for j in a_supports_b[brick_idx] - falling:
                if b_supported_by_a[j] <= falling:
                    q.append(j)
                    falling.add(j)
        overall_other_blocks_falling += len(falling) - 1

    return overall_other_blocks_falling


def main():
    input_txt = utils.get_input(22).strip()
    lines = input_txt.split("\n")
    bricks, a_supports_b, b_supported_by_a = setup(lines)

    print(f"Part 1: {part1(bricks, a_supports_b, b_supported_by_a)}")
    print(f"Part 2: {part2(bricks, a_supports_b, b_supported_by_a)}")


if __name__ == "__main__":
    main()
