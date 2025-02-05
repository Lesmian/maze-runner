import random
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
        seed = None
    ):
        self.start_point = Point(x1, y1)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        self._draw_cell(0, 0)

        end_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        end_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i + 1 < self.num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j + 1 < self.num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randint(0, len(to_visit) - 1)
            new_i, new_j = to_visit[direction]
            new_cell = self._cells[new_i][new_j]
            if new_i > i:
                cell.has_right_wall = False
                new_cell.has_left_wall = False
            elif new_i < i:
                cell.has_left_wall = False
                new_cell.has_right_wall = False
            elif new_j > j:
                cell.has_bottom_wall = False
                new_cell.has_top_wall = False
            elif new_j < j:
                cell.has_top_wall = False
                new_cell.has_bottom_wall = False

            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        directions = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        for direction in directions:
             new_i, new_j = direction
             cell_exists = new_i >= 0 and new_i < self.num_cols and new_j >= 0 and new_j < self.num_rows
             has_wall = False
             if new_i > i and cell.has_right_wall:
                has_wall = True
             elif new_i < i and cell.has_left_wall:
                has_wall = True
             elif new_j > j and cell.has_bottom_wall:
                has_wall = True
             elif new_j < j and cell.has_top_wall:
                has_wall = True

             if cell_exists and not self._cells[new_i][new_j].visited and not has_wall:
                new_cell = self._cells[new_i][new_j]
                cell.draw_move(new_cell)
                result = self._solve_r(new_i, new_j)
                if result:
                    return result
                cell.draw_move(new_cell, True)

        return False

    def _animate(self):
        if self._win == None:
            return

        self._win.redraw()
        time.sleep(0.05)
    