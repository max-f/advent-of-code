#!/usr/bin/env python

from utils import utils


def main():
    reach = 824501
    # reach = 92510
    # reach = 59414
    # reach = 18
    recipes = [3, 7]
    worker_one = 0
    worker_two = 1
    idx = -1
    look_at_steps = 6
    look_at = 1

    while True:
        score_new_recipe = recipes[worker_one] + recipes[worker_two]
        if score_new_recipe >= 10:
            recipes.append(1)
        recipes.append(score_new_recipe % 10)
        new_worker_one_total = 1 + recipes[worker_one] + worker_one
        new_worker_two_total = 1 + recipes[worker_two] + worker_two
        worker_one = new_worker_one_total % len(recipes)
        worker_two = new_worker_two_total % len(recipes)
        # Part 1
        # if len(recipes) >= reach + 10:
        #    break
        if len(recipes) > look_at_steps * look_at:
            if len(recipes) >= look_at_steps * 2:
                last_numbers_str = "".join(map(str, recipes[-(look_at_steps + 5) :]))
            else:
                last_numbers_str = "".join(map(str, recipes[-look_at_steps:]))
            if last_numbers_str.find(str(reach)) >= 0:
                complete_number_str = "".join(map(str, recipes))
                idx = complete_number_str.find(str(reach))
            look_at += 1
        if idx > 0:
            break

    # Part 1
    # if len(recipes) % 2 == 0 and (reach + 10) % 2 != 0:
    #    print('Part 1', ''.join(map(str,recipes[-11:-1])))
    # else:
    #    print('Part 1', ''.join(map(str,recipes[-10:])))
    print("Part 2", idx)


if __name__ == "__main__":
    main()
