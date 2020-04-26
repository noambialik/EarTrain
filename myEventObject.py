from threading import Event


class AUDIO_READY_EVENT(Event):

    def __init__(self):
        super().__init__()
        self.targetValue = None

    def set(self, targetValue=None):
        self.targetValue = targetValue
        super().set()


class GUI_EVENT(Event):

    def __init__(self):
        super().__init__()
        self.success = None
        self.quit = None

    def set(self, success=None, shouldQuit=None):
        self.success = success
        self.quit = shouldQuit
        super().set()


class CHOOSE_GAME_EVENT(Event):

    def __init__(self):
        super().__init__()
        self.game = None

    def set(self, game):
        self.game = game
        super().set()
