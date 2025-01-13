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

class Cell:
    def __init__(self, point, size, window):
        self._x1 = point.x
        self._x2 = point.x + size
        self._y1 = point.y
        self._y2 = point.y + size
        self._win = window

        self.left_wall = True
        self.right_wall = True
        self.up_wall = True
        self.down_wall = True

    def draw(self, canvas, fill_color="black"):
        if self.left_wall:
            Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
                ).draw(canvas, fill_color=fill_color)
        if self.right_wall:
            Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2)
                ).draw(canvas, fill_color=fill_color)
        if self.up_wall:
            Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
                ).draw(canvas, fill_color=fill_color)
        if self.down_wall:
            Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2)
                ).draw(canvas, fill_color=fill_color)