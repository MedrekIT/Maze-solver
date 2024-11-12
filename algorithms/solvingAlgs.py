from maze.Maze import *

class BFS:
    @staticmethod
    def checkCell(x, y, mazeGrid):
        return None if x < 0 or x > cols - 1 or y < 0 or y > rows - 1 else mazeGrid[x + y * cols]

    @staticmethod
    def checkNeighbors(currCell, mazeGrid):
        neighbors = []
        top = BFS.checkCell(currCell.x, currCell.y - 1, mazeGrid)
        bottom = BFS.checkCell(currCell.x, currCell.y + 1, mazeGrid)
        left = BFS.checkCell(currCell.x - 1, currCell.y, mazeGrid)
        right = BFS.checkCell(currCell.x + 1, currCell.y, mazeGrid)

        if top and not currCell.walls['top']:
            neighbors.append(top)
        if bottom and not currCell.walls['bottom']:
            neighbors.append(bottom)
        if left and not currCell.walls['left']:
            neighbors.append(left)
        if right and not currCell.walls['right']:
            neighbors.append(right)

        return neighbors

    @staticmethod
    def pathFinding(mazeGrid, visited: list):
        cellsQueue: list = [mazeGrid[0]]
        cameFrom = {mazeGrid[0]: None}
        path = []

        while len(cellsQueue) > 0:
            visitedCell = cellsQueue.pop(0)
            if visitedCell.finish:
                while visitedCell:
                    path.append(visitedCell)
                    visitedCell = cameFrom[visitedCell]

                for cell in path:
                    pg.draw.rect(WIN, (70, 255, 70), (cell.x * cellSize + 26, cell.y * cellSize + 26, cellSize - 1, cellSize - 1))
                    pg.display.update()
                break

            for cell in visited:
                pg.draw.rect(WIN, (255, 255, 255), (cell.x * cellSize + 26, cell.y * cellSize + 26, cellSize - 1, cellSize - 1))
                pg.display.update()

            neighbors = BFS.checkNeighbors(visitedCell, mazeGrid)
            for neighbor in neighbors:
                if neighbor not in visited:
                    cellsQueue.append(neighbor)
                    visited.append(neighbor)
                    cameFrom[neighbor] = visitedCell
                    pg.draw.rect(WIN, (255, 70, 70), (neighbor.x * cellSize + 26, neighbor.y * cellSize + 26, cellSize - 1, cellSize - 1))

            pg.draw.rect(WIN, (255, 255, 70), (visitedCell.x * cellSize + 26, visitedCell.y * cellSize + 26, cellSize - 1, cellSize - 1))
            pg.display.update()

        return path


class AStar:
    def starDef(self):
        pass