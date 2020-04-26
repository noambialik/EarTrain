import threading

import audio_process_functions
from games import Game
from myEventObject import CHOOSE_GAME_EVENT, GUI_EVENT


class gameThread(threading.Thread):
    def __init__(self, audio_ready, choose_game_event, gui_event):
        threading.Thread.__init__(self)
        self.game = Game(audio_ready, gui_event)
        self.audio_ready = audio_ready
        self.choose_game_event = choose_game_event
        self.gui_event = gui_event
        self.start()

    def run(self):
        self.choose_game_event.wait()
        self.setGame(self.choose_game_event.game)
        while not self.game.quit:
            self.game.playRound()

    def setGame(self, game_field):
        if game_field == "pan":
            self.game.processAudio = audio_process_functions.pan
