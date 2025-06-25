# For the paddle the user controls to hit the ball

import pygame

class Paddle:
    """
    Paddle controlled by the user. Handles drawing, movement, and boundary checking.
    """
    def __init__(self, screen_width, screen_height, color=(34, 147, 240)):
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

    def move_left(self):
        # Move left, but don't go off screen
        self.rect.x = max(0, self.rect.x - self.speed)

    def move_right(self):
        # Move right, but don't go off screen
        self.rect.x = min(self.screen_width - self.width, self.rect.x + self.speed)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
