from graphics import Window, Line, Point


class Cell:

    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self.__win is None:
            return

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall == True:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall)

        if self.has_right_wall == True:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall)

        if self.has_top_wall == True:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall)

        if self.has_bottom_wall == True:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall)

    def draw_move(self, to_cell: Cell, undo: bool = False):
        line_color = "red" if undo == False else "gray"

        half_length = abs(self.__x2 - self.__x1) // 2
        self_center_x = half_length + self.__x1
        self_center_y = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        to_center_x = half_length2 + to_cell.__x1
        to_center_y = half_length2 + to_cell.__y1

        move = Line(
            Point(self_center_x, self_center_y), Point(to_center_x, to_center_y)
        )
        self.__win.draw_line(move, fill_color=line_color)
