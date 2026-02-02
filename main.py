from maze import Maze
from graphics import Line, Point, Window


def main():
    print("Hello from maze-solver!")
    win = Window(800, 600)

    maze = Maze(100, 100, 5, 10, 50, 50, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
