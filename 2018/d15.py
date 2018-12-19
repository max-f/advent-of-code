#!/usr/bin/env python

from utils import utils
from collections import deque

Map = None


class Field():
    def __init__(self, x, y, field_type, actor=None):
        self.x = x
        self.y = y
        self.field_type = field_type
        self.actor = actor

    def is_wall(self):
        return self.field_type == '#'

    def adjacent(self):
        adjacent = []
        if self.x != 0:
            adjacent.append((-1, 0))
        if self.x != len(Map) - 1:
            adjacent.append((0, 1))
        if self.y != 0:
            adjacent.append((0, -1))
        if self.x != len(Map[0]) - 1:
            adjacent.append((0, 1))
        return [Map[self.x + i][self.y + j] for i, j in adjacent]

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Actor():
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hitpoints = 200
        self.team = team

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y

    def move(self, actors):
        targets = [a for a in actors if a.team != self.team]
        if not targets:
            return None
        pass

    def find_move_with_bfs(self, possibilities):
        start = Map[self.x][self.y]
        to_check = deque([(start, 0)])
        # TODO
        distance_info = {}
        visited = set()
        # TODO
        occupied = set()

        while to_check:
            field, dist = to_check.popleft()
            x, y = field.x, field.y
            for adjacent in field.adjacent:
                # Field is start field or already occupied
                if adjacent == self or adjacent in occupied:
                    continue
                # TODO: Update distance info if smaller distance is found

                # Field was already visited
                if adjacent in visited:
                    continue
                # Field not in queue yet -> add
                if not any(adjacent == check[0] for check in to_check):
                    to_check.append((adjacent, dist + 1))
            visited.add(field)

            # TODO: find target fields with smallest distance

            # TODO: backtrack to get next position to move to
        return None


def tick(actors):
    for actor in actors:
        continue
    pass


def read_in_map(data):
    global Map
    map_size_y = len(data)
    map_size_x = len(data[0])
    actors = []
    Map = [[None for y in range(map_size_y)] for x in range(map_size_x)]

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in ['G', 'E']:
                actor = Actor(x, y, c)
                actors.append(actor)
                field = Field(x, y, '.', actor)
            else:
                field = Field(x, y, c)
            Map[x][y] = field

    print('wtf this is awkward')
    return Map, actors


def main():
    data = utils.get_input(42).split("\n")

    Map, actors = read_in_map(data)
    print(actors)


if __name__ == "__main__":
    main()
