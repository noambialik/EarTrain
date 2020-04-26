from threading import Event


class AUDIO_READY_EVENT(Event):

    def __init__(self):
        super().__init__()
        self.targetValue = None

    def set(self, targetValue=None):
        self.targetValue = targetValue
        super().set()

        def clear(self):
            super(self).clear()
            self.targetValue = None


class GUI_EVENT(Event):

    def __init__(self):
        super().__init__()
        self.success = None
        self.quit = None
        self.game = None
        self.game = None
        self.change_game = None

    def set(self, success=None, shouldQuit=None, game=None):
        self.success = success
        self.quit = shouldQuit
        self.game = game
        if game is not None:
            self.change_game = True
        super().set()

    def clear(self):
        super().clear()
        self.success = None
        self.quit = None
        self.game = None
        self.game = None
        self.change_game = None

