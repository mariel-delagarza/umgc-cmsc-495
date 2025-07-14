
"""Generate custom sine wave .wav files for Breakout game sound effects."""

import wave
import numpy as np
import os


def create_dummy_wav(file_path, duration_seconds=0.25, sample_rate=44100, frequency=440):

    n_samples = int(sample_rate * duration_seconds)
    t = np.linspace(0, duration_seconds, n_samples, False)
    audio = 0.2 * np.sin(2 * np.pi * frequency * t)
    audio = (audio * 32767).astype(np.int16)

    with wave.open(file_path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())


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
