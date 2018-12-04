#!/usr/bin/env python

from collections import defaultdict
from operator import itemgetter

from utils import utils


def parse_time(line):
    words = line.split()
    time = words[1][:-1]
    return int(time.split(":")[1])


def argmax(d, guard_id=None):
    best = None
    for k, v in d.copy().items():
        if guard_id and guard_id != k[0]:
            continue
        elif best is None or v > d[best]:
            best = k
    return best


def process_data(lines):
    total_time_per_guard = defaultdict(int)
    time_per_guard_and_minute = defaultdict(int)
    guard = None
    asleep = None
    for line in lines:
        if line:
            time = parse_time(line)
            if "begins shift" in line:
                guard = int(line.split()[3][1:])
                asleep = None
            elif "falls asleep" in line:
                asleep = time
            elif "wakes up" in line:
                for t in range(asleep, time):
                    time_per_guard_and_minute[(guard, t)] += 1
                    total_time_per_guard[guard] += 1
    return total_time_per_guard, time_per_guard_and_minute


def main():
    lines = utils.get_input(4).split("\n")
    lines.sort()

    total_time_per_guard, time_per_guard_and_minute = process_data(lines)

    most_asleep = max(total_time_per_guard.items(), key=itemgetter(1))[0]
    best_guard, best_min = argmax(time_per_guard_and_minute, most_asleep)
    print(best_guard, best_min)
    print(f"Part 1: {best_guard * best_min}")

    best_guard, best_min = argmax(time_per_guard_and_minute)
    print(best_guard, best_min)
    print(f"Part 2: {best_guard * best_min}")


if __name__ == "__main__":
    main()
