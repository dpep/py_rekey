#!/usr/bin/env python

import os
import sys
import unittest

from collections import namedtuple

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey import rekey


class SetTest(unittest.TestCase):
    def test_basic(self):
        Point = namedtuple('Point', ['name', 'x', 'y'])  # hashable
        points = set([
            Point(name='home', x=1, y=2),
            Point(name='work', x=3, y=6)
        ])
        self.assertEquals(
            {
                'home' : 1,
                'work' : 3,
            },
            rekey(points, 'name', 'x')
        )

        self.assertEquals(
            {
                'home' : 3,
                'work' : 9,
            },
            rekey(points, 'name', lambda p: p.x * 3),
        )


if __name__ == '__main__':
    unittest.main()
