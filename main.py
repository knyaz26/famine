import threading
from settings import Settings
from game import Game

# tkinters mainloop wont allow us to exec game logic
game = Game()
threading.Thread(target=game.run, daemon=True).start()

settings = Settings()
settings.enter()
