import unittest
import sys
import os
from main import nitro_salt


sys.path.append(os.getcwd())


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt(self):
        self.assertEqual(nitro_salt(1000), 10)


if __name__ == '__main__':
    unittest.main()
