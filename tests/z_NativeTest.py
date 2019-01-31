#!/usr/bin/env python

"""
Make native list / dict / set rekeyable.

Warning: This test must run last because it's modification
of builtin types will effect other tests, hence the z_ prefix
in it's file name.
"""

import os
import sys
import unittest

from collections import namedtuple

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
import rekey.native


class NativeTest(unittest.TestCase):
    def test_list(self):
        people = [
          { 'id' : 1, 'name' : 'alice', 'age' : 30},
          { 'id' : 2, 'name' : 'bob', 'age' : 24},
          { 'id' : 3, 'name' : 'charlie', 'age' : 88},
        ]
        self.assertEquals(
            {
                1 : 'alice',
                2 : 'bob',
                3 : 'charlie',
            },
            people.rekey('id', 'name'),
        )


    def test_dict(self):
        coordinates = {
            'home' : {'x' : 1, 'y' : 2},
            'work' : {'x' : 3, 'y' : 6},
        }
        self.assertEquals(
            {
                1 : 2,
                3 : 6,
            },
            coordinates.rekey('x', 'y')
        )


    def test_set(self):
        Point = namedtuple('Point', ['x', 'y'])  # hashable
        points = set([
            Point(x=1, y=2),
            Point(x=3, y=6)
        ])
        self.assertEquals(
            {
                2 : 1,
                6 : 3,
            },
            points.rekey('y', 'x')
        )


    def test_tuple(self):
        people = (
          { 'id' : 1, 'name' : 'alice', 'age' : 30},
          { 'id' : 2, 'name' : 'bob', 'age' : 24},
          { 'id' : 3, 'name' : 'charlie', 'age' : 88},
        )

        self.assertEquals(
            {
                1 : 'alice',
                2 : 'bob',
                3 : 'charlie',
            },
            people.rekey('id', 'name'),
        )



if __name__ == '__main__':
    unittest.main()
