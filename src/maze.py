from cell import Cell, Point
from time import sleep

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size,
            win=None
            ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for c in range(self.num_cols):
            row_list = []
            for r in range(self.num_rows):
                x = (c * self.cell_size) + self.x
                y = (r * self.cell_size) + self.y
                position = Point(x, y)
                row_list.append(Cell(position, self.cell_size, self._win))
                if self._win:
                    row_list[-1].draw(self._win.canvas) #and draw it onto the canvas
                    self._animate()
            self._cells.append(row_list)

    def _draw_cell(self, column, row):
        cell = self._cells[column][row]
        cell.draw(self._win.canvas)

    def _animate(self):
        self._win.redraw()
        sleep(0.1)

    def _break_entrance_and_exit(self):
        self._cells[0][0].up_wall = False
        if self._win:
            self._draw_cell(0, 0)
        self._cells[-1][-1].down_wall = False
        if self._win:
            self._draw_cell(-1,-1)