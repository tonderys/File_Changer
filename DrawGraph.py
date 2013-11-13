from Tkinter import *

class NoTuplePassedToDraw (Exception):
    pass

class DrawGraph:
    def __init__(self,top_window, values, width = 500, height = 500, row = 1, column = 1):
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
        scroll_height = 20

        self.top_window = top_window

        self.frame = Frame(self.top_window, width = 500, height = self.height)
        self.frame.grid(row = 0, column = 0)
        self.frame.grid_propagate(False)

        self.scroll = Scrollbar (self.frame, orient=HORIZONTAL)
        self.board = Canvas (self.frame, width = 500, height = self.height-scroll_height, scrollregion = (0,0,self.width, self.height), xscrollcommand=self.scroll.set)
        self.scroll['command'] = self.board.xview
        
        self.board.grid(row = 0, column = 0, sticky = (N,E,W,S))
        self.scroll.grid(row = 1, column = 0, sticky = (E,W))
 
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
    tuple_of_numbers = (0,1,4,9,16,25,36,49,64,81,100,81,64,49,36,25,16,9,4,1)
    draw_graph = DrawGraph(top_window, tuple_of_numbers*5)
    draw_graph.top_window.mainloop()
       
