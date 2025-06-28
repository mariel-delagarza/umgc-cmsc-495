"""Defines the Paddle class for the Breakout game.

Handles paddle rendering, movement, and edge constraints.
"""

import pygame


class Paddle:
    """
    Paddle controlled by the user. Handles drawing, movement, and boundary checking.
    """

    def __init__(
        self,
        screen_width,
        screen_height,
        color=(34, 147, 240),
        border_margin=0,
        border_thickness=0
    ):
        """
        Initialize the Paddle with size, position, and movement limits.
        """
        # Paddle size from style guide
        self.width = 100
        self.height = 20
        # Paddle color (default: blue)
        self.color = color
        # Paddle speed (pixels per frame)
        self.speed = 7  # Store as variable for future level-based speed increases
        # Start position: centered horizontally, 50px from bottom
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - 50 - self.height
        # Store as pygame.Rect for collision and movement logic
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.screen_width = screen_width
        self.border_margin = border_margin
        self.border_thickness = border_thickness

    def move_left(self):
        """
        Move the paddle left, staying inside the game border.
        """
        # Respect left game border
        left_limit = self.border_margin + self.border_thickness
        self.rect.x = max(left_limit, self.rect.x - self.speed)

    def move_right(self):
        """
        Move the paddle right, staying inside the game border.
        """
        right_limit = self.screen_width - self.border_margin - \
            self.border_thickness - self.width
        self.rect.x = min(right_limit, self.rect.x + self.speed)

    def draw(self, surface):
        """
        Draw the paddle on the provided surface.
        """
        pygame.draw.rect(surface, self.color, self.rect)
