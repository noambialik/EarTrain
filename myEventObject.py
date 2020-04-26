from threading import Event

class AUDIO_READY_EVENT(Event):
    def set(self, targetValue):
        self.targetValue = targetValue
        super().set()

class GUI_EVENT(Event):
    def set(self, success=None, shouldQuit=None):
        self.success = success
        self.quit = shouldQuit
        super().set()
