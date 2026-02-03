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
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m._Maze__cells), num_cols)
        self.assertEqual(len(m._Maze__cells[0]), num_rows)

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

        # Verify cells are distinct objects, not references to the same object
        self.assertIsNot(m._Maze__cells[0][0], m._Maze__cells[0][1])
        self.assertIsNot(m._Maze__cells[0][0], m._Maze__cells[1][0])
        self.assertIsNot(m._Maze__cells[1][0], m._Maze__cells[1][1])

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

        # Entrance: top wall of cell[0][0] should be removed
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        # Exit: bottom wall of cell[-1][-1] should be removed
        self.assertFalse(m._Maze__cells[-1][-1].has_bottom_wall)

    def test_maze_reset_cells_visited(self):
        """All cells should have visited=False after maze generation completes."""
        m = Maze(0, 0, 5, 5, 10, 10)

        for col in m._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)

    def test_maze_reset_cells_visited_clears_all(self):
        """__reset_cells_visited should set visited=False on all cells."""
        m = Maze(0, 0, 3, 3, 10, 10)

        # Manually mark all cells as visited
        for col in m._Maze__cells:
            for cell in col:
                cell.visited = True

        # Call reset
        m._Maze__reset_cells_visited()

        # Verify all cells are now unvisited
        for col in m._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)

    def test_maze_break_walls_deterministic_with_seed(self):
        """Same seed should produce identical mazes."""
        m1 = Maze(0, 0, 5, 5, 10, 10, seed=42)
        m2 = Maze(0, 0, 5, 5, 10, 10, seed=42)

        for i in range(5):
            for j in range(5):
                c1 = m1._Maze__cells[i][j]
                c2 = m2._Maze__cells[i][j]
                self.assertEqual(c1.has_left_wall, c2.has_left_wall)
                self.assertEqual(c1.has_right_wall, c2.has_right_wall)
                self.assertEqual(c1.has_top_wall, c2.has_top_wall)
                self.assertEqual(c1.has_bottom_wall, c2.has_bottom_wall)

    def test_maze_break_walls_different_seeds_different_mazes(self):
        """Different seeds should produce different mazes."""
        m1 = Maze(0, 0, 5, 5, 10, 10, seed=42)
        m2 = Maze(0, 0, 5, 5, 10, 10, seed=99)

        differences = 0
        for i in range(5):
            for j in range(5):
                c1 = m1._Maze__cells[i][j]
                c2 = m2._Maze__cells[i][j]
                if c1.has_left_wall != c2.has_left_wall:
                    differences += 1
                if c1.has_right_wall != c2.has_right_wall:
                    differences += 1

        self.assertGreater(differences, 0)

    def test_maze_break_walls_consistent_between_neighbors(self):
        """If cell A has no right wall, cell B (to the right) should have no left wall."""
        m = Maze(0, 0, 5, 5, 10, 10, seed=42)

        for i in range(5):
            for j in range(5):
                cell = m._Maze__cells[i][j]

                # Check horizontal consistency
                if i < 4:
                    right_neighbor = m._Maze__cells[i + 1][j]
                    self.assertEqual(
                        cell.has_right_wall,
                        right_neighbor.has_left_wall,
                        f"Wall mismatch between ({i},{j}) and ({i+1},{j})"
                    )

                # Check vertical consistency
                if j < 4:
                    bottom_neighbor = m._Maze__cells[i][j + 1]
                    self.assertEqual(
                        cell.has_bottom_wall,
                        bottom_neighbor.has_top_wall,
                        f"Wall mismatch between ({i},{j}) and ({i},{j+1})"
                    )


if __name__ == "__main__":
    unittest.main()
