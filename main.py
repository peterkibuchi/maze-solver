from graphics import Window, Line, Point


def main():
    print("Hello from maze-solver!")
    win = Window(800, 600)
    point1, point2 = Point(100, 100), Point(500, 500)
    point3, point4 = Point(100, 500), Point(500, 100)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
