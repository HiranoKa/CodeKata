from fizz_buzz import FizzBuzz

__author__ = 'le-user'
# -*- coding: utf-8 -*-

import unittest

class MyTestCase(unittest.TestCase):
     def test_something(self):
        FizzBuzz(20)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
