import unittest
from cell import Cell
from maze import Maze


class TestCell(unittest.TestCase):
    def test_cell_default_walls(self):
        """All walls should be present by default."""
        cell = Cell()
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_walls_can_be_toggled(self):
        """Walls should be individually removable."""
        cell = Cell()
        cell.has_left_wall = False
        cell.has_top_wall = False

        self.assertFalse(cell.has_left_wall)
        self.assertFalse(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_draw_without_window_no_error(self):
        """Drawing without a window should not raise an error."""
        cell = Cell()
        cell.draw(10, 20, 50, 60)  # Should silently return

    def test_cell_draw_move_without_window_no_error(self):
        """draw_move without a window should not raise an error."""
        cell1 = Cell()
        cell2 = Cell()
        cell1.draw_move(cell2)  # Should silently return
        cell1.draw_move(cell2, undo=True)  # Should also work


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        """Maze should create correct number of columns and rows."""
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_create_cells_small(self):
        """Maze should work with minimal dimensions."""
        m = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m._Maze__cells), 1)
        self.assertEqual(len(m._Maze__cells[0]), 1)

    def test_maze_create_cells_large(self):
        """Maze should handle larger dimensions."""
        num_cols = 50
        num_rows = 40
        m = Maze(0, 0, num_rows, num_cols, 5, 5)

        self.assertEqual(len(m._Maze__cells), num_cols)
        self.assertEqual(len(m._Maze__cells[0]), num_rows)

    def test_maze_cells_are_cell_instances(self):
        """Each cell in the maze should be a Cell instance."""
        m = Maze(0, 0, 3, 4, 10, 10)
        for col in m._Maze__cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_maze_with_offset(self):
        """Maze should accept non-zero starting positions."""
        m = Maze(100, 200, 5, 5, 10, 10)
        self.assertEqual(len(m._Maze__cells), 5)
        self.assertEqual(len(m._Maze__cells[0]), 5)

    def test_maze_with_float_dimensions(self):
        """Maze should handle float cell sizes."""
        m = Maze(0.5, 0.5, 3, 3, 10.5, 10.5)
        self.assertEqual(len(m._Maze__cells), 3)
        self.assertEqual(len(m._Maze__cells[0]), 3)

    def test_maze_cells_independent(self):
        """Each cell should be an independent object."""
        m = Maze(0, 0, 3, 3, 10, 10)
        m._Maze__cells[0][0].has_left_wall = False

        # Other cells should not be affected
        self.assertTrue(m._Maze__cells[0][1].has_left_wall)
        self.assertTrue(m._Maze__cells[1][0].has_left_wall)

    def test_maze_rectangular_dimensions(self):
        """Maze should work with different row and column counts."""
        num_cols = 20
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m._Maze__cells), num_cols)
        for col in m._Maze__cells:
            self.assertEqual(len(col), num_rows)

    def test_maze_break_entrance_and_exit(self):
        """Entrance (top of first cell) and exit (bottom of last cell) should be open."""
        m = Maze(0, 0, 5, 5, 10, 10)
        m._Maze__break_entrance_and_exit()

        # Entrance: top wall of cell[0][0] should be removed
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        # Exit: bottom wall of cell[-1][-1] should be removed
        self.assertFalse(m._Maze__cells[-1][-1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
