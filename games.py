import os
import random
import winsound
from time import sleep

from pydub import AudioSegment
from pysndfx import AudioEffectsChain

from myEventObject import GUI_EVENT
from mygui import GUI


class Game:
    def __init__(self):
        self.panValue = None
        self.proc_sound = None
        self.gui_event = GUI_EVENT()
        self.gui = GUI(self.gui_event)
        self.audio_ready = self.gui.getAudioReady()
        self.quit = False

    def getSoundFromRandomFile(self):
        file_name = self.getRandomFile()
        if file_name.endswith("wav"):
            return AudioSegment.from_wav(file=file_name)
        elif file_name.endswith("mp3"):
            return AudioSegment.from_mp3(file=file_name)

    def playFile(self, file):
        winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_ALIAS)

    def stop(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)

    def exportFile(self):
        self.proc_sound.export("processed.wav", format="wav")

    def getRandomFile(self):
        return "songs/" + random.choice(os.listdir("songs/"))

    def playRound(self):
        self.playFile("processed.wav")
        self.audio_ready.set(self.panValue)

        self.gui_event.wait()
        self.stop()
        if self.gui_event.quit:
            self.quit = True
            return
        self.gui_event.clear()
        if self.gui_event.success:
            self.playFile("sounds/woohoo.wav")
        else:
            self.playFile("sounds/doh.wav")
        sleep(1)


class PanGame(Game):
    def processFile(self):
        self.sound = self.getSoundFromRandomFile()
        self.panValue = random.uniform(-1, 1)
        # cut to 30 seconds, set to mono and pan
        self.sound = self.sound.set_channels(1)[:30 * 1000]
        self.proc_sound = self.sound.pan(self.panValue)

        self.exportFile()

    def playRound(self):
        self.processFile()
        super().playRound()


class EqGame(Game):
    def __init__(self):
        super().__init__()
        self.sound = None
        self.fx = (AudioEffectsChain().equalizer(1000, q=2, db=25.0))

    def processFile(self):
        self.sound = self.getSoundFromRandomFile()[:30 * 1000]
        samples = self.sound.get_array_of_samples()
        self.proc_sound = self.sound._spawn(samples)
        self.exportFile()
        self.playFile("processed.wav")

    def test(self):
        #cut file
        self.sound = self.getSoundFromRandomFile()
        self.proc_sound = self.sound[:30 * 1000]
        self.exportFile()
        self.fx("processed.wav", "processed_1.wav")
        self.playFile("processed_1.wav")


if __name__ == "__main__":
    print("Running...")
    eq = EqGame()
    # eq.processFile()
    eq.test()
    print("Done!")
