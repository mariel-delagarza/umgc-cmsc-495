"""Breakout game main file: handles state switching, rendering, and input."""
import sys
import pygame
from paddle import Paddle  # Import the Paddle class
from ball import Ball  # Import the Ball class
# Import the Bricks class
from bricks import create_brick_grid, handle_ball_brick_collision
from scoreboard import Scoreboard  # Import the scoreboard class
from assets.sound_manager import SoundManager

# disable "pygame has no member" errors - it's a linter issue not a pygame issue.
# disable "invalid-name" - the actual constants are all uppercase as per PEP 8:
# "current_state" and "running" are not constants.
# pylint: disable=no-member, invalid-name

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600
FPS = 60
BORDER_MARGIN = 25  # Margin for the white border around the game area
BORDER_THICKNESS = 4  # Thickness of the white border

# Creates and initializes the SoundManager
sound = SoundManager()
sound.play_sound("startup")
sound.play_music()

# Colors
WHITE = (255, 255, 255)  # for the text and ball
BLACK = (0, 0, 0)  # for the background
RED = (232, 20, 5)  # for the bricks
YELLOW = (232, 228, 5)  # for the bricks
GREEN = (11, 230, 62)  # for the bricks
BLUE = (34, 147, 240)  # for the paddle

# Game states
WELCOME = "welcome"
GAMEPLAY = "gameplay"
GAME_OVER = "game_over"
LIFE_LOST = "life_lost"
current_state = WELCOME

# Game state variables
ball_active = False
initials_entered = False
player_initials = ""
input_active = False
initials_ready = False

# Font sizes
FONT_SIZE_TITLE = 40
FONT_SIZE_SUBTITLE = 20
FONT_SIZE_CREDITS = 16
FONT_SIZE_SCORE = 18

# Setup window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Instantiate the paddle (for gameplay)
paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, BLUE,
                BORDER_MARGIN, BORDER_THICKNESS)

# Instantiate scoreboard
scoreboard = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

# Font helper


def render_text(text, size, color, x, y, center=True, bold=False):
    """Render text on the screen with optional centering and bold styling."""
    font_path = (
        "assets/fonts/ChakraPetch-Bold.ttf"
        if bold else "assets/fonts/ChakraPetch-Regular.ttf"
    )
    font = pygame.font.Font(font_path, size)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(rendered, rect)


# Ball creation
game_ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

# Create bricks
brick_group = create_brick_grid(SCREEN_WIDTH)

# Initialize score variable
score = 0
lives = 3

