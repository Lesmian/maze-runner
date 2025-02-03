from line import Line
from point import Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window

    def draw(self, point1, point2):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point1.x, point2.y)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(point2.x, point1.y), Point(point2.x, point2.y)), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(point1.x, point1.y), Point(point2.x, point1.y)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(point1.x, point2.y), Point(point2.x, point2.y)), "black")
    
