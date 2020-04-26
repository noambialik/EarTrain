import games

####################
##MAIN
####################

if __name__ == "__main__":
    pan = games.PanGame()

    while not pan.quit:
        pan.playRound()
