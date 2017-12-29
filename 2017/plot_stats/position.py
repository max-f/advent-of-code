#!/usr/bin/env python

from typing import List, Tuple

import bs4
import matplotlib.pyplot as plt
import requests
import seaborn as sns


def get_personal_stats() -> Tuple[List[int], List[int]]:
    # Possibly automate OAuth in the future (python-oauth2?)
    #
    # Until then select whole table at http://adventofcode.com/2017/leaderboard/self
    # and use something like the following:
    # xclip -o | tail -n +3 | awk '{ print $3 }'  for part one ranks
    # xclip -o | tail -n +3 | awk '{ print $6 }'  for part two ranks
    part_one = list(reversed([2037, 2523, 900, 914, 567, 561, 900, 1243, 883, 2084, 810, 609,
                              1700, 825, 5124, 2363, 2381, 2245, 3312, 10358, 16760, 18710, 17060,
                              21869, 24523]))

    part_two = list(reversed([1760, 2476, 719, 872, 539, 907, 955, 1398, 857, 1408, 935, 735,
                              1468, 595, 4840, 2075, 2304, 2208, 6409, 9985, 16007, 17346,
                              12948, 18976, 20824]))
    return part_one, part_two


def get_total_numbers() -> Tuple[List[int], List[int]]:
    webpage = requests.get('http://adventofcode.com/2017/stats')
    soup = bs4.BeautifulSoup(webpage.content, 'html.parser')
    ankers_silver = soup.find_all('span', class_='stats-firstonly')[2::2]
    ankers_gold = soup.find_all('span', class_='stats-both')[2::2]
    part_two_total = [int(x.get_text()) for x in ankers_gold]
    part_one_total = [part_two_total[i] + int(x.get_text()) for i, x in enumerate(ankers_silver)]

    part_one_total = list(reversed(part_one_total))
    part_two_total = list(reversed(part_two_total))
    return part_one_total, part_two_total


def create_plot(xticks: List[str], p1_total: List[int], p1_personal: List[int],
                p2_total: List[int], p2_personal: List[int]) -> None:
    sns.set_style('darkgrid', {'axes.facecolor': 'eeeeee', 'axes.labelcolor': '555555',
                               'xtick.color':    '555555', 'ytick.color': '555555'})

    fig = plt.figure()
    ax = fig.add_subplot(111)

    #  Total
    plt.fill_between(xticks, p1_total, alpha=0.2)
    l1, = plt.plot(xticks, p1_total, label='part 1 (total)', lw=1.2)

    plt.fill_between(xticks, p2_total, alpha=0.2)
    l2, = plt.plot(xticks, p2_total, label='part 2 (total)', lw=1.2)

    # Personal
    l3, = plt.plot(xticks, p1_personal, 'o-', label='part 1', lw=1.2)
    l4, = plt.plot(xticks, p2_personal, 'o-', label='part 2', lw=1.2)

    # legend
    lns = [l1, l2, l3, l4]
    ax.legend(handles=lns, loc='best')

    # plt.title("Ranking", loc='left')
    plt.xlabel('Day')
    plt.ylabel('Participants/Position')
    plt.savefig('ranking.png', dpi=fig.dpi, bbox_inches='tight')


def main():
    xticks = ['{:02}'.format(x) for x in range(1, 26)]
    p1_total, p2_total = get_total_numbers()
    p1_personal, p2_personal = get_personal_stats()
    create_plot(xticks, p1_total, p1_personal, p2_total, p2_personal)


if __name__ == '__main__':
    main()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4
