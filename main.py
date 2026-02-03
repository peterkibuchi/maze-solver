import sys
from maze import Maze
from graphics import Line, Point, Window


def main():
    print("Hello from maze-solver!")
    screen_x, screen_y = 1000, 1000
    win = Window(screen_x, screen_y)

    margin = 50
    num_rows, num_cols = 12, 12
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, win)

    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved!")

    win.wait_for_close()


if __name__ == "__main__":
    main()
