import random
import winsound

from pydub import AudioSegment


def exportFile(proc_sound):
    proc_sound.export("processed.wav", format="wav")


def playFile(file):
    winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_ALIAS)


def stop():
    winsound.PlaySound(None, winsound.SND_ASYNC)


def getSoundFromFile(file_name):
    if file_name.endswith("wav"):
        return AudioSegment.from_wav(file=file_name)
    elif file_name.endswith("mp3"):
        return AudioSegment.from_mp3(file=file_name)


def pan(file_name):
    sound = getSoundFromFile(file_name)
    pan_value = random.uniform(-1, 1)
    # cut to 30 seconds, set to mono and pan
    sound = sound.set_channels(1)[:30 * 1000]
    proc_sound = sound.pan(pan_value)
    exportFile(proc_sound)
    return pan_value
