import os
import random
import time

import pygame

pygame.mixer.init()

# Optional: if you experience sound lag, pre-initialize with custom settings
# (must be called BEFORE pygame.mixer.init())
# pygame.mixer.pre_init(44100, -16, 2, 2048)

# Folder this script lives in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXTENSIONS = (".wav", ".mp3", ".ogg", ".flac")

# Scan the folder and load every sound file found
sounds = {}
for filename in sorted(os.listdir(SCRIPT_DIR)):
    if filename.lower().endswith(EXTENSIONS):
        try:
            sounds[filename] = pygame.mixer.Sound(os.path.join(SCRIPT_DIR, filename))
            print(f"Loaded {filename}")
        except pygame.error as e:
            print(f"Skipped {filename}: {e}")

if not sounds:
    raise SystemExit("No sound files found next to the script.")

names = list(sounds)

# Adjust volume if needed (0.0 to 1.0), e.g. for every sound:
# for s in sounds.values():
#     s.set_volume(0.8)

while True:
    time.sleep(0.4)
    # 1-in-9 chance each tick, same as before
    if random.randint(1, 5) == 1:
        choice = random.choice(names)
        print(f"Playing {choice}")
        sounds[choice].play()