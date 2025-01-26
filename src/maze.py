import random

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
            win=None,
            seed=None
            ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self._win = win

        if seed != None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_walls_r(self, i, k):
        c_cell = self._cells[i][k]
        c_cell.visited = True

        while True:
            to_vis = []
            # check visitable neighbours
            left = i - 1
            if left >= 0:
                if self._cells[left][k].visited == False:
                    to_vis.append(("left", left, k))
            right = i + 1
            if right < len(self._cells):
                if self._cells[right][k].visited == False:
                    to_vis.append(("right", right, k))
            up = k - 1
            if up >= 0:
                if self._cells[i][up].visited == False:
                    to_vis.append(("up" ,i, up))
            down = k + 1
            if down < len(self._cells[0]):
                if self._cells[i][down].visited == False:
                    to_vis.append(("down", i, down))
            
            if to_vis == []:
                if self._win != None:
                    c_cell.draw(self._win.canvas)
                return
            
            else:
                # choose a neighbour
                move_to = random.choice(to_vis)
                to_vis.remove(move_to)
                direc, col, row = move_to
                next_cell = self._cells[col][row]
                # remove walls
                c_cell.make_wall(direc)
                next_cell.make_wall(direc, inv_direction=True)
                # move to neighbour
                self._break_walls_r(col, row)