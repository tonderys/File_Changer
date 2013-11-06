from Tkinter import *

class NoTuplePassedToDraw (Exception):
    pass

class DrawGraph:
    def __init__(self,top_window, values, height=500, row = 1, column = 2):
        if type(values) is not tuple: raise NoTuplePassedToDraw
        self.values = values
        self.width = len(self.values)*10
        self.height = height
        self.y_top = 1
        self.y_bottom = self.height
        self.x_left_border = 1 
        self.x_right_border = self.width 
        self.x_axis = self.y_bottom
        self.min_value = 0
        self.max_value = 0

        self.top_window = top_window
        frame = Frame(self.top_window, width = 500, height = 500)
        frame.grid(row = 1, column = 1)
        self.board = Canvas (self.top_window,width = self.width, height = self.height, scrollregion = (0,0,500,500))
        scrollbar = Scrollbar(self.top_window, orient = HORIZONTAL)
        scrollbar.pack(side = BOTTOM, fill = X)
        scrollbar.config(command = self.board.xview)
        self.board.config(width = self.width, height = self.height)
        self.board.config(xscrollcommand = scrollbar.set)
        #self.board.grid(row = row, column = column, expand = True)
        self.board.pack(side = LEFT, fill = BOTH, expand = True)
       
        self.interior = interior = Frame(self.board)
        interior_id = self.board.create_window(0, 0, window=interior,
                                           anchor=NW)
 
        self.set_min_max_values()
        self.set_range_of_values()
        self.set_scale()
        self.set_x_axis_position()
        self.draw_x_axis_line()
        self.draw_y_axis_line()
        self.draw_graph()


    def set_min_max_values(self):
        for v in self.values:
            if v > self.max_value: self.max_value = v
            elif v < self.min_value: self.min_value = v

    def set_range_of_values(self):
        self.range_of_values = self.max_value - self.min_value

    def set_scale(self):
        self.scale = self.height / self.range_of_values

    def set_x_axis_position(self):
        if self.min_value < 0 and self.max_value > 0:
            self.x_axis = self.max_value * self.scale
        elif self.min_value < 0 and self.max_value <= 0:
            self.x_axis = 0

    def draw_x_axis_line(self):
        self.board.create_line(self.x_left_border, self.x_axis, self.x_right_border, self.x_axis)

    def draw_y_axis_line(self):
        self.board.create_line(self.x_left_border,self.y_top,self.x_left_border,self.y_bottom)

    def draw_graph(self):
        for i in range(0,len(self.values)-1):
            self.board.create_line(i*10, self.get_x_from_values(i), (i+1)*10, self.get_x_from_values(i+1))

    def get_x_from_values(self, x):
        return self.x_axis-(self.values[x]*self.scale)
if __name__ == "__main__":
    top_window = Tk()
    tuple_of_numbers = (1,4,9,16,25,36,49,64,81,100,81,64,49,36,25,16,9,4)
    tuple_of_tuples = (tuple_of_numbers) 
    draw_graph = DrawGraph(top_window, tuple_of_numbers)
    draw_graph.top_window.mainloop()
        
