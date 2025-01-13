from window import Point, Line

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
        
    def get_center(self):
        c_x = (self._x1 + self._x2) // 2
        c_y = (self._y1 + self._y2) // 2
        return Point(c_x, c_y)
    
    def draw_path(self, to_cell, undo=False):
        if self._win == None:
            return
        
        c1 = self.get_center()
        c2 = to_cell.get_center()

        fill_color = "red"
        if undo:
            fill_color = "yellow"

        Line(c1, c2).draw(self._win.canvas, fill_color=fill_color)
