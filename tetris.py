from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)

    def put_tetromino_in_field_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def check_if_tetromino_has_landed(self):
        if self.tetromino.landed:
            self.put_tetromino_in_field_array()
            self.tetromino = Tetromino(self)

    def control(self):
        pass

    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
            self.check_if_tetromino_has_landed()
        self.sprite_group.update()

    def draw(self):
        self.sprite_group.draw(self.app.screen)