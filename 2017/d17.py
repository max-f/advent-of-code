#!/usr/bin/env python


def part_one() -> None:
    buffer = [0]
    idx = 0
    for i in range(1, 2018):
        idx = step(buffer, idx)
        buffer.insert(idx + 1, i)
        idx += 1
    if len(buffer) == idx - 1:
        print(buffer[0])
    else:
        print(buffer[idx + 1])


def step(buffer: list, start: int) -> int:
    steps = 359
    return (steps + start) % len(buffer)


def part_two() -> None:
    steps = 359
    idx = 0
    for i in range(1, 50 * (10 ** 6) + 1):
        idx = (steps + idx) % i
        if idx == 0:
            print(i)
        idx += 1

def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
