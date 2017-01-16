#!/usr/bin/python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
import rekey


class ArrayTest(unittest.TestCase):
    def test_basic(self):
        data = [
            {'k': 1},
            {'k': 2},
            {'k': 3},
        ]
        self.assertEquals(
            data.rekey(None, 'k'),
            [1, 2, 3]
        )

        data = [
            {'k': 'a', 'v': 2},
            {'k': 'b', 'v': 4},
            {'k': 'c', 'v': 6},
        ]
        self.assertEquals(
            data.rekey('k', 'v'),
            {'a': 2, 'b': 4, 'c': 6}
        )


    def test_builtin_fn(self):
        data = [
            [1],
            [1, 2],
            [1, 2, 3],
        ]
        self.assertEquals(
            data.rekey(None, 'len'),
            [1, 2, 3]
        )


    def test_fn(self):
        def double(val):
            return val * 2

        self.assertEquals(
            [1, 2, 3].rekey(None, double),
            [2, 4, 6]
        )


    def test_lamba(self):
        self.assertEquals(
            [1, 2, 3].rekey(None, lambda x: x * 2),
            [2, 4, 6]
        )


if __name__ == '__main__':
    unittest.main()
