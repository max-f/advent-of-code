#!/usr/bin/env python

from utils import utils


def scan_polymers(text_list):
    changed = True
    while changed:
        changed = False
        for i, c in enumerate(text_list):
            if c.isupper():
                if i > 0 and text_list[i - 1] == c.lower():
                    text_list.pop(i - 1)
                    text_list.pop(i - 1)
                    changed = True
                elif i < len(text_list) - 1 and text_list[i + 1] == c.lower():
                    text_list.pop(i)
                    text_list.pop(i)
                    changed = True
            else:
                if i > 0 and text_list[i - 1] == c.upper():
                    text_list.pop(i - 1)
                    text_list.pop(i - 1)
                    changed = True
                elif i < len(text_list) - 1 and text_list[i + 1] == c.upper():
                    text_list.pop(i)
                    text_list.pop(i)
                    changed = True
    return text_list


def replace_polymer(text, p):
    text = text.replace(p, "")
    text = text.replace(p.upper(), "")
    return len(scan_polymers(list(text)))


def main():
    text = utils.get_input(5)
    # Test
    # text = 'dabAcCaCBAcCcaDA'
    text = text.strip()
    text_list = list(text)
    # print(text_list)
    text_list = scan_polymers(text_list)
    print(f"Part 1: {len(text_list)}")

    polymers = set(text.lower())
    shortest = len(text)
    best = ""
    for p in polymers:
        cur_length = replace_polymer(text, p)
        if cur_length < shortest:
            shortest = cur_length
            best = p
    print(best)
    print(f"Part 2: {shortest}")


if __name__ == "__main__":
    main()
