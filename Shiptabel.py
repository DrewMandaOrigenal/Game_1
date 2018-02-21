from tkinter import *

class Table:
    def __init__(self, window, colour="black", width=600, height=800):
      self.width = width
      self.height = height
      self.colour = colour

      self.canvas = Canvas(window, bg=self.colour, height=self.height,width=self.width)
      self.canvas.pack()

    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.colur
        return retangle.colour.create_rectangle(x1, y1, x2, y2, fill=c)

    def draw_circle(self, circle):
        x1 = circle.x_posn
        x2 = circle.x_posn + circle.width
        y1 = circle.y_posn
        y2 = circle.y_posn + circle. height
        c = circle.colour
        return self.canvas.create_circle(x1, y1, x2, y2, fill=c)

    def move_item(self, item):
        self.canvas.delete(item)

    def change_item_colour(self, item, c):
        self.canvas.itemconfigure(item, fill=c)
   
