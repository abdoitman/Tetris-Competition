from settings import *
import math

class Tetris:
    def __init__(self, app) -> None:
        self.app = app

    def draw_grid(self):
        for x in range(10):
            for y in range(20):
                pg.draw.rect(self.app.screen, 'black',
                             (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        pass

    def draw(self):
        self.draw_grid()