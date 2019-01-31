#!/usr/bin/env python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey import rekey


class ArrayTest(unittest.TestCase):
    def test_basic(self):
        data = {
            'a': {'k': 1, 'v': 2},
            'b': {'k': 3, 'v': 4},
            'c': {'k': 5, 'v': 6},
        }

        self.assertEquals(
            rekey(data, 'k', 'v'),
            {
                1: 2,
                3: 4,
                5: 6,
            }
        )

        self.assertEquals(
            rekey(data, None, 'v'),
            {
                'a': 2,
                'b': 4,
                'c': 6,
            }
        )


    def test_indicies(self):
        data = {
            'a': [0, 1],
            'b': [5, 6],
        }

        self.assertEquals(
            rekey(data, 0, max),
            {
                0 : 1,
                5 : 6
            }
        )


if __name__ == '__main__':
    unittest.main()
