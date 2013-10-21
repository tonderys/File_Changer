import os
import sys

class File_Finder:
    wanted_extension = ""

    def __init__(self, file_path, wanted_extension):
        self.file_paths = [] 
        if wanted_extension[0] == '.':
            self.wanted_extension = wanted_extension
        else:
            self.wanted_extension = '.'+wanted_extension
        self.seek_for_files(file_path)

    def seek_for_files(self, path):
       try:
           self.update_searched_file_list(path)
           for name in sorted(os.listdir(path)):
               full_path = os.path.join(path, name)
               if os.path.isdir(full_path):
                   self.seek_for_files(full_path)
           if not self.found_any():
               self.file_paths.append("haven't found any file with wanted extension")
              
       except OSError:
            self.file_paths.append("can't find/open file path")

    def update_searched_file_list(self, path):
        for name in sorted(os.listdir(path)):
            full_path = os.path.join(path, name)
            if self.is_searched_type(full_path) == True:
                self.file_paths.append(full_path)
    
    def is_searched_type(self, file_path):
       if os.path.isfile(file_path):
           if os.path.splitext(file_path)[1] == self.wanted_extension:
               return True
           else:
               return False
    
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
