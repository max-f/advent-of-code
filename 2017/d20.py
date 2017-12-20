#!/usr/bin/env python

from utils import utils
import numpy as np


class Particle(object):
    def __init__(self, ident, p, v, a):
        self.ident = ident
        self.p = np.array([int(p[0]), int(p[1]), int(p[2])])
        self.v = np.array([int(v[0]), int(v[1]), int(v[2])])
        self.a = np.array([int(a[0]), int(a[1]), int(a[2])])
        self.tmp_p = self.p
        self.tmp_v = self.v

    def start_over(self):
        self.tmp_v = self.v
        self.tmp_p = self.p

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
                                  self.a
                                  )

    def collides(self, other_particle):
        self.start_over()
        other_particle.start_over()
        for i in range(20):
            if np.array_equal(self.p, other_particle.p):
                return True
            self.tick()
            other_particle.tick()
        return False

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

    def collided(pas):
        seen = set()
        collision = list()
        for i in pas:
            s_collision = [x for x in pas if x is not i and np.array_equal(i.p, x.p) and x not in seen]
            if s_collision:
                s_collision.append(i)
            seen |= set(s_collision)
            collision.extend(s_collision)
        return collision


    tmp_particles = list(particles)
    for i in range(200):
        collision = collided(tmp_particles)
        for pa in collision:
            tmp_particles.remove(pa)
        [t.tick() for t in tmp_particles]


    print(len(tmp_particles))




if __name__ == '__main__':
    main()
