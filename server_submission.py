#########################################
## WELCOME TO THE CONTEST, HAVE FUN !! ##
#########################################
### ENTER THE REQUIRED INFO ABOUT THE ###
### TEAM TO GET STARTED WITH THE GAME ###
## REMEMBER THAT YOU WILL GET ONLY TEN ##
### SUBMISSIONS TO THE SERVER BUT YOU ###
## CAN TRY LOCALLY AS MUCH AS YOU WANT ##
#########################################

##########################
# Enter the ID (consisting of 8 characters)
# that was given to your team leader.
TEAM_ID = ""
##########################

from game import App



if __name__ == "__main__":
    game = App(server= True)
    game.run()