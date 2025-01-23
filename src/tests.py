import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_more_rows(self):
        num_cols = 1
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_more_cols(self):
        num_cols = 20
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_no_cols(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

    def test_maze_create_no_rows(self):
        num_cols = 1
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_no_rows(self):
        num_cols = 3
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].up_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].down_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()