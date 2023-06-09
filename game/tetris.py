from .settings import *
from .tetromino import Tetromino
from .bagrandomizer import *
import pygame.freetype as ft
import numpy as np

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.685, WIN_H * 0.02),
                            text= "Next", fgcolor= 'white', size= TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.6667, WIN_H * 0.32),
                            text= "Level", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.66, WIN_H * 0.39),
                            text= f"{self.app.tetris.level}", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.6667, WIN_H * 0.49),
                            text= "Lines", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.57),
                            text= f"{self.app.tetris.total_lines_cleared}", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.67),
                            text= "Score", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.742),
                            text= f"{self.app.tetris.score}", fgcolor= 'white', size= TILE_SIZE * 1.4)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.845),
                            text= "Time Left", fgcolor= 'white', size= TILE_SIZE * 1)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.888),
                            text= f"{self.app.counter // (FPS * 100)}", fgcolor= 'white', size= TILE_SIZE * 1.4)

class Tetris:
    def __init__(self, app) -> None:
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self, next(get_next_shape(self.app.seed)))
        self.next_tetromino = Tetromino(self, next(get_next_shape(self.app.seed)), current= False)            
        self.speed_up = False
        self.start_game = True

        self.level = 1
        self.score = 0
        self.full_lines = 0
        self.total_lines_cleared = 0
        self.moves = 0
        self.moves_info = []

    def get_score(self):
        self.score += POINTS_PER_LINE[self.full_lines] * self.level
        self.full_lines = 0

    def get_level(self):
        self.level = ( self.total_lines_cleared // 10 ) + 1 

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

                self.moves_info.append(self.moves)
                self.app.c_info.append(self.app.counter)
                self.full_lines += 1
                self.total_lines_cleared += 1

    def solver(self, logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared):
       return []

    def check_if_tetromino_has_landed(self):
        if self.tetromino.landed:
            if self.is_game_over():
                pg.time.wait(1000)
                pg.quit()
                self.app.running = False
                return
            self.speed_up = False
            self.put_tetromino_in_field_array()
            self.next_tetromino.current = True
            self.tetromino = self.next_tetromino
            self.next_tetromino = Tetromino(self, next(get_next_shape(self.app.seed)), current= False)
            self.moves += 1

            self.state = self.return_state_info()
            controls = self.solver(*self.state)
            self.control_via_array(controls)

    def return_state_info(self):
        logical_field_array = np.array(self.field_array)
        indicies = np.nonzero(self.field_array)
        logical_field_array[indicies] = 1
        return (logical_field_array,
                self.tetromino.shape,
                self.next_tetromino.shape,
                self.app.counter // (100 * FPS),
                self.level,
                self.score,
                self.total_lines_cleared)

    def control_via_array(self, control_array):
        for control in control_array:
            if control[:3] == "MOV":
                if control[-1] == "D":
                    self.speed_up =True
                    break
                self.tetromino.move(direction= CONTROLS[control[-1]])
            elif control[:3] == "ROT":
                self.tetromino.rotate(direction= control[4:])

    def update(self):
        trigger =  [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.app.info["S"] = self.score
            self.app.info["LC"] = self.total_lines_cleared
            self.app.info["C"] = self.app.c_info
            self.check_full_lines()
            self.tetromino.update()
            self.check_if_tetromino_has_landed()
            self.get_score()
            self.get_level()
        self.sprite_group.update()

    def draw(self):
        self.sprite_group.draw(self.app.screen)