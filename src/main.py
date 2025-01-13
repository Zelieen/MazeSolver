from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    lin = Line(Point(25, 40), Point(460, 206))
    win.draw_line(lin, "white")

    c1 = Cell(Point(50,120), 10, win)
    win.draw_cell(c1)

    c2 = Cell(Point(500,120), 100, win)
    c2.left_wall = False
    win.draw_cell(c2, "red")

    c3 = Cell(Point(510,320), 50, win)
    c3.right_wall = False
    win.draw_cell(c3, "blue")

    c4 = Cell(Point(450,30), 50, win)
    c4.up_wall = False
    c4.down_wall = False
    win.draw_cell(c4, "green")

    c5 = Cell(Point(400,320), 25, win)
    c5.left_wall = False
    c5.right_wall = False
    c5.up_wall = False
    c5.down_wall = False
    win.draw_cell(c5)

    c1.draw_path(c2)
    c3.draw_path(c4, True)

    win.wait_for_close()

main()