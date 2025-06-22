import pyray as pr
from graphic.ready import ready
from graphic.update import update

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        ready.start_window()
        settings_data = ready.load_sql()
        colonists = ready.spawn_colonists(settings_data[0], settings_data[4], settings_data[3])
        food_list = ready.spawn_food(settings_data[1])

        while not pr.window_should_close() and self.running:
            update.update_colonists(colonists)
            update.update_food(food_list)
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)
            update.draw_food(food_list)
            update.draw_colonists(colonists)
            pr.end_drawing()

        pr.close_window()

