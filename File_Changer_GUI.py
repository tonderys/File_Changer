from Tkinter import *
from threading import Thread
from File_Finder import *
from File_Changer import *
from colour import Color

class File_Changer_GUI:

    def __init__(self):
        self.top_window = Tk()
        self.path_label = Label(self.top_window, text = "path")
        self.path_label.grid(column = 1, row = 2)
        self.path_entry = Entry(self.top_window, width = 30)
        self.path_entry.insert(0,"./")
        self.path_entry.grid(column = 2, row = 2, columnspan = 2)
        self.extension_label = Label(self.top_window, text = "extension")
        self.extension_label.grid(column = 1, row = 3)
        self.extension_entry = Entry(self.top_window, width = 30)
        self.extension_entry.insert(0,"sm")
        self.extension_entry.grid(column = 2, row = 3, columnspan = 2)
        self.files_label = Label(self.top_window, text = "found files:")
        self.files_label.grid(column = 4, row = 1, columnspan = 2)
        self.files_list = Listbox(self.top_window, width = 60)
        self.files_list.grid(column = 4, row = 2, rowspan = 3, columnspan = 2)
        self.search_button = Button(self.top_window, text = "Search", command = self.search_for_files_and_put_to_list)
        self.search_button.grid (column = 1, columnspan = 3, row = 4)

        self.searched_phrase_label = Label(self.top_window, text = "searched phrase")
        self.searched_phrase_label.grid (column = 1, row = 6)
        self.searched_phrase_entry = Entry(self.top_window, width = 30)
        self.searched_phrase_entry.insert(0,"[0-4]")
        self.searched_phrase_entry.grid(column = 2, columnspan = 2, row = 6)
        self.old_phrase_label = Label(self.top_window, text = "old phrase")
        self.old_phrase_label.grid(column = 1, row = 7)
        self.old_phrase_entry = Entry(self.top_window, width = 30)
        self.old_phrase_entry.insert(0, "4")
        self.old_phrase_entry.grid(column = 2, columnspan = 2, row = 7)
        self.new_phrase_label = Label(self.top_window, text = "new phrase")
        self.new_phrase_label.grid(column = 1, row = 8)
        self.new_phrase_entry = Entry(self.top_window, width = 30)
        self.new_phrase_entry.insert(0, "2")
        self.new_phrase_entry.grid(column = 2, columnspan = 2, row = 8)
        self.line_length_label = Label(self.top_window, text = "line length")
        self.line_length_label.grid(column = 1, row = 9)
        self.line_length_entry = Entry(self.top_window, width = 3) 
        self.line_length_entry.insert(0, "4")
        self.line_length_entry.grid(column = 2, row =9, sticky = "w")
        self.change_button = Button(self.top_window, text = "change", command = self.change_files)
        self.change_button.grid(column = 3, row = 9)
        self.changed_files_label = Label(self.top_window, text = "changed files:")
        self.changed_files_label.grid(column = 4, row = 5)
        self.changed_files_list = Listbox(self.top_window, width = 30, fg = Color("green"))
        self.changed_files_list.grid(column = 4, row = 6, rowspan = 4)
        self.unchanged_files_label = Label(self.top_window, text = "unchanged files:")
        self.unchanged_files_label.grid(column = 5, row = 5)
        self.unchanged_files_list = Listbox(self.top_window, width = 30, fg = Color("red"))
        self.unchanged_files_list.grid(column = 5, row = 6, rowspan = 4)

    def search_for_files_and_put_to_list(self):
        self.files_list.delete(0, END)
        self.finder = File_Finder(self.path_entry.get(), self.extension_entry.get())
        for file_path in self.finder.file_paths:
            self.files_list.insert(1,file_path)

    def change_files(self):
        self.changed_files_list.delete(0, END)
        for file_path in self.files_list.get(0, END):
            changer = File_Changer(str(file_path), str(self.searched_phrase_entry.get()), int(self.line_length_entry.get()), str(self.old_phrase_entry.get()), str(self.new_phrase_entry.get()))
            self.put_on_proper_list(changer.output_code, file_path)

    def put_on_proper_list(self, code, file_path):
        if code != 1:
            self.unchanged_files_list.insert(1, file_path)
        else:
            self.changed_files_list.insert(1, file_path)

if __name__ == "__main__":
    gui = File_Changer_GUI()
    gui.top_window.mainloop()
