from graphics import Line, Point, Window


class Cell():
    def __init__(self, window: Window | None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1: int | float = -1
        self.__y1: int | float = -1
        self.__x2: int | float = -1
        self.__y2: int | float = -1
        self.__win = window

    def draw(self, x1: int | float, y1: int | float, x2: int | float, y2: int | float):
        if self.__win is None:
            return

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_top_wall:
            self.__win.draw_line(Line(top_left, top_right))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right))
        if self.has_left_wall:
            self.__win.draw_line(Line(top_left, bottom_left))
        if self.has_right_wall:
            self.__win.draw_line(Line(top_right, bottom_right))

    def draw_move(self, to_cell, undo: bool = False):
        if self.__win is None:
            return

        line_color = "gray" if undo else "red"

        self_center = Point(
            (self.__x1 + self.__x2) / 2,
            (self.__y1 + self.__y2) / 2
        )
        other_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2,
            (to_cell.__y1 + to_cell.__y2) / 2
        )

        self.__win.draw_line(Line(self_center, other_center), line_color)
