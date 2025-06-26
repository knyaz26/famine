import pyray as pr
import sqlite3 as sq
from graphic.mediator import mediator

class Update():
    def __init__(self):
        self.last_vote_day = -1
        self.game_over = False

    def update_colonists(self, colonists):
        if colonists:
            for i in colonists:
                i.update()

    def draw_colonists(self, colonists):
        if colonists:
            for i in colonists:
                i.draw()

    def update_food(self, food_list):
        for i in food_list:
            i.update()
            
    def draw_food(self, food_list):
        for i in food_list:
            i.draw()

    def return_collisions(self, colonists, food_list):
        for i in colonists:
            for j in food_list:
                if pr.check_collision_recs(i.rect, j.rect):
                    event = f"{i.name} collected food."
                    self.sql_insert_events(event)
                    self.feed_colonist(i)
                    food_list.remove(j)
                    mediator.build_tree(colonists, food_list)
        return food_list

    def sql_insert_events(self, event):
        connect = sq.connect("database/famine_db")
        cursor = connect.cursor()
        cursor.execute("""
            insert into events (event) values (?)
        """, (event,))
        connect.commit()
        connect.close()
    
    def sql_insert_dashboard_data(self, days, charisma, stockpile, population, knocked_down, food_left):
        connect = sq.connect("database/famine_db")
        cursor = connect.cursor()
        cursor.execute("""
            insert into dashboard_data (days, charisma, stockpile, population, knocked_down, food_left)
            values (?, ?, ?, ?, ?, ?)
        """, (days, charisma, stockpile, population, knocked_down, food_left))
        connect.commit()
        connect.close()

    def feed_colonist(self, colonist):
        colonist.stockpile += 1
        colonist.charisma -= 1
        

    def end_day(self, colonists, food_list, days, food):
        if not food_list and colonists:
            charisma = 0
            stockpile = 0
            knocked_down = 0
            population = len(colonists)
            food_left = food
            for i in colonists:
                i.eat()
                charisma += i.charisma
                stockpile += i.stockpile
                knocked_down += 1 if i.knocked_down else 0
            event = "day has passed..."
            self.sql_insert_events(event)
            self.sql_insert_dashboard_data(days, charisma, stockpile, population, knocked_down, food_left)
            self.revive_knocked_colonists(colonists)
            return True
        return False

    def kill_off_starved(self, colonists):
        for i in colonists:
            if len(colonists) <= 1:
                self.winner(i)
                return
            if i.dead:
                event = f"{i.name} has died."
                self.sql_insert_events(event)
                colonists.remove(i)
        return colonists

    def check_election(self, vote_intervals, day, colonists):
        if day % vote_intervals == 0 and colonists and day != self.last_vote_day:
            self.last_vote_day = day
            lowest =colonists[0]
            for i in colonists:
                if i.charisma < lowest.charisma:
                    lowest = i
            event = f"{lowest.name} was voted out."
            self.sql_insert_events(event)
            lowest.die()

    def winner(self, winner):
        event = f"{winner.name} has survived the onslought"
        self.sql_insert_events(event)
        self.game_over = True

    def is_game_over(self):
        return False if self.game_over else True

    def check_colonist_collisions(self, colonists):
        if colonists:
            for i in range(len(colonists)):
                for j in range(i + 1, len(colonists)):
                    if pr.check_collision_recs(colonists[i].rect, colonists[j].rect):
                        if colonists[i].strength > colonists[j].strength:
                            colonists[j].knocked_down = True
                        else:
                            colonists[i].knocked_down = True
        
    def revive_knocked_colonists(self, colonists):
        for i in colonists:
            i.knocked_down = False


update = Update()
