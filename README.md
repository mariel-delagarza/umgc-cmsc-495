# Breakout Game in Python
This is an implementation of the classic arcade game 'Breakout'. The user begins with 3 lives and a score of 0.

The user controls a paddle at the bottom of the screen that can move left and right. A small ball bounces around the screen and when the ball collides with:
- The paddle, it bounces off the paddle
- The left and right walls or bottom of the header, it bounces off
- A brick, the brick disappaers, the ball bounces off, and the user is awarded points
- The bottom of the screen, 1 life is lost.

Red bricks are worth 5 points, yellow bricks are worth 3 points, green bricks are worth 1 point. When all lives are lost, the game is over and the user may press `R` to restart or `Q` to quit the program.



## To run
- Make sure you have python3 and `pygame` installed on your computer. If needed, check the [`pygame` install documentation](https://www.pygame.org/wiki/GettingStarted).
- In your terminal, run `python3 main.py` to start the program.
- To force quit the program, enter `ctrl + C` in your terminal.

## To play
- From the welcome screen, press `SPACE` to start.
- During gameplay:
  - Press `P` to pause and unpause.
  - Use left and right arrow keys to move paddle left and right.
- When game ends:
  - Press `R` to restart (after restarting, instructions will display to press `SPACE` to begin gameplay and `P` to pause/unpause).
  - Press `Q` to quit and close the program.
  
### Hard Mode
- At the welcome screen, press 'H' to enable hard mode.
- Press 'SPACE' to start.
- The game will load with 1 life instead of 3.

## To contribute
- Create a branch with a clear name. For example:
  - Issue-12
  - feat/new-feature-name
  - bug/bug-name
- Create a pull request and assign any group member(s) to review
