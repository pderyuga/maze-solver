from graphics import Window, Cell


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(50, 50, 100, 100)

    win.wait_for_close()


if __name__ == "__main__":
    main()
