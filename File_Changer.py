import shutil
import sys
import re


class File_Changer:
    def __init__(self, filename, searched_phrase, old_phrase, new_phrase):
        self.filename = filename
        self.searched_phrase = searched_phrase
        self.old_phrase = old_phrase
        self.new_phrase = new_phrase
        self.change_file()

    def file_match(self):
        filename = self.filename
        searched_phrase = self.searched_phrase
        old_phrase = self.old_phrase
        source = open(filename)
        for line in source:
            if re.search(searched_phrase, line) and re.search(old_phrase, line) and len(line.strip())==4:
                print "zmiana pliku "+filename
                source.close()
                return True
        else:
            print "w pliku "+filename+" nie znaleziono szukanej frazy"
            source.close()
            return False
    
    def change_file(self):
        filename = self.filename
        searched_phrase = self.searched_phrase
        old_phrase = self.old_phrase
        new_phrase = self.new_phrase
        try:
            if (self.file_match() == True):
                shutil.move( filename, filename+"~")
                new_file = open (filename, "w")
                source = open (filename+"~", "r")
                   
                for line in source:
                    if re.search(searched_phrase, line) and re.search(old_phrase, line) and len(line.strip())==4:
                        new_file.write(line.replace(old_phrase,new_phrase))
                    else:
                        new_file.write(line)
                new_file.close()
                source.close()
        except (IOError):
            print "no such file, or cant open: "+sys.argv[1]

if __name__ == "__main__":
    changer = File_Changer(sys.argv[1], "[0-4]{4}", "4", "2")
    
