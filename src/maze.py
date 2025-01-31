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
        if len(self._cells) > 0:
            if len(self._cells[0]) > 0:
                self._break_entrance_and_exit()
                self._break_walls_r(0, 0)
                self._reset_cells_visited()

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
                    self._animate(0.005)
            self._cells.append(row_list)

    def _draw_cell(self, column, row):
        cell = self._cells[column][row]
        cell.draw(self._win.canvas)

    def _animate(self, duration=0.1):
        if self._win == None:
            return
        self._win.redraw()
        sleep(duration)

    def _break_entrance_and_exit(self):
        if len(self._cells) < 1:
            return
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
            #self._animate(0.05)
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
                #to_vis.remove(move_to)
                direc, col, row = move_to
                next_cell = self._cells[col][row]
                # remove walls
                c_cell.make_wall(direc)
                next_cell.make_wall(direc, inv_direction=True)
                # move to neighbour
                self._break_walls_r(col, row)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, k):
        self._animate()
        self._cells[i][k].visited = True
        if self._cells[i][k] == self._cells[-1][-1]:
            return True
        directions = [("left", i-1, k), ("right", i+1, k), ("up", i, k-1), ("down", i, k+1)]
        for direction, h, v in directions:
            valid_cell = (h in range(len(self._cells))) and (v in range(len(self._cells[0])))
            
            no_wall = False
            if direction == "left":
                no_wall = not self._cells[i][k].left_wall
            if direction == "right":
                no_wall = not self._cells[i][k].right_wall
            if direction == "up":
                no_wall = not self._cells[i][k].up_wall            
            if direction == "down":
                no_wall = not self._cells[i][k].down_wall
            
            if valid_cell and no_wall:
                if self._cells[h][v].visited == False:
                    self._cells[i][k].draw_path(self._cells[h][v]) #move
                    success = self.solve_r(h, v)
                    if success:
                        return True
                    else:
                        self._cells[i][k].draw_path(self._cells[h][v], True) #undo
        return False