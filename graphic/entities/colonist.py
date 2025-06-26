import pyray as pr
import random

class Colonist():
    def __init__(self, id, sprite, charisma, health):
        self.id = id
        self.sprite = sprite
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 600)
        self.charisma = charisma
        self.health = health
        self.src = pr.Rectangle(0, 0, self.sprite.width, self.sprite.height)
        self.origin = pr.Vector2(self.sprite.width // 2, self.sprite.height)
        self.target = None
        self.speed = 0.5

    def update(self):
        self.move_towards()
        self.update_rectangle()

    def draw(self):
        pr.draw_texture_pro(
            self.sprite,
            self.src,
            self.rect,
            self.origin,
            0,
            pr.WHITE
        )

    def move_towards(self):
        if self.target:
            print("moving toward", self.target.pos_x, self.target.pos_y)
            
            pos1 = (self.pos_x, self.pos_y)
            pos2 = (self.target.pos_x, self.target.pos_y)
            dx = pos2[0] - pos1[0]
            dy = pos2[1] - pos1[1]
            dist = (dx**2 + dy**2) ** 0.5
            if dist==0:
                return
            nx, ny = dx / dist, dy / dist
            move_dist = min(self.speed, dist)
            self.pos_x = pos1[0] + nx * move_dist
            self.pos_y = pos1[1] + ny * move_dist

    def update_rectangle(self):
        self.rect = pr.Rectangle(self.pos_x, self.pos_y, self.sprite.width * 2, self.sprite.height * 2)
