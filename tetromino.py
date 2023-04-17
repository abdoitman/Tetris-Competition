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
    
    def update_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.update_rect_pos()
    
    def is_colided(self, pos):
        x, y = int(pos.x) , int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H:
            return False
        return True

class Tetromino:
    def __init__(self, tetris) -> None:
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS_SHAPE.keys()))
        self.color = TETROMINOS_COLOR[self.shape]
        self.blocks = [Block(self, pos, self.color) for pos in TETROMINOS_SHAPE[self.shape]]

    def is_colided(self, blocks_positions):
        return any(map(Block.is_colided, self.blocks, blocks_positions))   

    def move(self, direction):
        moving_direction = MOVING_DIRECTIONS[direction]

        new_positions = [block.pos + moving_direction for block in self.blocks]
        is_colided = self.is_colided(new_positions)
        
        if not is_colided:
            for block in self.blocks:
                block.pos += moving_direction

    def update(self):
        self.move(direction='down')