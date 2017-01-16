#!/usr/bin/python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
import rekey

class ArrayTest(unittest.TestCase):
    # def setUp(self):
    #     self.data =


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

        # self.assertFalse(LengthCacheable.list())

        # res = LengthCacheable.get('abc')
        # self.assertEquals(res, 3)

        # self.assertEquals(len(LengthCacheable.list()), 1)

        # res = LengthCacheable.get('z')
        # self.assertEquals(res, 1)

        # res = LengthCacheable.multiget(['abc', 'z'])
        # self.assertEquals(res, { 'abc' : 3, 'z' : 1 })


if __name__ == '__main__':
    unittest.main()



# def ran(val):
#     return 3

# data = [
#     {
#         'a': 1,
#     },
#     {
#         'a': 2,
#     },
# ]

# print data.rekey(None, 'ran')
