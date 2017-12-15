#!/usr/bin/env python


def to_binary(n: int) -> str:
    return '{0:b}'.format(n)


def gen_a() -> int:
    a = 634
    factor = 16807
    div = 2147483647
    while True:
        a = (a * factor) % div
        # comment if condition for part 1
        if a % 4 == 0:
            yield a


def gen_b() -> str:
    b = 301
    factor = 48271
    div = 2147483647
    while True:
        b = (b * factor) % div
        # comment if condition for part 1
        if b % 8 == 0:
            yield b


def calc_matching_pairs() -> None:
    result = 0
    ag = gen_a()
    bg = gen_b()
    for _ in range(5 * (10 ** 6)):
        a = next(ag)
        b = next(bg)
        a_bin = to_binary(a)[-16:]
        b_bin = to_binary(b)[-16:]
        if a_bin == b_bin:
            result += 1
    print(result)


def main():
    calc_matching_pairs()


if __name__ == '__main__':
    main()
