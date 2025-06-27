# For the bouncing ball
import pygame

class Ball:
    # can remove speed_x values for adding difficulties later on. 
    def __init__(self, screen_width, screen_height, speed_x=-3, speed_y=-4):
        self.radius = 5
        self.x = int(screen_width // 2)
        self.y = int(screen_height // 1.5)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = (255,255,255)
        self.bottom_hit = False
    
    # For drawing loop
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # For when paddle misses the ball, or game is restarted.
    def restart(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 1.5
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_walls(self, screen_width, screen_height, border_margin, border_thickness, padding_side):
        # Bounds for collision
        left_bound = border_margin + border_thickness
        right_bound = screen_width - border_thickness - border_margin
        top_bound = border_margin + border_thickness + padding_side
        # Demo purposes
        bottom_bound = screen_height - border_thickness - border_margin

        # Actual collsion checking
        if self.x - self.radius <= left_bound or self.x + self.radius >= right_bound:
            self.speed_x *= -1
        if self.y - self.radius <= top_bound:
            self.speed_y *= -1
        if  self.y + self.radius >= bottom_bound:
            self.speed_y *= -1
            self.bottom_hit = True
            # Debug for flag
            print(self.bottom_hit)
