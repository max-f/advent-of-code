#!/usr/bin/env python

import itertools

from utils import utils

FIRST_CRASH = ""


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn = "left"
        self.crashed = False

    def decide_at_intersection(self):
        cart_turn_left = {"^": "<", "v": ">", ">": "^", "<": "v"}
        cart_turn_right = {"^": ">", "v": "<", ">": "v", "<": "^"}

        if self.turn == "left":
            self.direction = cart_turn_left[self.direction]
            self.turn = "straight"
        elif self.turn == "straight":
            self.turn = "right"
        else:
            self.direction = cart_turn_right[self.direction]
            self.turn = "left"

    def can_crash(self, other):
        return (
            not self.crashed
            and not other.crashed
            and self.x == other.x
            and self.y == other.y
        )

    # For sorting
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y


def tick(trackmap, carts):
    global FIRST_CRASH
    carts = sorted(carts)
    for cart in carts:
        if cart.crashed:
            continue
        move(trackmap, cart)
        for cart1, cart2 in itertools.combinations(carts, 2):
            if cart1.can_crash(cart2):
                if not FIRST_CRASH:
                    FIRST_CRASH = f"{cart1.x},{cart1.y}"
                cart1.crashed = True
                cart2.crashed = True
                print("Crash", cart1.x, cart1.y)
    return carts


def move(trackmap, cart):
    # UP
    if cart.direction == "^":
        next_c = trackmap[cart.x][cart.y - 1]
        if next_c == "+":
            cart.decide_at_intersection()
        else:
            if next_c == "\\":
                cart.direction = "<"
            elif next_c == "/":
                cart.direction = ">"
        cart.y -= 1

    # DOWN
    elif cart.direction == "v":
        next_c = trackmap[cart.x][cart.y + 1]
        if next_c == "+":
            cart.decide_at_intersection()
        else:
            if next_c == "\\":
                cart.direction = ">"
            elif next_c == "/":
                cart.direction = "<"
        cart.y += 1

    # RIGHT
    elif cart.direction == ">":
        next_c = trackmap[cart.x + 1][cart.y]
        if next_c == "+":
            cart.decide_at_intersection()
        else:
            if next_c == "\\":
                cart.direction = "v"
            elif next_c == "/":
                cart.direction = "^"
        cart.x += 1

    # LEFT
    else:
        next_c = trackmap[cart.x - 1][cart.y]
        if next_c == "+":
            cart.decide_at_intersection()
        else:
            if next_c == "\\":
                cart.direction = "^"
            elif next_c == "/":
                cart.direction = "v"
        cart.x -= 1
    return cart


def main():
    data = utils.get_input(13).split("\n")
    carts = []
    map_size_y = len(data)
    map_size_x = len(data[0])
    trackmap = [["" for y in range(map_size_y)] for x in range(map_size_x)]

    cart_to_track = {"^": "|", "v": "|", "<": "|", ">": "|"}

    for y, line in enumerate(data):
        for x, c in enumerate((line)):
            if c in ["^", "v", ">", "<"]:
                carts.append(Cart(x, y, c))
                trackmap[x][y] = cart_to_track[c]
            else:
                trackmap[x][y] = c

    last_cart = None

    while True:
        carts = [c for c in carts if not c.crashed]
        # print(len(carts))
        if len(carts) == 1:
            last_cart = carts[0]
            break
        if not carts:
            print("ERROR: All carts crashed??")
        carts = tick(trackmap, carts)
    print(f"Part 1: {FIRST_CRASH}")
    print(f"Part 2: {last_cart.x},{last_cart.y}")


if __name__ == "__main__":
    main()
