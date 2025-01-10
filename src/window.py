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
