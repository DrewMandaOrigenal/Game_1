from tkinter import *

class Table:

    def __init__(self, window, colour="black", net_colour="green",
               width=600, height=400,
               vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.colour = colour
        
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width= self.width)
        self.canvas.pack()

        if(vertical_net):
           self.canvas.create_line(self.width/2, 0, self.width/2,
                                   self.height, width=2, fill=net_colour, dash=(15, 23))

        if(horizontal_net):
           self.canvas.create_line(0, self.height/2, self.width,
                                   self.height/2, width=2, fill=net_colour, dash=(15, 23))
    
    def draw_oval(self, master):
        return

    def draw_rectangle(self, master):
        return

    def move_(self, circle, y1, y2):
        return
