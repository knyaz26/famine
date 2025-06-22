import pyray as pr
import random

class Colonist():
    def __init__(self, id, charisma, health):
        self.id = id
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 600)
        self.charisma = charisma
        self.health = health
        
