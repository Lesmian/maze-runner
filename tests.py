import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_returns_correct_size(self):
        num_cols = 3
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_creates_entrance_and_exit(self):
        num_cols = 3
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[2][4].has_bottom_wall,
            False,
        )

    def test_maze_breaks_walls(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][0].has_bottom_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            True,
        )
        self.assertEqual(
            m1._cells[0][0].has_right_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][0].has_top_wall,
            True,
        )
        self.assertEqual(
            m1._cells[1][0].has_bottom_wall,
            True,
        )
        self.assertEqual(
            m1._cells[1][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][0].has_right_wall,
            True,
        )
        self.assertEqual(
            m1._cells[0][1].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][1].has_bottom_wall,
            True,
        )
        self.assertEqual(
            m1._cells[0][1].has_left_wall,
            True,
        )
        self.assertEqual(
            m1._cells[0][1].has_right_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][1].has_top_wall,
            True,
        )
        self.assertEqual(
            m1._cells[1][1].has_bottom_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][1].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[1][1].has_right_wall,
            True,
        )

if __name__ == "__main__":
    unittest.main()