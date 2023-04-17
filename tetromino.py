from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos, color):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE_SIZE

class Tetromino:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS_SHAPE.keys()))
        self.color = TETROMINOS_COLOR[self.shape]
        self.blocks = [Block(self, pos, self.color) for pos in TETROMINOS_SHAPE[self.shape]]
        
    def update(self):
        pass