# Main loop
clock = pygame.time.Clock()  # Initialize the clock for FPS control
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # This is placed here to prevent p & q from messing with initials
        if input_active and current_state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # Backspace to remove letter
                    player_initials = player_initials[:-1]
                elif event.unicode.isalpha() and len(player_initials) < 3:  # Allow typing of letters
                    player_initials += event.unicode.upper()
                    initials_ready = len(player_initials) == 3
                    # Automatically save when length reaches 3
                    if initials_ready:
                        scoreboard.save_score(score, player_initials)
                        input_active = False
                        initials_entered = True
            continue  # Needed to allow for Q and R to work

        # Change state on key press
        if event.type == pygame.KEYDOWN:
            # Pause Checks
            if event.key == pygame.K_p and current_state == GAMEPLAY and ball_active:
                paused = not paused
            # Restart after life lost
            elif event.key == pygame.K_SPACE and current_state == LIFE_LOST:
                current_state = GAMEPLAY
                paused = False  # unpause when resuming
                ball_active = True
            elif event.key == pygame.K_SPACE:
                if current_state == WELCOME:
                    sound.play_sound("startup")
                    current_state = GAMEPLAY
                    game_ball.draw(screen)
                    ball_active = True  # start moving on gameplay load
                elif current_state == GAMEPLAY:
                    ball_active = True
            # Restart during Game Over
            elif event.key == pygame.K_r and current_state == GAME_OVER:
                score = 0
                lives = 3
                paused = False  # no longer paused
                ball_active = False  # wait for user to start
                initials_entered = False
                input_active = False
                current_state = GAMEPLAY
                paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, BLUE,
                                BORDER_MARGIN, BORDER_THICKNESS)
                game_ball.restart(SCREEN_WIDTH, SCREEN_HEIGHT)
                brick_group.empty()
                brick_group = create_brick_grid(SCREEN_WIDTH)
            elif event.key == pygame.K_q and current_state == GAME_OVER:
                running = False

    # If score doesn't reach top 10, it will skip initial inputs
    if input_active and current_state == GAME_OVER:
        if scoreboard.top_scores(score):
            input_active = True
        else:
            input_active = False

    # (Optional) Add other key handling for GAME_OVER if needed

    screen.fill(BLACK)

    # Render based on paused status
    if current_state == GAMEPLAY:
        if not ball_active:
            render_text("PRESS SPACE TO START", FONT_SIZE_TITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-40, bold=True)
            render_text("PRESS 'P' TO PAUSE/UNPAUSE", FONT_SIZE_SUBTITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif paused:
            render_text("(P)AUSED", FONT_SIZE_TITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, bold=True)
    # Handle continuous key presses for paddle movement
    if not paused:
        if current_state == GAMEPLAY:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                paddle.move_left()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                paddle.move_right()

    # Render based on current state
    if current_state == WELCOME:
        # Title
        render_text("Welcome to Breakout!", FONT_SIZE_TITLE, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60, bold=True)
        # Subtitle
        render_text("Press SPACE to Start", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)

        render_text("Press 'P' to Pause/Unpause", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 2)
        # Credits
        render_text("CMSC495-6981 Group 3", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        render_text("By Rebecca Allen, Tej Charfi, Mariel de la Garza,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        render_text("Robel Girma, Veronica Hercules Villeda,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        render_text("William Hoover, Paige Ratliff-Jackson,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
        render_text("and Megan Weatherbee", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140)

    elif current_state in (GAMEPLAY, LIFE_LOST):
        # White border
        pygame.draw.rect(screen, WHITE,
                         (BORDER_MARGIN, BORDER_MARGIN, SCREEN_WIDTH - 2 *
                          BORDER_MARGIN, SCREEN_HEIGHT - 2*BORDER_MARGIN),
                         BORDER_THICKNESS)

        # Draw all the bricks on the screen
        brick_group.update()
        brick_group.draw(screen)

        # Draw brick particles
        for brick in brick_group:
            brick.draw_particles(screen)

        # UI Labels
        PADDING_TOP = 35
        PADDING_SIDE = 50

        # Top-left: LEVEL
        render_text("LEVEL", FONT_SIZE_SCORE, WHITE, PADDING_SIDE,
                    PADDING_TOP, center=False, bold=True)

        # Top-right: LIVES + SCORE
        RIGHT_X = SCREEN_WIDTH - PADDING_SIDE - 120
        render_text(f"LIVES: {lives}", FONT_SIZE_SCORE, WHITE, RIGHT_X,
                    PADDING_TOP, center=False, bold=True)
        render_text(f"SCORE: {score}", FONT_SIZE_SCORE, WHITE, RIGHT_X,
                    PADDING_TOP + 20, center=False, bold=True)

        # Horizontal underline (2px height)
        UNDERLNE_Y = PADDING_TOP + 45
        pygame.draw.line(screen, WHITE, (30, UNDERLNE_Y),
                         (SCREEN_WIDTH - 30, UNDERLNE_Y), 2)

        if current_state == GAMEPLAY and not paused and ball_active:
            game_ball.move()
            game_ball.bounce_walls(
                SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_MARGIN, BORDER_THICKNESS, PADDING_SIDE, sound)
            game_ball.bounce_paddle(paddle.rect, paddle, sound)

            # Check if the ball hit any bricks
            score = handle_ball_brick_collision(
                game_ball, brick_group, score, sound)

            # Life update
            if game_ball.bottom_hit:
                # Sound when ball hits the bottom
                sound.play_sound("floor_hit")
                sound.play_sound("life_lost")  # Sound when a life is lost
                lives -= 1
                game_ball.restart(SCREEN_WIDTH, SCREEN_HEIGHT)
                game_ball.bottom_hit = False
                if lives > 0:
                    current_state = LIFE_LOST
                    paused = False  # don't move until user resumes
                elif lives <= 0:
                    sound.play_sound("game_over")
                    sound.stop_music()
                    current_state = GAME_OVER
                    initials_entered = False
                    player_initials = ""

                    # Only activate input if score qualifies
                    if scoreboard.top_scores(score):
                        scoreboard.new_initials(score)
                        input_active = True
                    else:
                        input_active = False

        game_ball.draw(screen)

        if current_state == LIFE_LOST:
            render_text("LIFE LOST", FONT_SIZE_TITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40, bold=True)
            render_text(f"LIVES REMAINING: {lives}", FONT_SIZE_SUBTITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            render_text("PRESS SPACE TO START", FONT_SIZE_SUBTITLE, WHITE,
                        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)

        # Draw the paddle
        paddle.draw(screen)

    elif current_state == GAME_OVER:
        pygame.draw.rect(screen, WHITE,
                         (BORDER_MARGIN, BORDER_MARGIN, SCREEN_WIDTH - 2 *
                          BORDER_MARGIN, SCREEN_HEIGHT - 2 * BORDER_MARGIN),
                         BORDER_THICKNESS)

        # Title
        render_text("GAME OVER", FONT_SIZE_TITLE, WHITE,
                    SCREEN_WIDTH // 2, BORDER_MARGIN + 30, bold=True)

        # Horizontal underline (2px height)
        underline_y = PADDING_TOP + 45
        pygame.draw.line(screen, WHITE, (30, underline_y),
                         (SCREEN_WIDTH - 30, underline_y), 2)

        # Allows scoreboard to display
        if input_active:
            scoreboard.draw_scoreboard_initials(screen, player_initials)
        else:
            scoreboard.draw_scoreboard(screen, SCREEN_WIDTH)

        # Retry and Quit text at the bottom
        BOTTOM_Y = SCREEN_HEIGHT - BORDER_MARGIN - 30
        render_text("RETRY (R)", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH // 4, BOTTOM_Y, bold=True)
        render_text("QUIT (Q)", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH * 3 // 4, BOTTOM_Y, bold=True)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
