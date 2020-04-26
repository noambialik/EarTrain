import tkinter as tk
from PIL import Image, ImageTk
from numpy import interp
import threading
from myEventObject import AUDIO_READY_EVENT, GUI_EVENT

def clip(x, xmin, xmax):
    return max(xmin, min(x, xmax))

class GUI(threading.Thread):

    def __init__(self, gui_event):
        threading.Thread.__init__(self)
        self.gui_event = gui_event
        self.audio_ready = AUDIO_READY_EVENT()
        self.start()

    def quitGame(self):
        self.gui_event.set(shouldQuit=True)
        self.root.destroy()
        
    def getAudioReady(self):
        return self.audio_ready

    def mouseXToPan(self, x):
        return round(interp(x, [0, self.w], [-1,1]), 2)
    
    def panToMouseX(self, pan):
        return interp(pan, [-1,1], [0, self.w])
    
    def callback(self):
        self.root.quit()

    def onMouseMove(self, event):
        x, y = clip(event.x, 0, self.w), self.h // 2
        self.canvas.coords(self.mouseImg, x - 250, y - 150, x + 250, y + 100)
        if self.audio_ready.isSet():
            mapped = self.mouseXToPan(x)
            if mapped  == 0.0:
                labelText = "0"
            elif mapped > 0:
                labelText = str(abs(mapped)) + " R"
            else:
                labelText = str(abs(mapped)) + " L"
            self.scoreLabel.configure(foreground="black")
            if self.rightAnswerRect is not None:
                self.canvas.delete(self.rightAnswerRect)
                self.rightAnswerRect = None
        else:
            labelText = "Loading Audio..."
        


        self.posLabel['text'] = labelText

    def drawRightAnswer(self):
        x, y = self.panToMouseX(self.audio_ready.targetValue), self.h // 2
        self.rightAnswerRect = self.canvas.create_rectangle(x-1, y - 150, x + 1, y + 100, fill='black')

    def handleResult(self):
        if (abs(self.panToMouseX(self.guess) - self.panToMouseX(self.audio_ready.targetValue)) < 250):
            #print("Yay! panValue was " + str(self.audio_ready.targetValue))
            self.score += 100
            color = 'green'
            success = True
        else:
            #print("No! panValue was " + str(self.audio_ready.targetValue))
            color = 'red'
            success = False
        self.scoreLabel['text'] = "SCORE: " + str(self.score)
        self.scoreLabel.configure(foreground=color)
        return success

    def onClick(self, event):
        if self.audio_ready.isSet():
            self.audio_ready.clear()
            self.drawRightAnswer()
            mapped = self.mouseXToPan(event.x)
            self.guess = mapped
            success = self.handleResult()
            self.gui_event.set(success)

    def initGui(self):
        self.root = tk.Tk()
        self.root.title('EarTrain')
        fname = "resources/pan_background.png"
        bg_image = tk.PhotoImage(file=fname)
        # get the width and height of the image
        self.w = bg_image.width()
        self.h = bg_image.height()
        self.root.geometry("%dx%d+50+30" % (self.w, self.h))
        self.canvas = tk.Canvas(width=self.w, height=self.h)
        self.canvas.pack(side='top', fill='both', expand='yes')
        self.canvas.create_image(0, 0, image=bg_image, anchor='nw')
        x, y = self.w // 2, self.h // 2
        self.mouseImg = self.canvas.create_rectangle(x-250, y - 150, x + 250, y + 100, fill='black', stipple='gray12')
        self.posLabel = tk.Label(self.root, text="Loading Audio...")
        self.posLabel.place(x=x - 40, y=30)
        self.scoreLabel = tk.Label(self.root, text="SCORE: 0")
        self.scoreLabel.place(x= 50, y=30)
        self.score = 0
        self.rightAnswerRect = None
        
        #events
        self.root.bind('<Motion>', self.onMouseMove)
        self.root.bind("<Button-1>", self.onClick)
        self.root.protocol("WM_DELETE_WINDOW", self.quitGame)
        
        self.root.mainloop()
        
        
    def run(self):
        self.initGui()


if __name__ == '__main__':
    GUI(GUI_EVENT())
