
"""Generate custom sine wave .wav files for Breakout game sound effects."""

import wave
import os
import numpy as np


def create_dummy_wav(file_path, duration_seconds=0.25, sample_rate=44100, frequency=440):
    """
    Generate a mono sine wave and save it as a .wav file.

    Parameters:
        file_path (str): Output path for the .wav file.
        duration_seconds (float): Length of the sound in seconds. Default is 0.25 seconds.
        sample_rate (int): Number of samples per second (Hz). Default is 44100 Hz.
        frequency (int): Frequency of the sine wave in Hz. Default is 440 Hz (A4 note).

    This function creates a simple tone using NumPy and writes it to a WAV file
    using Python's built-in wave module. The output is a 16-bit PCM mono file.
    """

    n_samples = int(sample_rate * duration_seconds)
    t = np.linspace(0, duration_seconds, n_samples, False)
    audio = 0.2 * np.sin(2 * np.pi * frequency * t)
    audio = (audio * 32767).astype(np.int16)

    with wave.open(file_path, 'w') as wf:
        wf.setnchannels(1)  # pylint: disable=no-member
        wf.setsampwidth(2)  # pylint: disable=no-member
        wf.setframerate(sample_rate)  # pylint: disable=no-member
        wf.writeframes(audio.tobytes())  # pylint: disable=no-member


# Folder setup
os.makedirs("assets/sounds", exist_ok=True)
os.makedirs("assets/music", exist_ok=True)

# sounds and associated frequencies
sound_map = {
    "brick_hit.wav": 880,
    "wall_hit.wav": 660,
    "paddle_hit.wav": 550,
    "floor_hit.wav": 330,
    "life_lost.wav": 220,
    "game_over.wav": 110,
    "startup.wav": 990
}

# Generate each .wav file
for name, freq in sound_map.items():
    path = os.path.join("assets/sounds", name)
    create_dummy_wav(path, frequency=freq)

# looping background tone
create_dummy_wav("assets/music/background.wav",
                 duration_seconds=3.0, frequency=260)
