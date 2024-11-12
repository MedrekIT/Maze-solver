from maze.Maze import *
import random as rd

# Depth first search maze generating algorithm
# Methods are static to avoid 'self'
class DFS:
    # Checking if neighbor is inside a grid
    @staticmethod
    def checkCell(x, y, mazeGrid):
        return None if x < 0 or x > cols - 1 or y < 0 or y > rows - 1 else mazeGrid[x + y * cols]

    # Choosing random unvisited neighbor to remove wall
    @staticmethod
    def checkNeighbors(currCell, mazeGrid):
        neighbors = []
        top = DFS.checkCell(currCell.x, currCell.y - 1, mazeGrid)
        bottom = DFS.checkCell(currCell.x, currCell.y + 1, mazeGrid)
        left = DFS.checkCell(currCell.x - 1, currCell.y, mazeGrid)
        right = DFS.checkCell(currCell.x + 1, currCell.y, mazeGrid)

        if top and not top.visited:
            neighbors.append(top)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        if right and not right.visited:
            neighbors.append(right)

        return rd.choice(neighbors) if neighbors else None

    # Removing wall between current cell and our neighbor
    @staticmethod
    def removeWalls(currCell, nextCell):
        dx = currCell.x - nextCell.x
        dy = currCell.y - nextCell.y
        if dx == 1:
            currCell.walls['left'] = False
            nextCell.walls['right'] = False
        if dx == -1:
            currCell.walls['right'] = False
            nextCell.walls['left'] = False
        if dy == 1:
            currCell.walls['top'] = False
            nextCell.walls['bottom'] = False
        if dy == -1:
            currCell.walls['bottom'] = False
            nextCell.walls['top'] = False

    # Coloring active cell to get animation effect
    @staticmethod
    def drawGeneration(currCell):
        pg.draw.rect(WIN, (255, 0, 0), (currCell.x * cellSize + 25, currCell.y * cellSize + 25, cellSize, cellSize))

    # Going through whole algorithm for current cell
    @staticmethod
    def mazeGeneration(currCell, mazeGrid, visitedCells):
        # Checking if cell has any unvisited neighbors, then removing walls between this cell and random neighbor
        nextCell = DFS.checkNeighbors(currCell, mazeGrid)
        if nextCell:
            nextCell.visited = True
            visitedCells.append(nextCell)
            DFS.removeWalls(currCell, nextCell)
            currCell = nextCell
        elif visitedCells:
            currCell = visitedCells.pop()
        return currCell