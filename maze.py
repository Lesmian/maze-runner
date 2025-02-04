import time
from cell import Cell
from point import Point


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.start_point = Point(x1, y1)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell_start_point = Point(
            self.start_point.x + i * self.cell_size_x, 
            self.start_point.y + j * self.cell_size_y
        )
        cell_end_point = Point(
            self.start_point.x + (i + 1) * self.cell_size_x, 
            self.start_point.y + (j + 1) * self.cell_size_y
        )
        cell.draw(cell_start_point, cell_end_point)
        self._animate()

    def _animate(self):
        if self._win == None:
            return

        self.win.redraw()
        time.sleep(0.05)
    