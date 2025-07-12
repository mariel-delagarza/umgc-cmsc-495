"""Defines the Scoreboard class for the Breakout game

Handles rendering, sorting and saving to scoreboard.txt"""
import os
import pygame

class Scoreboard:
    """
    Scoreboard tracks top ten scores in a seperate text file and allows players to add initials if
    high score is reached.
    """

    def __init__(self, screen_width, screen_height):
        """Will generate two different scoreboards depending on if the player manages to hit
        top ten scores.
        Calculates """
        super().__init__()

        self.new_score = 0
        # Colors
        self.white = (255, 255, 255)
        self.green = (11, 230, 62)
        # Spacing
        self.x = int(screen_width // 2)
        self.y = int(screen_height // 2)
        self.row_spacing = 35
        self.rank = self.x - 80
        self.score = self.x
        self.name = self.x + 100
        self.underline_y = 80
        self.row_y = self.underline_y + 80
        # Text manipulation
        self.size_subtitle = 48
        self.size_row = 30
        self.font_bold = "assets/fonts/ChakraPetch-Bold.ttf"
        self.font_path = "assets/fonts/ChakraPetch-Regular.ttf"
        self.max_entries = 10
        self.scoreboard_file = "scoreboard.txt"


    def render_text(self, screen, text, size, color, x, y, center=True, bold=False):
        """Render text on the screen with optional centering and bold styling."""
        font_path = self.font_bold if bold else self.font_path
        font = pygame.font.Font(font_path, size)
        rendered = font.render(text, True, color)
        rect = rendered.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        screen.blit(rendered, rect)

    def top_scores(self, score):
        """
        Checks load_scoreboard to see if new score is higher than the top scores.
        """
        scores = [s for s, n in self.load_scoreboard()]
        if len(scores) < self.max_entries:
            return True
        return score >= scores[-1] # Allows player to win ties

    def load_scoreboard(self):
        """
        Contains logic that will pull the text from the scoreboard file and allow the program
        to read it.
        """
        if not os.path.exists(self.scoreboard_file):
            return []

        # Open/Read files
        with open(self.scoreboard_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        entries = []

        # Split line by comma and into two parts
        for line in lines:
            parts = line.split(',')
            if len(parts) == 2:
                name = parts[0]
                try:
                    # Convert score from string to int
                    score = int(parts[1])
                    entries.append((score, name))
                except ValueError:
                    # Added to skip if not integer
                    continue
        # Return score descending based on scores
        return sorted(entries, key=lambda x: -x[0])[:self.max_entries]

    def new_initials(self, score):
        """
        Stores score so it can be checked in top_scores.
        """
        self.new_score = score  # store score so it can be checked in top_scores

    def draw_scoreboard_initials(self, screen, initials):
        """
        Handles scoreboard generation and allow new score to be assigned an integer.
        Also controls the color for new score entry.
        """
        # Combines new score with existing scores and marks new score as True for coloring later
        temp_entries = [(self.new_score, initials, True)] + [(score, name, False) for
                                                             score, name in
                                                             self.load_scoreboard()]

        # Sort by score descending, stable sort keeps new entry order at top if scores equal
        temp_entries = sorted(temp_entries, key=lambda x: -x[0])[:self.max_entries]

        # Subtitle SCOREBOARD
        self.render_text(screen, "SCOREBOARD", self.size_subtitle, self.white,
                         self.x, self.underline_y + 30, bold=False)

        # Loop top entries and render each row
        for index, (s, n, is_new) in enumerate(temp_entries):
            rank_str = f"{index + 1}{self.get_rank_suffix(index + 1)}"
            row_y = self.row_y + index * self.row_spacing

            # Color text to green if it's new, or keep it white
            row_color = self.green if is_new else self.white

            # Render rank, score and name for each row
            self.render_text(screen, rank_str, self.size_row, row_color, self.rank, row_y)
            self.render_text(screen, str(s), self.size_row, row_color, self.score, row_y)
            self.render_text(screen, n, self.size_row, row_color, self.name, row_y)

    def draw_scoreboard(self, screen, screen_width):
        """
        Handles scoreboard generation based on the existing scoreboard file.
        """
        # Subtitle SCOREBOARD
        self.render_text(screen, "SCOREBOARD", self.size_subtitle, self.white,
                         screen_width // 2, self.underline_y + 30, bold=False)

        # Load top scores from file
        leaderboard = self.load_scoreboard()

        # Loop top entries and render each row
        for index, (score, name) in enumerate(leaderboard):
            rank_str = f"{index + 1}{self.get_rank_suffix(index + 1)}"
            row_y = self.row_y + index * self.row_spacing

            # Render rank, score, and name for each row
            self.render_text(screen, rank_str, self.size_row, self.white, self.rank, row_y)
            self.render_text(screen, str(score), self.size_row, self.white, self.score, row_y)
            self.render_text(screen, name, self.size_row, self.white, self.name, row_y)

    def save_score(self, score, name):
        """
        Saves a new score into the scoreboard file.
        """
        entries = self.load_scoreboard()
        # Insert new score at the top
        entries.insert(0, (score, name))

        # Sort by score in descending order but keep same-score entries in order of insertion
        entries = sorted(entries, key=lambda x: -x[0])
        # Keep only top N entries
        entries = entries[:self.max_entries]
        with open(self.scoreboard_file, "w", encoding="utf-8") as file:
            for s, n in entries:
                file.write(f"{n},{s}\n")

    def get_rank_suffix(self, rank):
        """
         Allows suffix of numbers to be assigned appropriately.
        """
        if 10 <= rank % 100 <= 20:
            return "TH"
        return {1: "ST", 2: "ND", 3: "RD"}.get(rank % 10, "TH")
