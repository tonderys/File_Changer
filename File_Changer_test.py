import unittest
import os
import os.path
import shutil
from File_Changer import *

filename = "testTmpFile"
class TestInit(unittest.TestCase):
    def setUp(self):
        if os.path.exists(filename):
            os.remove(filename)
    def tearDown(self):
        if os.path.exists(filename):
            os.remove(filename)

class correctly_executed_program(TestInit):
    def runTest (self):
        output = open(filename, "w")
        output.write("0000\n01234\na324\n0004\n4444\n")
        output.close()
 
        File_Changer(filename, "[0-4]", 4, "4", "2")

        output = open(filename, "r")
        self.failUnlessEqual (output.read(), "0000\n01234\na324\n0002\n2222\n")
        output.close()
        
        self.failUnless(os.path.exists(filename+"~"))        
        os.remove(filename+"~")

class no_input_file(TestInit):
    def runTest(self):
        self.failUnlessEqual(File_Changer(filename, "[0-4]", 4, "4", "2").output, "brak pliku/uprawnien")
        self.failIf(os.path.exists(filename+"~"))

def suite():
    suite = unittest.TestSuite()
    suite.addTest (correctly_executed_program())
    suite.addTest (no_input_file())
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)

