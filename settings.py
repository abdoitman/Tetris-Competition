import pygame as pg
import random

vec = pg.math.Vector2

FPS = 120
GAME_DURATION = 90 #seconds
FIELD_COLOR = 'black'
INFO_BG_COLOR = (37,37,37)

FONT_PATH = "assets\Archive.otf"

TILE_SIZE = 40
FIELD_SIZE = FIELD_W , FIELD_H = 10, 20
FIELD_RES = 10 * TILE_SIZE , 20 * TILE_SIZE     #standard tetris window is 10 blocks in width, 20 blocks in hieght

INIT_POS_OFFSET = vec(5, 0)

ANIM_TIME_INTERVAL = 240 #ms
FAST_ANIM_TIME_INTERVAL = 1 #ms

FIELD_SCALE_W , FIELD_SCALE_H = 1.7, 1
NEXT_TETROMIO_OFFSET = vec(FIELD_W * 1.278, FIELD_H * 0.194)
WIN_RES = WIN_W, WIN_H = FIELD_SCALE_W * FIELD_RES[0] , FIELD_SCALE_H * FIELD_RES[1]

TETROMINOS_SHAPE = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (-1, 0), (-1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

TETROMINOS_COLOR = {
    'T': (221, 10, 178),  #Purple
    'O': (255, 145, 12),  #Orange
    'J': (253, 63, 89),   #Red
    'L': (57, 137, 47),   #Green
    'I': (5, 119, 210),   #Blue 
    'S': (254, 190, 46),  #Yellow
    'Z': (15, 237, 250)   #Cyan
}

MOVING_DIRECTIONS = {
    'left': vec(-1,0),
    'right': vec(1,0),
    'down': vec(0,1)
}

POINTS_PER_LINE = {
            0 : 0,
            1 : 800,
            2 : 1200,
            3 : 1800,
            4 : 2000
        }

LEVEL_TIME_INTERVAL = {
    1 : 600,
    2 : 540,
    3 : 480,
    4 : 420,
    5 : 360,
    6 : 300,
    7 : 240,
    8 : 180,
    9 : 120
}

CONTROLS = {
    'L' : "left",
    'R' : "right",
    'D' : "down"
}