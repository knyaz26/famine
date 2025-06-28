import pyray as pr
import random
import names

names_list = [names.get_full_name() for _ in range(100)]

class Colonist():
    def __init__(self, id, sprite, charisma, health):
        self.id = id
        self.name = random.choice(names_list)
        self.sprite = sprite
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 600)
        self.charisma = charisma
        self.stockpile = 0
        self.health = health
        self.src = pr.Rectangle(0, 0, self.sprite.width, self.sprite.height)
        self.origin = pr.Vector2(self.sprite.width // 2, self.sprite.height)
        self.target = None
        self.speed = random.randint(10, 13) / 10
        self.strength = random.random()
        self.knocked_down = False
        self.dead = False
        self.shake_offset = 0
        self.shake_direction = 1
        self.tilt = 0
        self.tilt_direction = 1

    def update(self):
        self.move_towards()
        self.update_rectangle()
        if not self.knocked_down:
            self.shake()

    def shake(self):
        self.shake_offset += 0.3 * self.shake_direction
        if abs(self.shake_offset) > 3:
            self.shake_direction *= -1
        self.tilt += 0.5 * self.tilt_direction
        if abs(self.tilt) > 5:
            self.tilt_direction *= -1

    def draw(self):
        pr.draw_texture_pro(
            self.sprite,
            self.src,
            pr.Rectangle(self.pos_x, self.pos_y + self.shake_offset, self.sprite.width * 2, self.sprite.height * 2),
            self.origin,
            self.tilt,
            pr.WHITE
        )

    def move_towards(self):
        if self.target and not self.knocked_down:
            pos1 = (self.pos_x, self.pos_y)
            pos2 = (self.target.pos_x, self.target.pos_y)
            dx = pos2[0] - pos1[0]
            dy = pos2[1] - pos1[1]
            dist = (dx**2 + dy**2) ** 0.5
            if dist == 0:
                return
            nx, ny = dx / dist, dy / dist
            move_dist = min(self.speed, dist)
            self.pos_x = pos1[0] + nx * move_dist
            self.pos_y = pos1[1] + ny * move_dist

    def update_rectangle(self):
        self.rect = pr.Rectangle(self.pos_x, self.pos_y, self.sprite.width * 2, self.sprite.height * 2)

    def eat(self):
        if self.stockpile > 0:
            self.stockpile -= 1
        elif self.health > 0:
            self.health -= 1
        else:
            self.die()

    def die(self):
        self.dead = True
     
