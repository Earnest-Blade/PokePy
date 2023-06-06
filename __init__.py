import src.game as game

if __name__ == "__main__":
    gm = game.Game()
    gm.init(640, 480, "Window")
    gm.run()