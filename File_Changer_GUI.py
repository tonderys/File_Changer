from Tkinter import *
from threading import Thread

class File_Changer_GUI:
    path = ""

    def __init__(self):
        self.top_window = Tk()
        self.path_label = Label(self.top_window, text = "path")
        self.path_entry = Entry(self.top_window, textvariable = self.path, width = 30)
        self.scroll_list = 

        self.path_label.grid(column = 1, row = 1)
        self.path_entry.grid(column = 2, row = 1)
        self.top_window.mainloop()

gui = File_Changer_GUI()
