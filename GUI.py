from Tkinter import *

class Frame:
    clicked = 0
    top = None
    button = None

    def __init__(self):
    	self.top = Tk()
    	self.button = Button(self.top, text = "kilknieto %d razy" % (self.clicked), command = self.click)
    	self.button.pack()
    	self.top.mainloop()

    def click(self):
    	self.clicked += 1
        self.button.config(text ="kilknieto %d razy" % (self.clicked))

frame = Frame()
