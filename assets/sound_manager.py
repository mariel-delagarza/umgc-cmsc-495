"""SoundManager module for handling sound effects and background music in the game."""

import os
import pygame


class SoundManager:
    """
    Manages loading and playback of sound effects and background music for the game.
    Initializes the pygame mixer and provides helper methods for sound control.
    """

    def __init__(self):
        """
        Initialize the SoundManager by setting up the pygame mixer
        and loading all required sound effects and music.
        """
        pygame.mixer.init()
        self.load_sounds()

    def load_sounds(self):
        """
        Load all predefined sound effect files into a dictionary for later use.
        Also stores the path for the looping background music track.
        """
        self.sounds = {
            "brick_hit": self.load("assets/sounds/brick_hit.wav"),
            "wall_hit": self.load("assets/sounds/wall_hit.wav"),
            "paddle_hit": self.load("assets/sounds/paddle_hit.wav"),
            "floor_hit": self.load("assets/sounds/floor_hit.wav"),
            "life_lost": self.load("assets/sounds/life_lost.wav"),
            "game_over": self.load("assets/sounds/game_over.wav"),
            "startup": self.load("assets/sounds/startup.wav"),
        }

        self.background_music_path = "assets/music/background.wav"

    def load(self, path):
        """
        Load a sound file from the given path.

        Parameters:
            path (str): The file path of the sound to load.

        Returns:
            pygame.mixer.Sound object if the file exists, otherwise None.
        """
        if os.path.exists(path):
            return pygame.mixer.Sound(path)
        else:
            print(f"Warning: Sound file not found: {path}")
            return None

    def play_sound(self, name):
        """
        Play a specific sound effect by name.

        Parameters:
            name (str): The name of the sound effect to play (e.g., 'brick_hit').
        """
        sound = self.sounds.get(name)
        if sound:
            sound.play()

    def play_music(self):
        """
        Play the looping background music, if the file exists.
        """
        if os.path.exists(self.background_music_path):
            pygame.mixer.music.load(self.background_music_path)
            pygame.mixer.music.play(-1)
        else:
            print(
                f"Warning: Music file not found: {self.background_music_path}")

    def stop_music(self):
        """
        Stop the currently playing background music.
        """
        pygame.mixer.music.stop()
