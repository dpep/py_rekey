#!/usr/bin/env python

import os
import sys
import unittest

from collections import namedtuple

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey import rekey


class CornerCasesTest(unittest.TestCase):
    def test_empty_handles(self):
        data = {
            'a' : [1, 2],
            'b' : [3, 4],
        }

        self.assertEquals(data, rekey(data, None))
        self.assertEquals(data, rekey(data, None, None))


    def test_empty(self):
        self.assertEquals({}, rekey({}, 'k'))
        self.assertEquals({}, rekey({}, 'k', 'v'))
        self.assertEquals({}, rekey({}, None, 'v'))

        self.assertEquals({}, rekey([], 'k'))
        self.assertEquals({}, rekey([], 'k', 'v'))
        self.assertEquals([], rekey([], None, 'v'))


    def test_noop(self):
        data = [1, 2, 3]
        self.assertEquals(data, rekey(data, None))
        self.assertEquals(data, rekey(data, None, None))


    def test_null(self):
        self.assertEquals(None, rekey(None, None))
        self.assertEquals(None, rekey(None, 123))

        data = {
            None : [1, 2],
            'b' : [3, 4],
            'c' : None,
        }
        self.assertEquals(
            {
                None : 2,
                'b' : 4,
                'c' : None,
            },
            rekey(data, None, 1)
        )
        self.assertEquals(
            {
                1 : 2,
                3 : 4,
                None : None,
            },
            rekey(data, 0, 1)
        )


    def test_cast(self):
        # iterable but not a list
        class ListLike():
            def __iter__(self):
                data = [
                    { 'k' : 1, 'v' : 2},
                    { 'k' : 2, 'v' : 4},
                ]
                for v in data:
                    yield v

        self.assertEquals(
            {
                1 : 2,
                2 : 4,
            },
            rekey(ListLike(), 'k', 'v')
        )



if __name__ == '__main__':
    unittest.main()
