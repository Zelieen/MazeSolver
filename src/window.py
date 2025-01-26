from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__rootWidget = Tk()
        self.__rootWidget.title("A Maze Solver")
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__rootWidget, bg="grey", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)

        self.IsRunning = False
        
    def redraw(self):
        self.__rootWidget.update_idletasks()
        self.__rootWidget.update()

    def wait_for_close(self):
        self.IsRunning = True
        while self.IsRunning:
            self.redraw()

    def close(self):
        self.IsRunning = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill = fill_color,
            width = 2
        )