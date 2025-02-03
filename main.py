

from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 20), Point(50, 20)), "red")
    win.draw_line(Line(Point(50, 20), Point(150, 200)), "black")

    win.wait_for_close()

main()