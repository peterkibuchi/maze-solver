from cell import Cell
from graphics import Line, Point, Window


def main():
    print("Hello from maze-solver!")
    win = Window(800, 600)

    cell1 = Cell(win)
    cell2 = Cell(win)

    cell1.draw(100, 100, 200, 200)
    cell2.draw(400, 400, 500, 500)

    win.wait_for_close()


if __name__ == "__main__":
    main()
