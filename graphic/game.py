import pyray as pr
from graphic.ready import ready
from graphic.update import update

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        ready.start_window()
        data = ready.load_sql()
        print(data)

        while not pr.window_should_close() and self.running:
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)

            pr.end_drawing()

        pr.close_window()

