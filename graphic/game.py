import pyray as pr

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        pr.init_window(800, 600, b"Famine")
        pr.set_target_fps(60)

        while not pr.window_should_close() and self.running:
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)

            pr.draw_text("Famine World Running", 200, 200, 20, pr.DARKGRAY)

            pr.end_drawing()

        pr.close_window()

