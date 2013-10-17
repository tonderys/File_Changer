import unittest
from File_Finder import *

class File_finder_test(unittest.TestCase):
    def setUp(self):
        print "opening test"
    def tearDown(self):
        print "closing test"

    def test_case(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()
