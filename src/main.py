from window import Window, Line, Point

def main():
    win = Window(800, 600)
    lin = Line(Point(25, 40), Point(460, 206))
    win.draw_line(lin, "white")
    win.wait_for_close()

main()