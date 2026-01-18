import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        """Test maze creates cells with correct dimensions"""
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_1x1(self):
        """Test edge case: 1x1 maze"""
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m1._Maze__cells), 1)
        self.assertEqual(len(m1._Maze__cells[0]), 1)

    def test_maze_single_row(self):
        """Test edge case: single row maze"""
        num_cols = 5
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_single_column(self):
        """Test edge case: single column maze"""
        num_cols = 1
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_with_none_window(self):
        """Test maze creation without graphics window"""
        num_cols = 10
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)
        # Verify it doesn't crash when creating cells without window
        self.assertIsNotNone(m1._Maze__cells)


if __name__ == "__main__":
    unittest.main()
