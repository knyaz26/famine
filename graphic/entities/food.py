import pyray as pr
import random

class Food():
    def __init__(self, id):
        self.id = id
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 600)
