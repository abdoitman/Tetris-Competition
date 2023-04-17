import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = 'black'
INFO_BG_COLOR = 'darkgrey'

TILE_SIZE = 40
FIELD_SIZE = FIELD_W , FIELD_H = 10, 20
FIELD_RES = 10 * TILE_SIZE , 20 * TILE_SIZE     #standard tetris window is 10 blocks in width, 20 blocks in hieght

INIT_POS_OFFSET = vec(5, 0)

ANIM_TIME_INTERVAL = 500 #ms
FAST_ANIM_TIME_INTERVAL = 5 #ms

FIELD_SCALE_W , FIELD_SCALE_H = 1.7, 1
NEXT_TETROMIO_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
WIN_RES = WIN_W, WIN_H = FIELD_SCALE_W * FIELD_RES[0] , FIELD_SCALE_H * FIELD_RES[1]

TETROMINOS_SHAPE = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
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