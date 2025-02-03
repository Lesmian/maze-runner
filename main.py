

from cell import Cell
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(Point(50, 100), Point(200, 250))

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(Point(250, 100), Point(400, 250))

    cell1.draw_move(cell2, True)

    win.wait_for_close()

main()