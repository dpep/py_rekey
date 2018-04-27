#!/usr/bin/python

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
        data = {
            None : [1, 2],
            'b' : [3, 4],
            'c' : [None, 5]
        }
        self.assertEquals(
            {
                None : 2,
                'b' : 4,
                'c' : 5,
            },
            data.rekey(None, 1)
        )
        self.assertEquals(
            {
                1 : 2,
                3 : 4,
                None : 5
            },
            data.rekey(0, 1)
        )



if __name__ == '__main__':
    unittest.main()
