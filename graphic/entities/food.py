import pyray as pr
import random

class Food():
    def __init__(self, id, sprite):
        self.id = id
        self.sprite = sprite
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 600)
        self.src = pr.Rectangle(0, 0, self.sprite.width, self.sprite.height)
        self.origin = pr.Vector2(self.sprite.width // 2, self.sprite.height)

    def update(self):
        self.rect = pr.Rectangle(self.pos_x, self.pos_y, self.sprite.width, self.sprite.height)
        

    def draw(self):
        pr.draw_texture_pro(
            self.sprite,
            self.src,
            self.rect,
            self.origin,
            0,
            pr.WHITE
        )
