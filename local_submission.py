from game import *

def local_solver(logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared) -> list:
    return []

if __name__ == "__main__":
    new_game = App()
    new_game.tetris.solver = local_solver
    new_game.run()