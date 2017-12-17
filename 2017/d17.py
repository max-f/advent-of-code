#!/usr/bin/env python


def part_one() -> None:
    buffer = [0]
    idx = 0
    for i in range(1, 2018):
        idx = step(buffer, idx)
        buffer.insert(idx + 1, i)
        idx += 1
    print('Part 1: ', buffer[buffer.index(2017) + 1])


def step(buffer: list, start: int) -> int:
    steps = 359
    return (steps + start) % len(buffer)


def part_two() -> None:
    steps = 359
    idx = 0
    result = 0
    for i in range(1, 50 * (10 ** 6) + 1):
        idx = (steps + idx) % i
        if idx == 0:
            result = i
        idx += 1
    print('Part 2: ', result)

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
