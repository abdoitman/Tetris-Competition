from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def update(self):
        self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.sprite_group.draw(self.app.screen)