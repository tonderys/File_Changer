from File_Finder import *
from File_Changer import *

finder = File_Finder(sys.argv[2])
finder.seek_for_files(sys.argv[1])

for path in finder.file_paths:
    change_file(path)