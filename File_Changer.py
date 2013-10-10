import shutil
import sys
import re


class File_Changer:
    def __init__(self, filename, searched_phrase="[0-4]", line_length=4 , old_phrase="4", new_phrase="2"):
        self.output = ""
        self.filename = filename
        self.line_length = line_length
        self.searched_phrase = "%s{%s}" % (searched_phrase, line_length)
        self.old_phrase = old_phrase
        self.new_phrase = new_phrase
        self.change_file()

    def file_match(self):
        filename = self.filename
        searched_phrase = self.searched_phrase
        old_phrase = self.old_phrase
        try:
            source = open(filename)
            for line in source:
                if re.search(searched_phrase, line) and re.search(old_phrase, line) and len(line.strip())==self.line_length:
                    self.output = "zmiana pliku "+filename
                    source.close()
                    return True
            else:
                self.output = "w pliku "+filename+" nie znaleziono szukanej frazy"
                source.close()
                return False
        except IOError:
            self.output = "brak pliku/uprawnien"
    
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
                    if re.search(searched_phrase, line) and re.search(old_phrase, line) and len(line.strip())==self.line_length:
                        new_file.write(line.replace(old_phrase,new_phrase))
                    else:
                        new_file.write(line)
                new_file.close()
                source.close()
        except (IOError):
            print "no such file, or cant open: "+filename

if __name__ == "__main__":
    changer = File_Changer(sys.argv[1])
