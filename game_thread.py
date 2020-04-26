import threading

import audio_process_functions
from games import Game


class gameThread(threading.Thread):
    def __init__(self, audio_ready, gui_event):
        threading.Thread.__init__(self)
        self.game = Game(audio_ready, gui_event)
        self.audio_ready = audio_ready
        self.gui_event = gui_event
        self.start()

    def run(self):
        self.gui_event.wait()
        self.setGame(self.gui_event.game)
        self.game.quit = False
        self.gui_event.clear()
        while not self.game.quit:
            self.game.playRound()
        # change game if needed
        if self.gui_event.change_game:
            self.run()

    def setGame(self, game_field):
        if game_field == "pan":
            self.game.processAudio = audio_process_functions.pan
        elif game_field == "eq":
            self.game.processAudio = audio_process_functions.eq
            print("Game is now EQ! :)))))")
