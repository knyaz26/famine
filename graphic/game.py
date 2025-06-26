import pyray as pr
from graphic.ready import ready
from graphic.update import update
from graphic.mediator import mediator

class Game:
    def __init__(self):
        self.running = True
        self.settings_data = ready.load_sql()
        self.food = self.settings_data[1]
        self.decay = self.settings_data[2]
        self.vote_intervals = self.settings_data[5]
        self.day = 1

    def run(self):
        ready.start_window()
        colonists = ready.spawn_colonists(self.settings_data[0], self.settings_data[4], self.settings_data[3])
        food_list = ready.spawn_food(self.food)
        mediator.build_tree(colonists, food_list)
        while not pr.window_should_close() and self.running:
            update.update_colonists(colonists)
            update.update_food(food_list)
            food_list = update.return_collisions(colonists, food_list)
            colonists = update.kill_off_starved(colonists)
            day_passed = update.check_food(colonists, food_list)
            if day_passed:
                self.day += 1
                self.food -= self.decay
                food_list = ready.spawn_food(self.food)
                update.update_food(food_list)
            update.check_election(self.vote_intervals, self.day, colonists)
            pr.begin_drawing()
            pr.clear_background(pr.RAYWHITE)
            update.draw_food(food_list)
            update.draw_colonists(colonists)
            pr.end_drawing()
            self.running = update.is_game_over()

        pr.close_window()

