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



if __name__ == '__main__':
    unittest.main()
