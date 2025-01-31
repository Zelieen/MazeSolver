from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    M = Maze(0, 0, 16, 16, 50, win)
    M.solve()

    win.wait_for_close()

main()