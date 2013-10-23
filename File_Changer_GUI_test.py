import unittest
import shutil
import os
import os.path
from File_Changer_GUI import *

testdir = "testingDirectory"

class File_Changer_GUI_test(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        os.mkdir(testdir)
        for i in range(0,9):
            tmp_path = testdir+"/"+str(i)
            os.mkdir(tmp_path)
            testFile = open("%s/%d.sm" % (tmp_path, i), "w")
            tmp = (i%2)*4
            testFile.write("%d%d%d%d" % (tmp, tmp, tmp, tmp) )
            testFile.close()

    def tearDown(self):
        if os.path.exists(testdir):
            shutil.rmtree(testdir)

    def test_GUI_normal_scenario(self):
        gui = File_Changer_GUI()
        
        gui.search_for_files_and_put_to_list()
        self.assertEqual(gui.files_list.size(), 9)

        gui.change_files()
        self.assertEqual(gui.changed_files_list.size(), 4)
        self.assertEqual(gui.unchanged_files_list.size(), 5)
    
        for i in range(0,9):
            if i%2 == 0:
                self.assertFalse(os.path.exists("%s/%d/%d.sm~" % (testdir,i,i)))
            else:
                self.assertTrue(os.path.exists("%s/%d/%d.sm~" % (testdir,i,i)))

if __name__ == "__main__":
    unittest.main()
