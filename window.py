import pygame as pg

# Initializing most important variables
cols, rows, cellSize = 30, 20, 20
width, height = cols * cellSize + 50, rows * cellSize + 50

# PyGame window initialization
pg.init()
WIN = pg.display.set_mode((width, height))
pg.display.set_caption("Maze solver")

# Initializing program clock
clock = pg.time.Clock()