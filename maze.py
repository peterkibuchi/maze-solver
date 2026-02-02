from cell import Cell
from graphics import Window
import time


class Maze():
    def __init__(
            self,
            x1: int | float,
            y1: int | float,
            num_rows: int,
            num_cols: int,
            cell_size_x: int | float,
            cell_size_y: int | float,
            win: Window | None = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__cells: list[list[Cell]] = []
        self.__win = win

        self.__create_cells()
        self.__break_entrance_and_exit()

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
