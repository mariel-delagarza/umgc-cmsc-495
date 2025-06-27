"""Breakout game main file: handles state switching, rendering, and input."""
import sys
import pygame
from paddle import Paddle  # Import the Paddle class
from ball import Ball

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

# Colors
WHITE = (255, 255, 255)  # for the text and ball
BLACK = (0, 0, 0)  # for the background
RED = (232, 20, 5)  # for the bricks
YELLOW = (232, 228, 5)  # for the bricks
GREEN = (11, 320, 62)  # for the bricks
BLUE = (34, 147, 240)  # for the paddle

# Game states
WELCOME = "welcome"
GAMEPLAY = "gameplay"
GAME_OVER = "game_over"
current_state = WELCOME
ball_active = False

# Font sizes
FONT_SIZE_TITLE = 40
FONT_SIZE_SUBTITLE = 20
FONT_SIZE_CREDITS = 16
FONT_SIZE_SCORE = 18

# Setup window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Instantiate the paddle (for gameplay)
paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, BLUE)

# Font helper


def render_text(text, size, color, x, y, center=True, bold=False):
    """Render text on the screen with optional centering and bold styling."""
    font_path = "assets/fonts/ChakraPetch-Bold.ttf" if bold else "assets/fonts/ChakraPetch-Regular.ttf"
    font = pygame.font.Font(font_path, size)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(rendered, rect)


# Main loop
clock = pygame.time.Clock()  # Initialize the clock for FPS control
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change state on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if current_state == WELCOME:
                    current_state = GAMEPLAY
<< << << < HEAD
            # (Optional) Add other key handling for GAME_OVER if needed
== == == =
                    # Ball creation
                    game_ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
                    game_ball.draw(screen)
                    ball_active = False
                elif current_state == GAMEPLAY:
                    current_state = GAME_OVER
            if event.key == pygame.K_RETURN:
                if current_state == GAMEPLAY:
                    ball_active = True                

>>>>>>> 768447d (Added ball, its movement, and some collision logic)

    screen.fill(BLACK)

    # Handle continuous key presses for paddle movement
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
        # Credits
        render_text("CMSC495-6981 Group 3", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
        render_text("By Rebecca Allen, Tej Charfi, Mariel de la Garza,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        render_text("Robel Girma, Veronica Hercules Villeda,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
        render_text("William Hoover, Paige Ratliff-Jackson,", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        render_text("and Megan Weatherbee", FONT_SIZE_CREDITS, WHITE,
                    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
    elif current_state == GAMEPLAY:
        # White border
        pygame.draw.rect(screen, WHITE,
                         (BORDER_MARGIN, BORDER_MARGIN, SCREEN_WIDTH - 2 *
                          BORDER_MARGIN, SCREEN_HEIGHT - 2*BORDER_MARGIN),
                         BORDER_THICKNESS)       
        
        # UI Labels
        PADDING_TOP = 35
        PADDING_SIDE = 50

        # Top-left: LEVEL
        render_text("LEVEL", FONT_SIZE_SCORE, WHITE, PADDING_SIDE,
                    PADDING_TOP, center=False, bold=True)

        # Top-right: LIVES + SCORE
        RIGHT_X = SCREEN_WIDTH - PADDING_SIDE - 120
        render_text("LIVES", FONT_SIZE_SCORE, WHITE, RIGHT_X,
                    PADDING_TOP, center=False, bold=True)
        render_text("SCORE", FONT_SIZE_SCORE, WHITE, RIGHT_X,
                    PADDING_TOP + 20, center=False, bold=True)

        # Horizontal underline (2px height)
        UNDERLNE_Y = PADDING_TOP + 45
        pygame.draw.line(screen, WHITE, (30, UNDERLNE_Y),
                         (SCREEN_WIDTH - 30, UNDERLNE_Y), 2)
        
        #Ball tracking DEMO
        if ball_active == True:
            game_ball.move()
            game_ball.bounce_walls(SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_MARGIN, BORDER_THICKNESS, PADDING_SIDE)
        game_ball.draw(screen)

        # Placeholder instruction text
        render_text("PLACEHOLDER: PRESS SPACE TO SEE GAME OVER", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH // 2, UNDERLNE_Y + 20, bold=False)

        # Draw the paddle
        paddle.draw(screen)
    elif current_state == GAME_OVER:
        # White border
        pygame.draw.rect(screen, WHITE,
                         (BORDER_MARGIN, BORDER_MARGIN, SCREEN_WIDTH - 2 *
                          BORDER_MARGIN, SCREEN_HEIGHT - 2*BORDER_MARGIN),
                         BORDER_THICKNESS)
        # Title
        render_text("GAME OVER", FONT_SIZE_TITLE, WHITE,
                    SCREEN_WIDTH // 2, BORDER_MARGIN + 30, bold=True)

        # Horizontal underline (2px height)
        underline_y = PADDING_TOP + 45
        pygame.draw.line(screen, WHITE, (30, underline_y),
                         (SCREEN_WIDTH - 30, underline_y), 2)

        # Leaderboard header
        render_text("LEADERBOARD", FONT_SIZE_SUBTITLE, WHITE,
                    SCREEN_WIDTH // 2, underline_y + 30, bold=True)

        # Table columns
        row_y_start = underline_y + 100
        ROW_SPACING = 25

        # Define x positions for columns
        X_RANK = SCREEN_WIDTH // 2 - 100
        X_SCORE = SCREEN_WIDTH // 2
        X_NAME = SCREEN_WIDTH // 2 + 100

        leaderboard = [
            ("1ST", "20", "PBC"),
            ("2ND", "10", "GWZ"),
            ("3RD", "3", "AAA")
        ]

        # Column headers
        column_y = row_y_start - ROW_SPACING  # one row height above the first row
        render_text("SCORE", FONT_SIZE_CREDITS, WHITE,
                    X_SCORE, column_y, center=True, bold=True)
        render_text("NAME", FONT_SIZE_CREDITS, WHITE,
                    X_NAME, column_y, center=True, bold=True)

        for i, (rank, score, name) in enumerate(leaderboard):
            row_y = row_y_start + i * ROW_SPACING
            render_text(rank, FONT_SIZE_CREDITS, WHITE,
                        X_RANK, row_y, center=True)
            render_text(score, FONT_SIZE_CREDITS,
                        WHITE, X_SCORE, row_y, center=True)
            render_text(name, FONT_SIZE_CREDITS, WHITE,
                        X_NAME, row_y, center=True)

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
