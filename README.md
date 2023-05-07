# Tetris-Competition
Files needed to participate in the friendly Tetris contest either to run the game locally or to submit a solution to the server.

## Table of Contents
* __[About The Contest](#about-the-contest)__
* __[The Game](#the-game)__
  - __[Game Field](#game-field)__
  - __[Tetrominos](#tetrominos)__
    + __[Tetromino Movement](#tetromino-movement)__
    + __[7-Bag Randomizer](#7-bag-randomizer)__
  - __[Game Rules](#game-rules)__
  - __[How to Play](#how-to-play)__
* __[Scoring](#scoring)__
* __[Submitting to API](#submitting-to-api)__

## [About The Contest](#about-the-contest)
The contest is a game of **Tetris** where each team will try to *implement the best algorithm* to play the game and score the most points in **90 seconds** by clearing more and more lines.

<p align=center> <img src="https://user-images.githubusercontent.com/77892920/236681580-946a45b8-54d2-49a9-80f6-5d39b1529ad3.png"> </p>

Each team can try and play the game locally **as many times as they wish** but will only have **10** submissions to the API from which their score will be calculated.<br>
Although each team have 10 submissions to the API, their final ranking among other teams will be based on the **average of their highest 3 runs**.

## [Game Field](#game-field)
The game field of a game of tetris consists of **10** tiles in width and **20** tiles in height with the falling point of the tetrominos in the middle of top row.

<p align= "center"><img src = "https://user-images.githubusercontent.com/77892920/236684174-62a63fc2-083f-490f-83ca-b54bb7a2165c.png"></p>

## [Tetrominos](#tetrominos)
In the game, there are 7 shapes (tetrominos) that you'll be moving and playing with which are: **L, J, S, Z, O, T, and I tetrominos**. Each of the 7 falling tetrominos (shapes) consists of **4 blocks** with different combination describing the tetromino.
**Note that** on the game grid, the y axis is inverted, meaning that **downwards** is the positive y direction. Also the **falling point** of the tetrominos is *(0, 5)*. 

To represent a Tetromino, consider an origin point that all building blocks will be placed relative to, then the tetrominos are as following:<br>
<p align= "center"><img src = "https://user-images.githubusercontent.com/77892920/236688970-261ba5e1-1379-4c1b-8eeb-bf927352c423.png"> </p>

### [Tetromino Movement](#tetromino-movement)
**Note**: The game has an FPS of 120, which means the tetrominos fall at a rate of **2 tiles per second**.<br>
Tetrominos can have to types of controlled movements:<br>
1. **Linear Movement**: Moving **right**, **left**, and, **downwards**. <br>

    * Each tetromino falls by it's **origin point**; meaning that at the tetromino always starts falling **with its origin point on (0,5)**.
    * Moving a tetromino downwards will cause it to **hard drop** untill it hits another tetromino or the ground.
2. **Rotational Movement**: Rotating **Clockwise** and **Conter-Clockwise**. <br>

    * When rotating a tetromino, it rotates around its **origin point** and it won't rotate if it's *new position* afterwards will be **coliding with a wall** or **another tetromino**.

