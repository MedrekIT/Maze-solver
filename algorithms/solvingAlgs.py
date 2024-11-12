from maze.Maze import *
from algorithms.generationAlgs import *

# Breadth first search maze solving algorithm
# Methods are static to avoid 'self'
class BFS:
    # Similar to DFS method in generationAlgs, but here we check if there is a path to a neighbor
    @staticmethod
    def checkNeighbors(currCell, mazeGrid):
        neighbors = []
        top = DFS.checkCell(currCell.x, currCell.y - 1, mazeGrid)
        bottom = DFS.checkCell(currCell.x, currCell.y + 1, mazeGrid)
        left = DFS.checkCell(currCell.x - 1, currCell.y, mazeGrid)
        right = DFS.checkCell(currCell.x + 1, currCell.y, mazeGrid)

        if top and not currCell.walls['top']:
            neighbors.append(top)
        if bottom and not currCell.walls['bottom']:
            neighbors.append(bottom)
        if left and not currCell.walls['left']:
            neighbors.append(left)
        if right and not currCell.walls['right']:
            neighbors.append(right)

        return neighbors

    # Algorithm which goes through cells, remembers path to certain cell, and seeks for finishing cell
    @staticmethod
    def pathFinding(mazeGrid, visited: list):
        cellsQueue: list = [mazeGrid[0]]
        cameFrom = {mazeGrid[0]: None}
        path = []

        # Loop goes until it finds finish, if some cell is a dead end, algorithm continues for another cells
        while len(cellsQueue) > 0:
            visitedCell = cellsQueue.pop(0)
            if visitedCell.finish:
                while visitedCell:
                    path.append(visitedCell)
                    visitedCell = cameFrom[visitedCell]

                for cell in path:
                    drawCell(cell, (70, 255, 70))
                    pg.display.update()
                break

            for cell in visited:
                drawCell(cell, (255, 255, 255))
                pg.display.update()

            neighbors = BFS.checkNeighbors(visitedCell, mazeGrid)
            for neighbor in neighbors:
                if neighbor not in visited:
                    cellsQueue.append(neighbor)
                    visited.append(neighbor)
                    cameFrom[neighbor] = visitedCell
                    drawCell(neighbor, (255, 70, 70))

            drawCell(visitedCell, (255, 255, 70))
            pg.display.update()

        return path


class AStar:
    def starDef(self):
        pass