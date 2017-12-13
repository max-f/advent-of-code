#!/usr/bin/env python

from utils import utils


def read_firewall(day: int) -> dict:
    firewall = dict()
    input_str = utils.get_input(day)
    for line in input_str.rstrip().split('\n'):
        depth, scanner_range = line.split(': ')
        firewall[int(depth)] = int(scanner_range)
    return firewall


def part_one(day: int) -> None:
    firewall = read_firewall(day)
    result = 0
    for second in firewall.keys():
        scanner_range = firewall[second]
        if second % (2 * (scanner_range - 1)) == 0:
            result += second * firewall[second]
    print(result)


def part_two(day: int) -> None:
    firewall = read_firewall(day)
    delay = 0
    while not check_delay(firewall, delay):
        delay += 1
    print(delay)


def check_delay(firewall: dict, delay: int) -> bool:
    for second in firewall.keys():
        scanner_range = firewall[second]
        if (second + delay) % (2 * (scanner_range - 1)) == 0:
            return False
    return True


def main():
    part_one(13)
    part_two(13)


if __name__ == '__main__':
    main()
