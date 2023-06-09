from .settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos, color):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_TETROMIO_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, color, (1, 1, TILE_SIZE-2, TILE_SIZE-2), border_radius=8)
        self.rect = self.image.get_rect()
    
    def check_if_alive(self):
        if not self.alive:
            self.kill()

    def rotate(self, pivot_pos, direction):
        translated = self.pos - pivot_pos
        if direction == 'CW':
            rotated = translated.rotate(90) #clockwise
        elif direction == 'CCW':
            rotated = translated.rotate(-90) #counter clockwise
        return rotated + pivot_pos

    def update_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.check_if_alive()
        self.update_rect_pos()
    
    def is_colided(self, pos):
        x, y = int(pos.x) , int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True

class Tetromino:
    def __init__(self, tetris, shape, current= True):
        self.tetris = tetris
        # self.shape = random.choice(list(TETROMINOS_SHAPE.keys()))
        self.shape = shape
        self.color = TETROMINOS_COLOR[self.shape]
        self.blocks = [Block(self, pos, self.color) for pos in TETROMINOS_SHAPE[self.shape]]
        self.landed = False
        self.current = current

    def is_colided(self, blocks_positions):
        return any(map(Block.is_colided, self.blocks, blocks_positions))   

    def rotate(self, direction):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos, direction) for block in self.blocks]

        if not self.is_colided(new_block_positions):
            for index, block in enumerate(self.blocks):
                block.pos = new_block_positions[index]

    def move(self, direction):
        moving_direction = MOVING_DIRECTIONS[direction]

        new_positions = [block.pos + moving_direction for block in self.blocks]
        is_colided = self.is_colided(new_positions)
        
        if not is_colided:
            for block in self.blocks:
                block.pos += moving_direction
        elif direction == 'down':
            self.landed = True

    def update(self):
        self.move(direction='down')