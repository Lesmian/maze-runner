from line import Line
from point import Point


class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window

    def draw(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        if self._win == None:
            return

        if self.has_left_wall:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point1.x, point2.y)), "black")
        else:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point1.x, point2.y)), "#d9d9d9")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(point2.x, point1.y), Point(point2.x, point2.y)), "black")
        else:
            self._win.draw_line(Line(Point(point2.x, point1.y), Point(point2.x, point2.y)), "#d9d9d9")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point2.x, point1.y)), "black")
        else:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point2.x, point1.y)), "#d9d9d9")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(point1.x, point2.y), Point(point2.x, point2.y)), "black")
        else:
            self._win.draw_line(Line(Point(point1.x, point2.y), Point(point2.x, point2.y)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if self._win == None:
            return

        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        
        cell1_center = Point((self.point1.x + self.point2.x) / 2, (self.point1.y + self.point2.y) / 2)
        cell2_center = Point((to_cell.point1.x + to_cell.point2.x) / 2, (to_cell.point1.y + to_cell.point2.y) / 2)
        self._win.draw_line(Line(cell1_center, cell2_center), fill_color)
    
