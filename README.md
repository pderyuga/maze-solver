# Maze Solver

A visual maze generator and solver built in Python with an animated GUI. Watch as the program generates a random maze using recursive depth-first search, then solves it using recursive backtracking!

![Maze Solver Demo](https://img.shields.io/badge/python-3.14+-blue.svg)

## About

This project is based on [Boot.dev's "Build a Maze Solver in Python" course](https://www.boot.dev/courses/build-maze-solver-python). It demonstrates fundamental computer science concepts including:

- Recursive algorithms
- Graph traversal (depth-first search)
- Backtracking
- Object-oriented programming
- GUI programming with Tkinter

## Prerequisites

- Python 3.14 or higher
- `uv` package manager (recommended) or standard Python tools

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pderyuga/maze-solver.git
   cd maze-solver
   ```

2. **Install `uv` (if you don't have it):**

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up the virtual environment:**
   ```bash
   uv sync
   ```

## Usage

### Run the Maze Solver

Using `uv`:

```bash
uv run main.py
```

Or with standard Python:

```bash
python3 main.py
```

The program will:

1. Open a graphical window
2. Generate a random maze with animated wall-breaking
3. Automatically solve the maze with animated pathfinding
4. Display the solution path in red (with backtracking shown in gray)

### Run Tests

```bash
uv run tests.py
```

Or:

```bash
python3 tests.py
```

For verbose test output:

```bash
python3 tests.py -v
```

## Project Structure

```
maze-solver/
├── main.py           # Entry point - configures and runs the maze solver
├── maze.py           # Maze class - generation and solving algorithms
├── cell.py           # Cell class - represents individual maze cells
├── graphics.py       # Graphics classes - Window, Line, Point for visualization
├── tests.py          # Unit tests
├── pyproject.toml    # Project configuration and dependencies
└── README.md         # This file
```

## Configuration

You can modify settings in `main.py`:

```python
num_rows = 12          # Number of rows in the maze
num_cols = 16          # Number of columns in the maze
margin = 50            # Margin around the maze (pixels)
screen_x = 800         # Window width (pixels)
screen_y = 600         # Window height (pixels)
```

Cell sizes are calculated automatically based on the window size and margins.

## Ideas for Extension

While not required, if you enjoyed this project and want to extend it further for additional practice, here are some ideas:

- **Add other solving algorithms**, like breadth-first search or A\*
- **Make the visuals prettier**, change the colors, etc.
- **Mess with the animation settings** to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
- **Add configurations in the app itself** using Tkinter buttons and inputs to allow users to change maze size, speed, etc.
- **Make much larger mazes** to solve
- **Make it a game** where the user chooses directions
- **If you made it a game**, allow the user to race an algorithm
- **Make it 3-dimensional**
- **Time the various algorithms** and see which ones are the fastest

## License

This is an educational project. Feel free to use and modify as you learn!

## Acknowledgments

- [Boot.dev](https://www.boot.dev/) for the excellent course material
- The Python community for Tkinter documentation and examples
