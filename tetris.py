from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current= False)            
        self.speed_up = False

    def put_tetromino_in_field_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(500)
            return True

    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H -1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

    def check_if_tetromino_has_landed(self):
        if self.tetromino.landed:
            if self.is_game_over():
                pg.quit()
                sys.exit()
            self.speed_up = False
            self.put_tetromino_in_field_array()
            self.next_tetromino.current = True
            self.tetromino = self.next_tetromino
            self.next_tetromino = Tetromino(self, current= False)
            pg.time.wait(500)
           
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        if pressed_key == pg.K_UP:
            self.tetromino.rotate()
        if pressed_key == pg.K_DOWN:
            self.speed_up =True

    def update(self):
        trigger =  [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_if_tetromino_has_landed()
        self.sprite_group.update()

    def draw(self):
        self.sprite_group.draw(self.app.screen)