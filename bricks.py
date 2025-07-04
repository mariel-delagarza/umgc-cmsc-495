import pygame

# Set the size of each brick
brick_width = 40
brick_height = 20

# Space between each brick and padding from screen edges
brick_spacing = 5
brick_padding_left = 5
brick_padding_top = 65  # Starts (5px below the 60px header)

# List of brick colors and their scores
brick_colors = [
    {"color": (11, 230, 62), "score": 1},    # Green bricks = 1 point
    {"color": (232, 228, 5), "score": 3},    # Yellow bricks = 3 points
    {"color": (232, 20, 5), "score": 5}      # Red bricks = 5 points
]


# Define the Brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color, score):
        super().__init__()
        # Create a rectangle surface for the brick
        self.image = pygame.Surface((brick_width, brick_height))
        self.image.fill(color)  # Fill the brick with the given color
        self.rect = self.image.get_rect(topleft=(x, y))  # Position the brick
        self.score = score  # Store the score value of this brick


# This function creates a grid of bricks across the screen
def create_brick_grid(screen_width, rows_per_color=2):
    bricks = pygame.sprite.Group()  # Create a group to hold all bricks

    # Calculate how many columns fit in the screen
    columns = (screen_width - brick_padding_left * 2 + brick_spacing) // (brick_width + brick_spacing)

    # Go through each color (green, yellow, red)
    for color_info in brick_colors:
        # Add multiple rows for each color
        for row in range(rows_per_color):
            # Calculate the vertical position
            row_index = brick_colors.index(color_info) * rows_per_color + row
            y = brick_padding_top + row_index * (brick_height + brick_spacing)

            # Create bricks across this row
            for col in range(columns):
                x = brick_padding_left + col * (brick_width + brick_spacing)
                # Make a new brick with this color and position
                brick = Brick(x, y, color_info["color"], color_info["score"])
                bricks.add(brick)  # Add brick to the group

    return bricks  # Return the full group of bricks


# This function checks if the ball hit any bricks
def handle_ball_brick_collision(ball, bricks, score):
    # Check if the ball's rectangle overlaps any bricks
    hit_bricks = pygame.sprite.spritecollide(ball, bricks, dokill=True)

    # For every brick the ball hits: reverse ball's vertical direction and add points for the brick
    for brick in hit_bricks:
        ball.speed_y *= -1  # Reverse ball's vertical direction
        score += brick.score  # Add points for the brick

    return score  # Return the updated score
