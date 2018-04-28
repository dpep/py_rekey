#!/usr/bin/python

import os
import sys
import unittest

from collections import namedtuple

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey.rekeyable import *


class RekeyableTest(unittest.TestCase):
    def test_list(self):
        people = RekeyableList([
          { 'id' : 1, 'name' : 'alice', 'age' : 30},
          { 'id' : 2, 'name' : 'bob', 'age' : 24},
          { 'id' : 3, 'name' : 'charlie', 'age' : 88},
        ])
        self.assertEquals(
            {
                1 : 'alice',
                2 : 'bob',
                3 : 'charlie',
            },
            people.rekey('id', 'name'),
        )


    def test_dict(self):
        coordinates = RekeyableDict({
            'home' : {'x' : 1, 'y' : 2},
            'work' : {'x' : 3, 'y' : 6},
        })
        self.assertEquals(
            {
                1 : 2,
                3 : 6,
            },
            coordinates.rekey('x', 'y')
        )


    def test_set(self):
        Point = namedtuple('Point', ['name', 'x', 'y'])  # hashable
        points = RekeyableSet([
            Point(name='home', x=1, y=2),
            Point(name='work', x=3, y=6)
        ])
        self.assertEquals(
            {
                'home' : 1,
                'work' : 3,
            },
            points.rekey('name', 'x')
        )

        self.assertEquals(
            {
                'home' : 3,
                'work' : 9,
            },
            points.rekey('name', lambda p: p.x * 3),
        )


    def test_tuple(self):
        people = RekeyableTuple((
          { 'id' : 1, 'name' : 'alice', 'age' : 30},
          { 'id' : 2, 'name' : 'bob', 'age' : 24},
          { 'id' : 3, 'name' : 'charlie', 'age' : 88},
        ))

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
