from controller import controller
#creates a new game and runs it
#click this to actually start the game
class Main:
    newGame=controller()
    while True:
        newGame.new()
        newGame.run()
