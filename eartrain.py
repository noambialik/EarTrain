import games
from game_thread import gameThread
from myEventObject import GUI_EVENT, CHOOSE_GAME_EVENT
from mygui import GUI
import audio_process_functions


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
    choose_game_event = CHOOSE_GAME_EVENT()
    gui_event = GUI_EVENT()
    gui = GUI(gui_event, choose_game_event)
    audio_thread = gameThread(gui.audio_ready, choose_game_event, gui_event)
    gui.runGui()

