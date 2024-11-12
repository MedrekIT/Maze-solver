from algorithms.generationAlgs import *
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
    generation = False

    # Application loop
    runWin: bool = True
    while runWin:
        # Program speed
        clock.tick(60)

        # Drawing a display and a grid
        WIN.fill((220, 220, 220))
        for i in mazeGrid:
            i.drawMaze()

        # Events and keyboard handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type == pg.KEYDOWN:
                # Maze generation
                if event.key == pg.K_g:
                    generation = True


        if generation:
            currCell = DFS.mazeGeneration(currCell, mazeGrid, visitedCells)

        # Animating generation
        DFS.drawGeneration(currCell)
        pg.display.update()

    pg.quit()