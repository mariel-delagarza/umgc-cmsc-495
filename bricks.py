"""Defines brick layout, scoring, and collision logic for the Breakout game."""
import random
import pygame


# Set the size of each brick
BRICK_WIDTH = 40
BRICK_HEIGHT = 20

# Space between each brick and padding from screen edges
BRICK_SPACING = 5
BRICK_PADDING_LEFT = 30
BRICK_PADDING_TOP = 90

# List of brick colors and their scores
brick_colors = [
    {"color": (11, 230, 62), "score": 1},    # Green bricks = 1 point
    {"color": (232, 228, 5), "score": 3},    # Yellow bricks = 3 points
    {"color": (232, 20, 5), "score": 5}      # Red bricks = 5 points
]

# Define the Brick class
class Brick(pygame.sprite.Sprite):
    """Represents a single brick in the Breakout game."""

    def __init__(self, x, y, color, score):
        super().__init__()
        # Create a rectangle surface for the brick
        self.color = color
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)  # Fill the brick with the given color
        self.rect = self.image.get_rect(topleft=(x, y))  # Position the brick
        self.score = score  # Store the score value of this brick
        # Visual effect states
        self.flash_timer = 0
        self.shake_timer = 0
        self.original_pos = self.rect.topleft
        self.particles = []
        self.hit_flag = False

    def update(self):
        """Transforms brick layout by inverting color, shaking brick and """
        # Flash effect
        if self.flash_timer > 0:
            self.flash_timer -= 1
            inverted_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
            self.image.fill(inverted_color)
        elif self.hit_flag:
            self.image.fill((0, 0, 0))  # Fade to black after flash
        else:
            self.image.fill(self.color)

        # Shake effect
        if self.shake_timer > 0:
            self.shake_timer -= 1
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-2, 2)
            self.rect.topleft = (
                self.original_pos[0] + offset_x,
                self.original_pos[1] + offset_y,
            )
        else:
            self.rect.topleft = self.original_pos

        # Move particles
        for particle in self.particles[:]:
            particle["x"] += particle["dx"]
            particle["y"] += particle["dy"]
            particle["life"] -= 1
            if particle["life"] <= 0:
                self.particles.remove(particle)

    def draw_particles(self, surface):
        """Draws particles for brick hits."""
        for particle in self.particles:
            pygame.draw.circle(
                surface,
                particle["color"],
                (int(particle["x"]), int(particle["y"])),
                3
            )

# This function creates a grid of bricks across the screen
def create_brick_grid(screen_width, rows_per_color=2):
    """Creates a grid of bricks with specified rows per color."""

    bricks = pygame.sprite.Group()  # Create a group to hold all bricks

    # Calculate how many columns fit in the screen
    columns = (screen_width - BRICK_PADDING_LEFT * 2 +
               BRICK_SPACING) // (BRICK_WIDTH + BRICK_SPACING)

    # Go through each color (green, yellow, red)
    for color_info in brick_colors:
        # Add multiple rows for each color
        for row in range(rows_per_color):
            # Calculate the vertical position
            row_index = brick_colors.index(color_info) * rows_per_color + row
            y = BRICK_PADDING_TOP + row_index * (BRICK_HEIGHT + BRICK_SPACING)

            # Create bricks across this row
            for col in range(columns):
                x = BRICK_PADDING_LEFT + col * (BRICK_WIDTH + BRICK_SPACING)
                # Make a new brick with this color and position
                brick = Brick(x, y, color_info["color"], color_info["score"])
                bricks.add(brick)  # Add brick to the group

    return bricks  # Return the full group of bricks

# This function checks if the ball hit any bricks
def handle_ball_brick_collision(ball, bricks, score):
    """Checks for collisions between the ball and bricks and updates the score."""

    # Check if the ball's rectangle overlaps any bricks
    hit_bricks = pygame.sprite.spritecollide(ball, bricks, dokill=False)

    # For every brick the ball hits: reverse ball's vertical direction and add points for the brick
    for brick in hit_bricks:
        if not brick.hit_flag:
            ball.speed_y *= -1
            score += brick.score

            # Brick effects
            brick.flash_timer = 5
            brick.shake_timer = 10
            brick.hit_flag = True

            # Create particle burst
            for _ in range(15):
                brick.particles.append({
                    "x": brick.rect.centerx,
                    "y": brick.rect.centery,
                    "dx": random.uniform(-2, 2),
                    "dy": random.uniform(-2, 2),
                    "life": 10,
                    "color": brick.color
                })

    return score
