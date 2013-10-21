import unittest
import shutil
import os
from File_Finder import *

directory = 'testDirectory'

class File_finder_test(unittest.TestCase):
    def remove_test_directory(self): 
        if os.path.exists(directory):
            shutil.rmtree(directory) 

    def setUp(self):
        self.remove_test_directory()

    def tearDown(self):
        self.remove_test_directory()
    
    def test_file_not_found(self):
        os.mkdir(directory) 
        self.assertEqual(File_Finder(directory, ".txt").output_code, 2)
  
    def test_file_found(self):
        os.mkdir(directory)
        open("%s/file.txt" % directory,"w").close()
        self.assertEqual(File_Finder(directory, ".txt").output_code, 1)
    
    def test_invalid_path(self):
        self.assertEqual(File_Finder(directory, ".txt").output_code, 3)

if __name__ == "__main__":
    unittest.main()
