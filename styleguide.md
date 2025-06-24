<!-- --------------------------------------------------- -->
<!--          Style Guide for Group 3 Breakout           -->
<!-- --------------------------------------------------- -->
<!-- To check a box, use an X: `[X]`-->
<!-- Just delete anything we don't use-->

# Phase I (6/24 - 7/6)

## UI Design
### Size and Layout
<!-- Sizes are all in pixels -->
- Window size:
  - Height: 600
  - Width: 550
- Title text location: top of screen
- Title and stats kept in a header 50-60px tall
  - Border-bottom 3px solid white;
- *Credits location (e.g. under title)*:
- Welcome screen:
  - Instructions to press start: "Press any key to play"
  - Change to gameplay when user hits a key to start
- Stats used in Phase 1:
  - Current score
  - Number of lives
  - Current level
- Stats location:
  - Level: top left
  - Lives and score: top right
- Game Over is a seperate game screen 
- No play again buttons, just text instructions
  - Located at bottom of screen
  - "Retry (R)"
  - "Quit (Q)"
- Paddle size: 
  - Height: 20
  - Width: 100
- Ball size (radius): 5
- Brick size:
  - Height: 20
  - Width: 40
  - Space between them: 
  - Distance from left wall: 5
  - Distance from right wall: 5
  - Starting distance from top wall: 5px under header border
  - Starting distance from bottom: 50

### Content
- Title: BREAKOUT
- Credits:
- Instructions to press start (if any): "PRESS ANY KEY TO PLAY"
- Stats text:
  - "Score"
  - "Lives"
  - "Level"
- Game Over text:
  - GAME OVER
  - [tentative leaderboard]
- No play again buttons, just text instructions
  - Located at bottom of screen
  - "Retry (R)"
  - "Quit (Q)"
- No win-condition text; a user continues until lives = 0. There's no "winning". 

### Fonts
- Font for everything: [Chakra Petch](https://fonts.google.com/specimen/Chakra+Petch?preview.text=PRESS+ANY+KEY+TO+PLAY)
- Font size for headings (in px): 34px for h1, 32px for h2, 26 for h3
- Font size for other/body text (in px): 16px

### Colors (pygame uses RGB)
- Screen background is always black: rgb(0,0,0)
- All text is white: rgb(255,255,255)
- Brick colors: 
  - RED: rgb(232, 20, 5)
  - YELLOW: rgb(232, 228, 5)
  - GREEN: rgb(11, 230, 62)
- Paddle color: rgb(34, 147, 240)
- Ball color: white rgb(255,255,255)

## Gameplay
- Maximum number of lives:
- Base scoring:
  - Red bricks: 5 points
  - Yellow bricks: 3 points
  - Green bricks: 1 point
- Ball speed:
- Paddle speed:
- Controls for movement (which keyboard keys):
  - Left:
  - Right: 
  - Quit: "Q"
  - Restart: "R"

# Phase 2 (Start 7/9 *if* we're 100% done with all Phase 1 features)

## Animation for ball colliding with bricks
<!-- Any ideas or details -->

## Sound
- Welcome/on load
  - Asset name:
  - Asset attribution text:
- Ball collides with brick
  - Asset name:
  - Asset attribution text:
- Ball collides with floor
  - Asset name:
  - Asset attribution text:
- Ball collides with wall
  - Asset name:
  - Asset attribution text:
- Ball collides with paddle
  - Asset name:
  - Asset attribution text:
- Background music for gameplay
  - Asset name:
  - Asset attribution text:
- Sound for losing a life
  - Asset name:
  - Asset attribution text:
- Game over sound
  - Asset name:
  - Asset attribution text:

## Bonus scoring system
<!-- Any ideas or details -->

## Casual v. Hard mode
<!-- Any ideas or details -->

## Local multiplyer mode
<!-- Any ideas or details -->
### Playing at the same time
1. A paddle would be on each side of the screen with the bricks in a column in the middle. The users would take turns trying to hit the bricks. The user who hits the last brick wins.
2. Split-window, with any win system (pong, score-based, who runs out of lives first)

### Either playing at the same time or turn-based
2. A pong-type game where the first person to miss first loses
3. Score-based, whoever hits the most bricks wins.