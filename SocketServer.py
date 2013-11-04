from Tkinter import *
from time import *

class SocketServer:
    def __init__(self):
        self.top_window = Tk()
        self.message = Label(self.top_window, text = "")
        self.message.grid(column = 1, row = 1)

    def change_label(self, message):
        self.message.config(text = message)
        
socket = SocketServer()
socket.top_window.mainloop()
