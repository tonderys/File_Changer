import unittest
import shutil
import os
from File_Finder import *

directory = 'testDirectory'

class File_finder_test(unittest.TestCase):
    def setUp(self):
       if os.path.exists(directory):
           shutil.rmtree(directory) 
#   def tearDown(self):
#       self.setUp()
    
    def test_file_not_found(self):
        os.mkdir(directory) 
        self.assertFalse(File_Finder(directory,'.txt').found_any())
  
    def test_file_found(self):
        os.mkdir(directory)
        open("%s/file.txt"%directory,"w").close()
        self.assertTrue(File_Finder(directory, ".txt").found_any())

if __name__ == "__main__":
    unittest.main()
