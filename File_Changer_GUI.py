from Tkinter import *
from threading import Thread
from File_Finder import *

class File_Changer_GUI:
    path = ""
    extension = ""

    def __init__(self):
        self.top_window = Tk()
        self.path_label = Label(self.top_window, text = "path")
        self.path_label.grid(column = 1, row = 1)
        self.path_entry = Entry(self.top_window, textvariable = self.path, width = 30)
        self.path_entry.grid(column = 2, row = 1)
        self.extension_label = Label(self.top_window, text = "extension")
        self.extension_label.grid(column = 1, row = 2)
        self.extension_entry = Entry(self.top_window, textvariable = self.extension, width = 30)
        self.extension_entry.grid(column = 2, row = 2)
        self.scroll = Scrollbar(self.top_window)
        self.files_list = Listbox(self.top_window, yscrollcommand = self.scroll.set )
        self.files_list.grid(column = 3, row = 1, rowspan = 3)
        self.search_button = Button(self.top_window, text = "Search", command = self.search_for_files_and_put_to_list)
        self.search_button.grid (column = 1, columnspan = 2, row = 3)

        self.top_window.mainloop()

    def search_for_files_and_put_to_list(self):
        self.finder = File_Finder(self.path, self.extension)
        for file_path in self.finder.file_paths:
            self.files_list.insert(file_path)

gui = File_Changer_GUI()
