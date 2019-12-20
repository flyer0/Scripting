#!/usr/bin/env python
#
# demonstrates an composition relation between 2 classes
#

class Line(object):
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1

    def __call__(self, x):
        return self.c0 + self.c1*x

class Parabola(object):
    def __init__(self, c0, c1, c2):
        self.line = Line(c0, c1)
        self.c2 = c2

    def __call__(self, x):
        return self.line(x) + self.c2*x**2

def table(func, s, e, n):
    return [(x, func(x))
         for x in [s+i*(e-s)/n
              for i in range(n+1)]]

p = Parabola(0., 1., 1.)
print(table(p, 0., 1., 10))

import sys

print(sys.path)