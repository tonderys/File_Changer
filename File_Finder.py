import os
import sys

class File_Finder:
    file_paths = [] 
    wanted_extension = ""

    def __init__(self, wanted):
        self.wanted_extension = wanted

    def is_searched_type(self, file_path):
       if os.path.isfile(file_path):
           if os.path.splitext(file_path)[1] == self.wanted_extension:
               return True
           else:
               return False
    
    def update_searched_file_list(self, path):
       for name in sorted(os.listdir(path)):
           full_path = os.path.join(path, name)
           if self.is_searched_type(full_path) == True:
               self.file_paths.append(full_path)
    
    def seek_for_files(self, path):
       self.update_searched_file_list(path)
       for name in sorted(os.listdir(path)):
           full_path = os.path.join(path, name)
           if os.path.isdir(full_path):
               self.seek_for_files(full_path)

    def print_file_paths(self):
        for path in self.file_paths:
            print path
