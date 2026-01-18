import time

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
        win: Window = None,
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
