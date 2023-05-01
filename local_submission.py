from game import *

def local_solver(logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared) -> list:

    if current_tetromino == 'S':
        return ['MOV_L', 'MOV_L', 'MOV_L', 'MOV_L', "MOV_D"]
    else:
        return ['MOV_R', 'MOV_R', 'MOV_R', 'MOV_R']


if __name__ == "__main__":
    new_game = App()
    new_game.tetris.solver = local_solver
    new_game.run()