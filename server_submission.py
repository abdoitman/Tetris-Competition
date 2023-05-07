#########################################
## WELCOME TO THE CONTEST, HAVE FUN !! ##
#########################################
### ENTER THE REQUIRED INFO ABOUT THE TEAM TO GET STARTED WITH THE GAME ###
## REMEMBER THAT YOU WILL GET ONLY 10 SUBMISSIONS TO THE SERVER BUT YOU ###
## CAN TRY LOCALLY AS MUCH AS YOU WANT ##
#########################################

##########################
# Enter the ID (consisting of 8 characters)
# that was given to your team leader.
TEAM_ID = "test2"
NAME = ""
##########################

from game.game import *

def server_solver(logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared) -> list:
    return []

if __name__ == "__main__":
    server_game = App(server= True, Team_id= TEAM_ID)
    server_game.tetris.solver = server_solver
    server_game.run()