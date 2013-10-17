import unittest
import os
import os.path
import shutil
from File_Changer import *

filename = "testTmpFile"

class File_changer_test(unittest.TestCase):
    def setUp(self):
        if os.path.exists(filename):
            os.remove(filename)
    
    def tearDown(self):
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(filename+"~"):
            os.remove(filename+"~")

    def test_no_input_file(self):
        self.assertEqual(File_Changer(filename, "[0-4]", 4, "4", "2").output_code, 3)
        self.assertFalse(os.path.exists(filename+"~"))

    def test_pattern_not_found(self):
        output = open(filename, "w")
        output.write("0000")
        output.close()
        
        self.assertEqual(File_Changer(filename, "[0-4]", 4, "4", "2").output_code, 2)
        self.assertFalse(os.path.exists(filename+"~"))

    def test_single_line_with_pattern(self):
        output = open(filename, "w")
        output.write("4444")
        output.close()
        
        self.assertEqual(File_Changer(filename, "[0-4]", 4, "4", "2").output_code, 1)
        self.assertTrue(os.path.exists(filename+"~"))

    def test_correctly_executed_program(self):
        output = open(filename, "w")
        output.write("0000\n01234\na324\n0004\n4444\n")
        output.close()
 
        self.assertEqual(File_Changer(filename, "[0-4]", 4, "4", "2").output_code, 1)

        output = open(filename, "r")
        self.assertEqual (output.read(), "0000\n01234\na324\n0002\n2222\n")
        output.close()

if __name__ == "__main__":
    unittest.main()

