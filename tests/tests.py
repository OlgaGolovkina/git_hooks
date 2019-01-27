import unittest
import sys, os
from main import *


sys.path.append(os.getcwd())


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt(self):
        self.assertEqual(nitro_salt(1000), 10)


if __name__ == '__main__':
    unittest.main()
