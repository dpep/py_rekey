#!/usr/bin/env python

import os
import sys
import unittest


sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from rekey import rekey


class ErrorsTest(unittest.TestCase):
    def test_wrong_type(self):
        class Foo(): pass

        with self.assertRaises(TypeError):
            rekey(Foo(), 'foo')



if __name__ == '__main__':
    unittest.main()
