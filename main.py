

from cell import Cell
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(Point(50, 100), Point(200, 250))

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(Point(250, 100), Point(400, 250))

    win.wait_for_close()

main()