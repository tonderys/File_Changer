from Tkinter import *

class DrawGraph:
    def __init__(self, width, height, row = 1, column = 1):
        self.width = width
        self.height = height
        
        self.top_window = Tk()
        self.board = Canvas (self.top_window, width = width, height = height)
        self.board.grid(row = row, column = column)

        self.draw_axis_lines()
        self.draw_x_scale(0,10)

        self.top_window.mainloop()

    def draw_axis_lines(self):
        self.board.create_line(0,self.height-5,self.width,self.height-5)
        self.board.create_line(5,0,5,self.height)

    def draw_x_scale(self, min_value, max_value):
        x_range = max_value - min_value
        scale = self.width/x_range
        steps = int(self.width/scale)
        for i in range (1,steps):
            self.board.create_line(i*10,self.height-10,i*10,self.height)


draw_graph = DrawGraph(500,500)
        
