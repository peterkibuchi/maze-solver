from graphics import Line, Point, Window


class Cell():
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
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
