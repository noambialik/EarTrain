import os
import random

from pysndfx import AudioEffectsChain


def getRandomFile():
    return "songs/" + random.choice(os.listdir("songs/"))


if __name__ == "__main__":
    print("Running...")
    fx = (AudioEffectsChain().equalizer(2000, db=10.0))
    fx("sounds/doh.wav", "proc_test_pysndfx.wav")
    print("Done!")
