import wave, os
import numpy as np

duration = 0.5  # seconds
frequency = 1000  # Hz
sample_rate = 44100

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
beep = 0.5 * np.sin(2 * np.pi * frequency * t)

with wave.open("tone.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes((beep * 32767).astype(np.int16).tobytes())
    
print(os.getcwd())