from window import Point, Line

class Cell:
    def __init__(self, point, size, window=None):
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
        color = fill_color
        if not self.left_wall:
            color = "grey"
        Line(
            Point(self._x1, self._y1),
            Point(self._x1, self._y2)
            ).draw(canvas, fill_color=color)
        color = fill_color
        if not self.right_wall:
            color = "grey"
        Line(
            Point(self._x2, self._y1),
            Point(self._x2, self._y2)
            ).draw(canvas, fill_color=color)
        color = fill_color
        if not self.up_wall:
            color = "grey"
        
        Line(
            Point(self._x1, self._y1),
            Point(self._x2, self._y1)
            ).draw(canvas, fill_color=color)
        color = fill_color
        if not self.down_wall:
            color = "grey"
        Line(
            Point(self._x1, self._y2),
            Point(self._x2, self._y2)
            ).draw(canvas, fill_color=color)
        
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
