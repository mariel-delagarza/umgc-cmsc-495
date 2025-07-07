"""Defines the Ball class for the Breakout game.

Handles ball rendering, movement, and collision with walls and the paddle.
"""

import pygame

# pylint: disable=no-member, invalid-name


class Ball:
    """
    Ball object that moves around the screen, bounces off walls, and interacts with the paddle.
    """
    # can remove speed_x values for adding difficulties later on.

    def __init__(self, screen_width, screen_height, speed_x=-3, speed_y=-4):
        """
        Initialize the ball at the center of the screen with specified speed and radius.

        Args:
            screen_width (int): Width of the game screen.
            screen_height (int): Height of the game screen.
            speed_x (int, optional): Initial horizontal speed. Defaults to -3.
            speed_y (int, optional): Initial vertical speed. Defaults to -4.
        """
        super().__init__()

        self.radius = 5
        self.x = int(screen_width // 2)
        self.y = int(screen_height // 1.5)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = (255, 255, 255)
        self.bottom_hit = False

        # Make a small surface to show the ball (needed for Pygame sprites)
        self.image = pygame.Surface(
            (self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        # Draw the ball as a white circle on that surface
        pygame.draw.circle(self.image, self.color,
                           (self.radius, self.radius), self.radius)

        # Create a rectangle used for collision detection
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # For drawing loop
    def draw(self, screen):
        """
        Draw the ball on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # For when paddle misses the ball, or game is restarted.
    def restart(self, screen_width, screen_height):
        """
        Reset the ball to the starting position (center).

        Args:
            screen_width (int): Width of the game screen.
            screen_height (int): Height of the game screen.
        """
        self.x = screen_width // 2
        self.y = screen_height // 1.5
        self.speed_y = -abs(self.speed_y)  # ensure it's going up

    def move(self):
        """
        Update the ball’s position based on its current velocity.
        """
        self.x += self.speed_x  # Move left/right
        self.y += self.speed_y  # Move up/down

        # Update the collision box to match the new position
        self.rect.center = (self.x, self.y)

    def bounce_walls(
            self,
            screen_width,
            screen_height,
            border_margin,
            border_thickness,
            padding_top):
        """
        Handle collision with screen walls and reverse direction as needed.

        Args:
            screen_width (int): Width of the screen.
            screen_height (int): Height of the screen.
            border_margin (int): Margin around the screen.
            border_thickness (int): Thickness of the screen border.
            padding_top (int): Padding below the top border (e.g. for UI labels).
        """
        # Bounds for collision
        left_bound = border_margin + border_thickness
        right_bound = screen_width - border_thickness - border_margin
        top_bound = border_margin + border_thickness + padding_top
        # Demo purposes
        bottom_bound = screen_height - border_thickness - border_margin

        # Actual collsion checking
        if self.x - self.radius <= left_bound or self.x + self.radius >= right_bound:
            self.speed_x *= -1
        if self.y - self.radius <= top_bound:
            self.speed_y *= -1
        if self.y + self.radius >= bottom_bound:
            self.bottom_hit = True

    def bounce_paddle(self, paddle_rect):
        """
        Bounce off the paddle, reversing vertical direction and 
        tweaking horizontal based on hit location.

        Args:
            paddle_rect (pygame.Rect): Rect of the paddle to check for collision.
        """
        if self.rect.colliderect(paddle_rect):
            # Calculate the hit position on the paddle
            ball_center = self.x
            paddle_center = paddle_rect.centerx

            # Always reverse Y
            self.speed_y *= -1

            # If hitting left edge of paddle → send ball more left
            if ball_center < paddle_center - 20:
                self.speed_x = -abs(self.speed_x)  # ensure it's going left
            # If hitting right edge of paddle → send ball more right
            elif ball_center > paddle_center + 20:
                self.speed_x = abs(self.speed_x)  # ensure it's going right
            # Else: center hit → don't adjust X
