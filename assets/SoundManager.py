import pygame
import os

class SoundManager:
    def __init__(self):
        # Initialize the mixer module in pygame so we can play sounds
        pygame.mixer.init()
        # Loads all the sound files when the SoundManager is created
        self.load_sounds()

    def load_sounds(self):
        # Dictionary that holds all sound effects with a name that can be called by later
        self.sounds = {
            "brick_hit": self.load("assets/sounds/brick_hit.wav"),      # Sound when ball hits a brick
            "wall_hit": self.load("assets/sounds/wall_hit.wav"),        # Sound when ball hits a wall
            "paddle_hit": self.load("assets/sounds/paddle_hit.wav"),    # Sound when ball hits paddle
            "floor_hit": self.load("assets/sounds/floor_hit.wav"),      # Sound when ball hits the bottom
            "life_lost": self.load("assets/sounds/life_lost.wav"),      # Sound effect for losing a life
            "game_over": self.load("assets/sounds/game_over.wav"),      # Sound played when game is over
            "startup": self.load("assets/sounds/startup.wav"),          # Sound played when game starts
        }

        # Store the file path for the background music
        self.background_music_path = "assets/music/background.wav"

    def load(self, path):
        # Checking if the sound file exists at the given path
        if os.path.exists(path):
            # Load and return the sound file if it exists
            return pygame.mixer.Sound(path)
        else:
            # Print a warning message if the file is not found
            print(f"Warning: Sound file not found: {path}")
            return None  # Return None

    def play_sound(self, name):
        # Get the sound from the dictionary using its name
        sound = self.sounds.get(name)
        # Play sound if the sound was found and loaded correctly
        if sound:
            sound.play()

    def play_music(self):
        # Check if the background music file exists
        if os.path.exists(self.background_music_path):
            # Load and play the background music
            pygame.mixer.music.load(self.background_music_path)
            # loop throughout the game
            pygame.mixer.music.play(-1)
        else:
            # If the music file is missing, show a warning
            print(f"Warning: Music file not found: {self.background_music_path}")

    def stop_music(self):
        # Stop the background music
        pygame.mixer.music.stop()
