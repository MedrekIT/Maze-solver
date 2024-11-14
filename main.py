from algorithms.solvingAlgs import *
from maze.Maze import *
from window import *

if __name__ == '__main__':
    # Maze grid generation
    mazeGrid = Maze().grid
    mazeGrid[0].start = True
    mazeGrid[0].visited = True
    mazeGrid[len(mazeGrid) - 1].finish = True
    currCell = mazeGrid[0]
    visitedCells = [currCell]
    visitation = [currCell]
    path = []
    generation = False
    solved = False


    # Application loop
    runWin: bool = True
    while runWin:
        # Program speed
        clock.tick(60)

        # Drawing a display and a grid
        WIN.fill((220, 220, 220))
        for cell in mazeGrid:
            cell.drawMaze()

        # Events and keyboard handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.KEYDOWN:
                # Maze generation
                if event.key == pg.K_g:
                    generation = True
                # Grid regeneration
                if event.key == pg.K_r:
                    mazeGrid = Maze().grid
                    mazeGrid[0].start = True
                    mazeGrid[0].visited = True
                    mazeGrid[len(mazeGrid) - 1].finish = True
                    currCell = mazeGrid[0]
                    visitedCells = [currCell]
                    visitation = [currCell]
                    path = []
                    generation = True
                    solvig = False
                # Maze solving
                if event.key == pg.K_s and not generation:
                    path = BFS.pathFinding(mazeGrid, visitation, path)
                    solved = True

        if solved:
            for cell in path:
                pg.draw.rect(WIN, (70, 255, 70), (cell.x * cellSize + 26, cell.y * cellSize + 26, cellSize - 1, cellSize - 1))
            pg.draw.rect(WIN, (70, 70, 255), (mazeGrid[0].x * cellSize + 26, mazeGrid[0].y * cellSize + 26, cellSize - 1, cellSize - 1))
            pg.draw.rect(WIN, (70, 70, 255), (mazeGrid[-1].x * cellSize + 26, mazeGrid[-1].y * cellSize + 26, cellSize - 1, cellSize - 1))

        if generation:
            currCell = DFS.mazeGeneration(currCell, mazeGrid, visitedCells)
            # Animating generation
            drawCell(currCell, (255, 70, 70))
            if currCell.x == 0 and currCell.y == 0: generation = False

        pg.display.update()

    pg.quit()