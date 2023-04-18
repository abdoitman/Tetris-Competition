from settings import *
from tetromino import Tetromino
import pygame.freetype as ft

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.685, WIN_H * 0.02),
                            text= "Next", fgcolor= 'white', size= TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.6667, WIN_H * 0.32),
                            text= "Level", fgcolor= 'white', size= TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.66, WIN_H * 0.395),
                            text= f"{self.app.tetris.level}", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.6667, WIN_H * 0.52),
                            text= "Lines", fgcolor= 'white', size= TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.605),
                            text= f"{self.app.tetris.total_lines_cleared}", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.7),
                            text= "Score", fgcolor= 'white', size= TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.8),
                            text= f"{self.app.tetris.score}", fgcolor= 'white', size= TILE_SIZE * 1.4)

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current= False)            
        self.speed_up = False

        self.level = 1
        self.score = 0
        self.full_lines = 0
        self.total_lines_cleared = 0
        self.points_per_line = {
            0 : 0,
            1 : 800,
            2 : 1200,
            3 : 1800,
            4 : 2000
        }

    def get_score(self):
        self.score += self.points_per_line[self.full_lines] * self.level
        self.full_lines = 0

    def get_level(self):
        self.level = ( self.total_lines_cleared // 10 ) + 1 

    def update_level_speed(self):
        if self.level < 10:
            ANIM_TIME_INTERVAL = LEVEL_TIME_INTERVAL[self.level]
        elif self.level < 20:
            ANIM_TIME_INTERVAL = 100
        else:
            ANIM_TIME_INTERVAL = 50

    def put_tetromino_in_field_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(1500)
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

                self.full_lines += 1
                self.total_lines_cleared += 1

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
            self.get_score()
            self.get_level()
            self.update_level_speed()
        self.sprite_group.update()

    def draw(self):
        self.sprite_group.draw(self.app.screen)