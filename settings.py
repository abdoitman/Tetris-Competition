import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (47,48,51)

TILE_SIZE = 40
FIELD_RES = 10 * TILE_SIZE , 20 * TILE_SIZE     #standard tetris window is 10 blocks in width, 20 blocks in hieght

INIT_POS_OFFSET = vec(5, 10)

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
    'Z': (15, 237, 250)    #Cyan
}