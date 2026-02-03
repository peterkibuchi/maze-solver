import random
import time
from cell import Cell
from graphics import Window


class Maze():
    def __init__(
            self,
            x1: int | float,
            y1: int | float,
            num_rows: int,
            num_cols: int,
            cell_size_x: int | float,
            cell_size_y: int | float,
            win: Window | None = None,
            seed: int | None = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__cells: list[list[Cell]] = []
        self.__win = win

        if seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        # The top level list contains the columns, the inner lists the rows
        self.__cells = [[Cell(self.__win) for j in range(
            self.__num_rows)] for i in range(self.__num_cols)]

        for j in range(self.__num_rows):
            for i in range(self.__num_cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        if self.__win is None:
            return

        # i = column, j = row
        left_x = self.__x1 + (self.__cell_size_x * i)  # column → x
        top_y = self.__y1 + (self.__cell_size_y * j)  # row → y

        right_x = left_x + self.__cell_size_x
        bottom_y = top_y + self.__cell_size_y

        self.__cells[i][j].draw(left_x, top_y, right_x, bottom_y)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        last_row_idx = self.__num_rows - 1
        last_col_idx = self.__num_cols - 1
        self.__cells[last_col_idx][last_row_idx].has_bottom_wall = False
        self.__draw_cell(last_col_idx, last_row_idx)

    def __break_walls_r(self, i: int, j: int):
        self.__cells[i][j].visited = True

        while True:
            adjacent_cells = [
                (i-1, j),  # top_cell_idx
                (i+1, j),  # bottom_cell_idx
                (i, j-1),  # left_cell_idx
                (i, j+1)  # right_cell_idx
            ]

            def is_index_valid(index, num_items): return 0 <= index < num_items
            viable_cells = [
                cell for cell in adjacent_cells
                if is_index_valid(cell[0], self.__num_cols) and is_index_valid(cell[1], self.__num_rows)
            ]

            possible_moves: list[tuple[int, int]] = []
            for col, row in viable_cells:
                if not self.__cells[col][row].visited:
                    possible_moves.append((col, row))

            # if there is nowhere to go from here, break out
            if len(possible_moves) == 0:
                self.__draw_cell(i, j)
                return

            # randomly choose the next direction to go
            next_cell_i, next_cell_j = random.choice(possible_moves)
            next_cell = self.__cells[next_cell_i][next_cell_j]

            # break walls between this cell and the next cell
            if next_cell_i == i - 1 and next_cell_j == j:  # left
                self.__cells[i][j].has_left_wall = False
                next_cell.has_right_wall = False

            elif next_cell_i == i + 1 and next_cell_j == j:  # right
                self.__cells[i][j].has_right_wall = False
                next_cell.has_left_wall = False

            elif next_cell_i == i and next_cell_j == j - 1:  # above
                self.__cells[i][j].has_top_wall = False
                next_cell.has_bottom_wall = False

            elif next_cell_i == i and next_cell_j == j + 1:  # below
                self.__cells[i][j].has_bottom_wall = False
                next_cell.has_top_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_cell_i, next_cell_j)
