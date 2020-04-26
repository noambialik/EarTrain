from game_thread import gameThread
from myEventObject import GUI_EVENT
from mygui import GUI


####################
##MAIN
####################
def getGameSelected(my_gui):
    my_gui.gui_event.wait()
    my_gui.gui_event.clear()
    return my_gui.game


if __name__ == "__main__":
    # pan = games.PanGame()
    #
    # while not pan.quit:
    #     pan.playRound()
    gui_event = GUI_EVENT()
    gui = GUI(gui_event)
    audio_thread = gameThread(gui.audio_ready, gui_event)
    gui.runGui()

