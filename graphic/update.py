import pyray as pr
from graphic.mediator import mediator

class Update():
    def __init__(self):
        pass

    def update_colonists(self, colonists):
        for i in colonists:
            i.update()

    def draw_colonists(self, colonists):
        for i in colonists:
            i.draw()

    def update_food(self, food_list):
        for i in food_list:
            i.update()
            
    def draw_food(self, food_list):
        for i in food_list:
            i.draw()

    def update_targets(self, colonists, food_list):
        mediator.get_objects(colonists, food_list)
        mediator.build_tree()

update = Update()
