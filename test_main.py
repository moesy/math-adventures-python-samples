import unittest
import sys


class TestEnvironment(unittest.TestCase):

    def test_python_version(self):
        self.assertEqual(sys.version_info[0], 3)


if __name__ == '__main__':
    unittest.main()
