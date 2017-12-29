#!/usr/bin/env python

import datetime
import os
import subprocess
import time
from typing import List

import matplotlib.pyplot as plt
import seaborn as sns


def create_timings() -> List[int]:
    cwd = os.getcwd()
    os.chdir('..')
    timings = list()
    for day in range(1, 26):
        start = time.time()
        subprocess.run(['python', 'd{:02}.py'.format(day)], stdout=subprocess.DEVNULL)
        elapsed_time = time.time() - start
        timings.append(elapsed_time)
    os.chdir(cwd)
    return timings


def read_timings() -> List[float]:
    try:
        with open('timings.txt', 'r') as f:
            input_str = f.read()
            lines = input_str.split('\n')
            print('Using timings from {}'.format(lines[0]))
            timings = lines[-1].split(',')
            timings = [float(x.strip('[ ]')) for x in timings]
            return timings
    except:
        timings = create_timings()
        write_timings(timings)
        return timings


def write_timings(timings: List[int]) -> None:
    with open('timings.txt', 'w') as f:
        print('Writing timings to timings.txt')
        f.write(str(datetime.datetime.now()) + '\n')
        f.write(str(timings))


def create_plot(xs: List[str], slocs: List[int], runtimes: List[int]) -> None:
    sns.set_style('dark', {'axes.facecolor': 'eeeeee', 'axes.labelcolor': '555555',
                           'xtick.color':    '555555', 'ytick.color': '555555'})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    axes = [ax, ax.twinx()]

    axes[0].set_yscale('linear')
    axes[-1].set_yscale('log')

    axes[0].set_xlabel("Day")
    axes[0].set_ylabel("SLOC")
    axes[-1].set_ylabel("Runtime in secs")

    sns.barplot(xs, slocs, ax=axes[0], alpha=0.6)
    p1, = axes[-1].plot(xs, runtimes, 'o-', lw=1.5, color='#080808', label='Runtime')

    lns = [p1]
    ax.legend(handles=lns, loc='upper left')
    plt.savefig('img/sloc_runtime.png', dpi=fig.dpi, bbox_inches='tight')
    plt.show()


def main():
    xticks = ['{:02}'.format(x) for x in range(1, 26)]
    # Values taken from CLI program SLOCCount
    sloc_counts = [34, 24, 60, 28, 38, 46, 101, 40, 38, 48, 33, 19, 33, 33, 34,
                   31, 26, 106, 66, 51, 45, 68, 40, 43, 66]

    if os.path.isfile('timings.txt'):
        timings = read_timings()
    else:
        timings = create_timings()
        write_timings(timings)
    create_plot(xticks, sloc_counts, timings)


if __name__ == '__main__':
    main()

# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4
