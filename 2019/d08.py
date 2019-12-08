#!/usr/bin/env python

from utils import utils


def part1(input_txt) -> int:
    layer_size = 25 * 6
    layers = []
    for idx in range(0, len(input_txt), layer_size):
        layer = input_txt[idx:idx + layer_size]
        layers.append(layer)
    min_layer = min(layers, key=lambda l: sum(p == '0' for p in l))
    twos = len([x for x in min_layer if x == '2'])
    ones = len([x for x in min_layer if x == '1'])
    return twos * ones


def part2(input_txt) -> None:
    width = 25
    height = 6
    layer_size = width * height
    layers = []
    for idx in range(0, len(input_txt), layer_size):
        layer = input_txt[idx:idx + layer_size]
        layers.append(layer)

    img = []
    for i in range(layer_size):
        for layer_number in range(len(layers)):
            layer = layers[layer_number]
            pixel = layer[i]
            if pixel == '0' or pixel == '1':
                img.append(pixel)
                break
    for y in range(height):
        row = img[y * width:y * width + width]
        transformed_row = ['X' if c == '1' else ' ' for c in row]
        print(''.join(transformed_row))


def main():
    input_txt = utils.get_input(8).strip()
    p1 = part1(input_txt)
    print(f"Part 1: {p1}")

    part2(input_txt)


if __name__ == "__main__":
    main()
