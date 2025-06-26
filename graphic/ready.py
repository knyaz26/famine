import pyray as pr
import sqlite3 as sq
import random
from graphic.entities.colonist import Colonist
from graphic.entities.food import Food

class Ready():
    def __init__(self):
        pass

    def start_window(self):
        pr.set_trace_log_level(pr.LOG_NONE)
        pr.init_window(800, 600, "Famine")
        pr.set_target_fps(60)
        # pr.set_window_icon()

    def load_sql(self):
        connection = sq.connect("database/famine_db")
        cursor = connection.cursor()
        data = cursor.execute(
        """
        SELECT *
        FROM settings
        ORDER BY rowid
        DESC LIMIT 1;
        """).fetchone()
        connection.close()
        return data

    def spawn_colonists(self, ammount, charisma, health):
        colonists = []
        sprite = pr.load_texture("assets/human.png")
        charisma = random.randint(0, charisma)
        for i in range(ammount):
            colonist = Colonist(i,sprite, charisma, health)
            colonists.append(colonist)
        return colonists

    def spawn_food(self, ammount):
        sprite = pr.load_texture("assets/food.png")
        food_list = []
        for i in range(ammount):
            food = Food(i, sprite)
            food_list.append(food)
        return food_list

ready = Ready()
