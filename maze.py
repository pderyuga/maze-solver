import time
import random

from graphics import Window
from cell import Cell


class Maze:

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | float | str | bytes | bytearray | None = None,
    ):
        self.__x1: int = x1
        self.__y1: int = y1
        self.__num_rows: int = num_rows
        self.__num_cols: int = num_cols
        self.__cell_size_x: int = cell_size_x
        self.__cell_size_y: int = cell_size_y
        self.__win: Window = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if not seed == None:
            random.seed(seed)
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for i in range(self.__num_cols):
            col = []
            for j in range(self.__num_rows):
                col.append(Cell(self.__win))
            self.__cells.append(col)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        if self.__win is None:
            return
        # Calculate the x/y position of the cell based on the i/j position and cell size
        x1 = self.__x1 + (i * self.__cell_size_x)
        y1 = self.__y1 + (j * self.__cell_size_y)
        x2 = self.__x1 + ((i + 1) * self.__cell_size_x)
        y2 = self.__y1 + ((j + 1) * self.__cell_size_y)
        # Draw the cell using Cell's draw() method
        self.__cells[i][j].draw(x1, y1, x2, y2)
        # Call the self._animate() method to animate the drawing of the cell
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        # Call the window's redraw() method
        self.__win.redraw()
        # Sleep for a short amount of time (0.05 sec) so that we can see the animation
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        # Remove the top wall of the top-left cell by setting has_top_wall = False (the entrance)
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        # Remove the bottom wall of the bottom-right cell (the exit)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i: int, j: int):
        # Mark the current cell as visited
        self.__cells[i][j].visited = True
        # In an infinite loop:
        while True:
            # Check the cells that are directly adjacent to the current cell
            adjacent_cell_coords = list(
                set(
                    [
                        (max(i - 1, 0), j),
                        (min(i + 1, self.__num_cols - 1), j),
                        (i, min(j + 1, self.__num_rows - 1)),
                        (i, max(j - 1, 0)),
                    ]
                )
            )

            # Keep track of any that have not been visited as "possible direction" and move on
            possible_directions: list[tuple[int, int]] = []
            for coordinates in adjacent_cell_coords:
                if self.__cells[coordinates[0]][coordinates[1]].visited == False:
                    possible_directions.append(coordinates)

            # If there are zero directions you can go from the current cell,
            # then draw the current cell and return to break out of the loop
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            # Otherwise, pick a random direction
            direction_index = random.randrange(len(possible_directions))
            direction = possible_directions[direction_index]

            i_new = direction[0]
            j_new = direction[1]

            # Knock down the walls between the current cell and the chosen cell
            if i_new > i:
                # break right wall of current cell
                self.__cells[i][j].has_right_wall = False
                # break left wall of target cell
                self.__cells[i_new][j_new].has_left_wall = False
            if i_new < i:
                # break left wall of current cell
                self.__cells[i][j].has_left_wall = False
                # break right wall of target
                self.__cells[i_new][j_new].has_right_wall = False
            if j_new > j:
                # break bottom wall of current cell
                self.__cells[i][j].has_bottom_wall = False
                # brek top wall of target cell
                self.__cells[i_new][j_new].has_top_wall = False
            if j_new < j:
                # break top wall of current cell
                self.__cells[i][j].has_top_wall = False
                # break bottom wall of target cell
                self.__cells[i_new][j_new].has_bottom_wall = False

            # Move to the chosen cell by recursively calling __break_walls_r
            self.__break_walls_r(i_new, j_new)
