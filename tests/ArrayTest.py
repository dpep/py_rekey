#!/usr/bin/env python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey import rekey


class ArrayTest(unittest.TestCase):
    def test_basic(self):
        data = [
            {'k': 'a', 'v': 2},
            {'k': 'b', 'v': 4},
            {'k': 'c', 'v': 6},
        ]
        self.assertEquals(
            {'a': 2, 'b': 4, 'c': 6},
            rekey(data, 'k', 'v')
        )

        data = [
            {'k': 1},
            {'k': 2},
            {'k': 3},
        ]
        self.assertEquals(
            [1, 2, 3],
            rekey(data, None, 'k')
        )

    def test_indicies(self):
        data = [
            [0, 1, 2],
            [5, 6, 7],
        ]
        self.assertEquals(
            [0, 5],
            rekey(data, None, 0)
        )


    def test_builtin_fn(self):
        data = [
            [1],
            [1, 2],
            [1, 2, 3],
        ]
        self.assertEquals(
            [1, 2, 3],
            rekey(data, None, len)
        )


    def test_fn(self):
        def double(val):
            return val * 2

        self.assertEquals(
            [2, 4, 6],
            rekey([1, 2, 3], None, double)
        )


    def test_lamba(self):
        self.assertEquals(
            [2, 4, 6],
            rekey([1, 2, 3], None, lambda x: x * 2)
        )


if __name__ == '__main__':
    unittest.main()
