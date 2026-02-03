# Maze Solver

A visual maze generator and solver built with `tkinter`. The program generates a random maze, then animates an algorithm finding a path from the start to the goal.

You can use this as a learning tool for pathfinding algorithms, recursion, and GUI programming in Python.

## Features

- Random maze generation on a grid
- Visual animation of the solving process
- Clear distinction between:
  - Walls
  - Open paths
  - Current search frontier
  - Final solution path
- Configurable maze size and speed (if you implemented that)
- Simple GUI using `tkinter` (included with Python)

## Tech Stack

- Language: Python 3.13
- GUI: tkinter
- Algorithms: Depth-first search (DFS)

## How It Works

At a high level:

1. The program creates a 2D grid representing the maze.
2. A maze generation algorithm carves passages between cells.
3. A solving algorithm (e.g. DFS) explores neighboring cells recursively or iteratively.
4. Each step of the search is drawn to the screen to visualize progress.
5. When the goal is reached, the final path is highlighted.

## Getting Started

### Prerequisites

- Python 3.13+ installed
You can check your version with:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/peterkibuchi/maze-solver.git
cd maze-solver
```

### Running the Project

From the project directory, run:

```bash
python3 main.py
```

A window should open and immediately show a generated maze and start solving it.

## Possible Extensions

- Add BFS, Dijkstra, or A* as additional solving options
- Add UI controls for:
  - Maze size
  - Animation speed
  - Algorithm selection
- Improve visuals (colors, themes, highlighting)
- Turn it into a playable maze game
- Let the user race the algorithm
- Experiment with 3D mazes or very large grids
- Benchmark different algorithms’ performance
