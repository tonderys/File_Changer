import shutil
import sys
import re

def file_match(filename):
    source = open(filename)
    for line in source:
        if re.search("[0-4]{4}", line) and re.search("[4]{1}", line) and len(line.strip())==4:
            print "zmiana pliku "+filename
            source.close()
            return True
    else:
        print "w pliku "+filename+" nie znaleziono szukanej frazy"
        source.close()
        return False

def change_file(filename):
    try:
        if (file_match(filename) == True):
            shutil.move( filename, filename+"~")
            new_file = open (filename, "w")
            source = open (filename+"~", "r")
               
            for line in source:
                if re.search("[0-4]{4}", line) and re.search("[4]{1}", line) and len(line.strip())==4:
                    new_file.write(line.replace("4","2"))
                else:
                    new_file.write(line)
            new_file.close()
            source.close()
    except (IOError):
        print "no such file, or cant open: "+sys.argv[1]

