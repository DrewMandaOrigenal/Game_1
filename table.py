from tkinter import *

class Table:

    def __init__(self, window, colour="black", width=600, height=400):
        self.width = width
        self.height = height
        self.colour = colour
        
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width= self.width)
        self.canvas.pack()

    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.colour
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
    
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.colour
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)

    def move_item(self, item, x1, x2, y1, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
