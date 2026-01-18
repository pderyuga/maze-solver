from graphics import Window, Point, Line


def main():
    print("Hello from maze-solver!")
    win = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(100, 100)
    line = Line(point1, point2)
    win.draw_line(line, fill_color="red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
