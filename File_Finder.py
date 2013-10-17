import os
import sys

class File_Finder:
    file_paths = [] 
    wanted_extension = ""

    def __init__(self, file_path, wanted_extension):
        self.wanted_extension = wanted_extension
        self.seek_for_files(file_path)

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
    
    def found_any(self):
        if len(self.file_paths) == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    file_path = sys.argv[1]
    wanted_extension = sys.argv[2]
    finder = File_Finder(file_path, wanted_extension)
    finder.print_file_paths()
