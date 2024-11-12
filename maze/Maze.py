from window import *

# Grid cell initialization
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'bottom': True, 'left': True, 'right': True}
        self.start = False
        self.visited = False
        self.finish = False

    # Drawing lines where walls are active
    def drawMaze(self):
        if self.walls['top']:
            pg.draw.line(WIN, (0, 0, 0), ((self.x * cellSize) + 25, (self.y * cellSize) + 25),
                         ((self.x * cellSize) + 25 + cellSize, (self.y * cellSize) + 25))
        if self.walls['bottom']:
            pg.draw.line(WIN, (0, 0, 0), ((self.x * cellSize) + 25, (self.y * cellSize) + 25 + cellSize),
                         ((self.x * cellSize) + 25 + cellSize, (self.y * cellSize) + 25 + cellSize))
        if self.walls['left']:
            pg.draw.line(WIN, (0, 0, 0), ((self.x * cellSize) + 25, (self.y * cellSize) + 25),
                         ((self.x * cellSize) + 25, (self.y * cellSize) + 25 + cellSize))
        if self.walls['right']:
            pg.draw.line(WIN, (0, 0, 0), ((self.x * cellSize) + 25 + cellSize, (self.y * cellSize) + 25),
                         ((self.x * cellSize) + 25 + cellSize, (self.y * cellSize) + 25 + cellSize))

# Implementing grid in the maze
class Maze:
    def __init__(self):
        self.grid = [Cell(col, row) for row in range(rows) for col in range(cols)]