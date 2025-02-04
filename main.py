

from cell import Cell
from maze import Maze
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 4, 5, 50, 60, win)

    win.wait_for_close()

main()