# __Tetris Competition__
![tetris-multicolored-pattern-4u7ed6koskqhcez1](https://user-images.githubusercontent.com/77892920/236696126-7109c136-e7a8-491e-aa3f-3e95ac2f6bf4.jpg)<br>
<p align= "center">Files needed to participate in the friendly Tetris contest either to run the game locally or to submit a solution to the server.</p>

## __Table of Contents__
* __[About The Contest](#about-the-contest)__
* __[The Game](#the-game)__
  - __[Game Field](#game-field)__
  - __[Tetrominos](#tetrominos)__
    + __[Tetromino Movement](#tetromino-movement)__
    + __[7-Bag Randomizer](#7-bag-randomizer)__
* __[How to Play](#how-to-play)__
* __[Scoring](#scoring)__
* __[Submitting to API](#submitting-to-api)__

<hr>

## __[About The Contest](#about-the-contest)__
The contest is a game of **Tetris** where each team will try to *implement the best algorithm* to play the game and score the most points in **90 seconds** by clearing more and more lines.

<p align=center> <img src="https://user-images.githubusercontent.com/77892920/236681580-946a45b8-54d2-49a9-80f6-5d39b1529ad3.png"> </p>

Each team can try and play the game locally **as many times as they wish** but will only have **10** submissions to the API from which their score will be calculated.<br>
Although each team have 10 submissions to the API, their final ranking among other teams will be based on the **average of their highest 3 runs**.
## [Game Field](#game-field)
The game field of a game of tetris consists of **10** tiles in width and **20** tiles in height with the falling point of the tetrominos in the middle of top row.<br>
The origin point of the game field sets at **the upper left corner** with the positive x-axis in the **right direction** and the positive y-axis in the **downward direction**.

<p align= "center"><img src = "https://user-images.githubusercontent.com/77892920/236684174-62a63fc2-083f-490f-83ca-b54bb7a2165c.png"></p>

<hr>

## [Tetrominos](#tetrominos)
In the game, there are 7 shapes (tetrominos) that you'll be moving and playing with which are: **L, J, S, Z, O, T, and I tetrominos**. Each of the 7 falling tetrominos (shapes) consists of **4 blocks** with different combination describing the tetromino.
**Note that** on the game grid, the y axis is inverted, meaning that **downwards** is the positive y direction. Also the **falling point** of the tetrominos is *(0, 5)*. 

To represent a Tetromino, consider an origin point that all building blocks will be placed relative to, then the tetrominos are as following:<br>
<p align= "center"><img src = "https://user-images.githubusercontent.com/77892920/236688970-261ba5e1-1379-4c1b-8eeb-bf927352c423.png"> </p>

<hr>

### __[Tetromino Movement](#tetromino-movement)__
**Note**: The game has an FPS of 120, which means the tetrominos fall at a rate of **2 tiles per second**.<br>
Tetrominos can have to types of **controlled movements**:<br>
1. **Linear Movement**: Moving **right**, **left**, and, **downwards**. <br>

    * Each tetromino falls by it's **origin point**; meaning that at the tetromino always starts falling **with its origin point on (0,5)**.
    * Moving a tetromino downwards will cause it to **hard drop** untill it hits another tetromino or the ground.
2. **Rotational Movement**: Rotating **Clockwise** and **Conter-Clockwise**. <br>

    * When rotating a tetromino, it rotates around its **origin point** and it won't rotate if it's *new position* afterwards will be **coliding with a wall** or **another tetromino**.
    
### __[7-Bag Randomizer](#7-bag-randomizer)__
7-bag randomizer is the algorithm determining which tetromino gets generated next based on some rules:<br>
  
  1. During the span of any 7 moves, each tetromino should get generated **at least once**.
  2. No tetromino should get generated 3 times in a row.<br>
  
This algorithms treats the randomization of the tetrominos as if they were drawn from a bag and refiling the bag when it gets empty.

<hr>

## __[How to Play](#how-to-play)__
First you need to install the required packages using:
```Python3
pip install -r requirements.txt
```
Secondly, to test your algorithm locally, go to `local_submission.py` file and implement the algorithm inside `local_solver` function:
```Python3
def local_solver(logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared) -> list:
    return []
```
At each state *(before the next tetromino starts falling)* this function will provide you with the following information:

  * **logical_map** : **20x10 binary numpy array** providing you with the state of game field, with each element representing a cell in the game field. Each element can be **0** if that cell is empty on the game field, or a **1** if that cell has a block.
  * **current_tetromino** : **String** representing the shape of the *falling* tetromino in *this* move.
  * **next_tetromino** : **String** representing the shape of the *faling* tetromino in *nex|t* move.
  * **time_left** : **Integer** indicating the time left in seconds.
  * **level** : **Integer** indicating the current level of the player. (Explained more in detail in *[Scoring](#scoring)*)
  * **lines_cleared** : **Integer** indicating the total lines cleared in the game so far.
  
The function should return a **list of instructions** to control the tetromino. Valid instructions are the following:
  - **"MOV_L"** → Makes the tetromino move *1 tile* to the **left** (if possible).
  - **"MOV_R"** → Makes the tetromino move *1 tile* to the **right** (if possible).
  - **"MOV_D"** → Makes the tetromino hard drop.
  
  - **"ROT_CW"** → Makes the tetromino **rotate clockwise** (if possible).
  - **"ROT_CCW"** → Makes the tetromino **rotate counter clockwise** (if possible).

<hr>

## __[Scoring](#scoring)__
Scoring points in the game depends solely on 2 parameters: `lines_cleared` at the time and `level` of the player.<br>
### Points per line
Points awarded after clearing the lines depends on how many lines are cleared in the single move according to the following table:
| Lines cleared | Points |
|:-------------:|:------:|
| 1             |   800  |
| 2             |  1200  |
| 3             |  1800  |
| 4             |  2000  |
### Level
Each run, the player starts at level **1**. After clearing **10** lines the player levels up.
### Total Score
After clearing any number of lines in a move, the points awarded for them are calculated. Then the total score gets updated as:

<p align="center"> $Score_{total} \mathrel{+}= points \enspace * \enspace level$ </p>

<hr>

## __[Submitting to API](#submitting-to-api)__
**First**, head to `server_submission.py` file and fill the `TEAM_ID` with your team_id. <br>
Similar to the local submission, to submit your algorithm to the API, fill `server_solver` function with your algorithm
```Python3
def server_solver(logical_map, current_tetromino, next_tetromino, time_left, level, score, lines_cleared) -> list:
    return []
```
This will send a GET request to the API to start the game and begin the trial for the team.<br>
**NOTE**: Unfortunately the API is currently down, therefore server submissions doesn't work.
