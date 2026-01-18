from graphics import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(100, 50, 150, 100)

    cell1.draw_move(cell2, False)

    maze = Maze(150, 100, 9, 9, 50, 50, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
