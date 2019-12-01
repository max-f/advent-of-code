#!/usr/bin/env python


def get_input(day):
    filename = "input/input{:02d}".format(day)
    with open(filename, "rt") as file_input:
        return file_input.read()
