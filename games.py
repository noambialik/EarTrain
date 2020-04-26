import os
import random
from time import sleep

import audio_process_functions


class Game:
    def __init__(self, audio_ready, gui_event):
        self.gui_event = gui_event
        self.audio_ready = audio_ready
        self.quit = False
        self.processAudio = None

    def getRandomFile(self):
        return "songs/" + random.choice(os.listdir("songs/"))

    def playRound(self):
        # create processed audio file
        target = self.processAudio(file_name=self.getRandomFile())
        audio_process_functions.playFile("processed.wav")
        # signal to GUI that audio is playing
        self.audio_ready.set(target)

        # wait for answer from user
        self.gui_event.wait()
        audio_process_functions.stop()
        if self.gui_event.quit:
            self.quit = True
            return
        self.gui_event.clear()
        if self.gui_event.success:
            audio_process_functions.playFile("sounds/woohoo.wav")
        else:
            audio_process_functions.playFile("sounds/doh.wav")
        sleep(1)


# class PanGame(Game):
#     def processFile(self):
#         self.sound = self.getSoundFromRandomFile()
#         self.panValue = random.uniform(-1, 1)
#         # cut to 30 seconds, set to mono and pan
#         self.sound = self.sound.set_channels(1)[:30 * 1000]
#         self.proc_sound = self.sound.pan(self.panValue)
#
#         self.exportFile()
#
#     def playRound(self):
#         self.processFile()
#         super().playRound()


# class EqGame(Game):
#     def __init__(self):
#         super().__init__()
#         self.sound = None
#         self.fx = (AudioEffectsChain().equalizer(1000, q=2, db=25.0))
#
#     def processFile(self):
#         self.sound = self.getSoundFromRandomFile()[:30 * 1000]
#         samples = self.sound.get_array_of_samples()
#         self.proc_sound = self.sound._spawn(samples)
#         self.exportFile()
#         self.playFile("processed.wav")
#
#     def test(self):
#         # cut file
#         self.sound = self.getSoundFromRandomFile()
#         self.proc_sound = self.sound[:30 * 1000]
#         self.exportFile()
#         self.fx("processed.wav", "processed_1.wav")
#         self.playFile("processed_1.wav")


# if __name__ == "__main__":
#     print("Running...")
#     eq = EqGame()
#     # eq.processFile()
#     eq.test()
#     print("Done!")
