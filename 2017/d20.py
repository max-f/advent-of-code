#!/usr/bin/env python

from utils import utils
import numpy as np


class Particle(object):

    def __init__(self, ident, p, v, a):
        self.ident = ident
        self.p = np.array([int(p[0]), int(p[1]), int(p[2])])
        self.v = np.array([int(v[0]), int(v[1]), int(v[2])])
        self.a = np.array([int(a[0]), int(a[1]), int(a[2])])

    def tick(self):
        self.v += self.a
        self.p += self.v

    def total_acceleration(self):
        return np.sum(np.absolute(self.a))

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                        self.ident,
                                        self.p,
                                        self.v,
                                        self.a)


def main():
    particles = []
    lines = [x for x in utils.get_input(20).strip().split('\n')]
    for i, particle in enumerate(lines):
        p, v, a = [x.strip() for x in particle.split('>,')]
        p = p[3:].split(',')
        v = v[3:].split(',')
        a = a[3:-1].split(',')
        particles.append(Particle(i, p, v, a))

    print(particles)
    print(sorted(particles, key=Particle.total_acceleration))

    # p1 = Particle(0, ['0', '2', '3'], ['1'] * 3, ['1'] * 3)
    # p2 = Particle(1, ['0', '2', '3'], [1] * 3, [2] * 3)
    # test = set()
    # test.add(p1)
    # print(p2 in test)
    # print(p1 is p2)

    def collided(particles_arg: list) -> list:
        seen_idcs = set()
        collision = list()
        for i, particle in enumerate(particles_arg):
            s_collision = [j for j, x in enumerate(particles_arg) if x is not
                           particle and np.array_equal(particle.p, x.p) and
                           j not in seen_idcs]
            if s_collision:
                s_collision.append(i)
            seen_idcs |= set(s_collision)
            collision.extend(s_collision)
        return collision

    tmp_particles = list(particles)
    for i in range(200):
        collision = collided(tmp_particles)
        for idx in reversed(sorted(collision)):
            del tmp_particles[idx]
        [t.tick() for t in tmp_particles]

    print(len(tmp_particles))


if __name__ == '__main__':
    main()
