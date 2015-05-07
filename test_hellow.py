from Hellow import Hellow

__author__ = 'le-user'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        str = Hellow()
        self.assertEqual('HellowWorldFunc', str)


if __name__ == '__main__':
    unittest.main()
