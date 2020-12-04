#!/usr/bin/env python

import re
from utils import utils

"""
Code for https://adventofcode.com/2020/day/4
"""

VALID_EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def part1(passports: list[dict]) -> int:
    valid = 0
    for passport in passports:
        if (
            "ecl" in passport
            and "pid" in passport
            and "eyr" in passport
            and "hcl" in passport
            and "byr" in passport
            and "iyr" in passport
            and "hgt" in passport
        ):
            valid += 1
    return valid


def part2(passports: list[dict]) -> int:
    return sum(map(lambda x: is_valid_passport(x), passports))


def is_valid_passport(passport: dict) -> bool:
    global VALID_EYE_COLORS
    byr = "byr" in passport and 1920 <= int(passport["byr"]) <= 2002
    iyr = "iyr" in passport and 2010 <= int(passport["iyr"]) <= 2020
    eyr = "eyr" in passport and 2020 <= int(passport["eyr"]) <= 2030

    hgt = "hgt" in passport and validate_height(passport["hgt"])
    hcl = bool("hcl" in passport and re.match(r"^#[0-9a-f]{6}$", passport["hcl"]))
    ecl = "ecl" in passport and passport["ecl"] in VALID_EYE_COLORS
    pid = bool("pid" in passport and re.match(r"^[0-9]{9}$", passport["pid"]))
    return byr and iyr and eyr and hgt and hcl and ecl and pid


def validate_height(height: str) -> bool:
    hgt_match = re.match(r"(\d+)(cm|in)", height)
    if not hgt_match:
        return False
    if hgt_match.group(2) == "cm":
        return 150 <= int(hgt_match.group(1)) <= 193
    else:
        return 59 <= int(hgt_match.group(1)) <= 76


def main():
    input_txt = utils.get_input(4)
    passports = re.split(r"\n\s*\n", input_txt)
    all_passports = []
    regex = re.compile(r"(\w+):([\w#]+)")
    for passport in passports:
        key_values = regex.findall(passport)
        passport = {}
        for key, value in key_values:
            passport[key] = value
        all_passports.append(passport)
    print(part1(all_passports))
    print(part2(all_passports))


if __name__ == "__main__":
    main()
