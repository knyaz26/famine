import pyray as pr
import sqlite3 as sq
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
        mediator.build_tree(colonists, food_list)

    def return_collisions(self, colonists, food_list):
        for i in colonists:
            for j in food_list:
                if pr.check_collision_recs(i.rect, j.rect):
                    event = f"{i.name} collected food."
                    self.insert_sql(event)
                    # food up
                    # charisma down
                    food_list.remove(j)
        return food_list

    def insert_sql(self, event):
        connect = sq.connect("database/famine_db")
        cursor = connect.cursor()
        cursor.execute("""
            insert into events (event) values (?)
        """, (event,))
        connect.commit()
        connect.close()

    

update = Update()
