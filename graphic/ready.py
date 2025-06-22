import pyray as pr
import sqlite3 as sq

class Ready():
    def __init__(self):
        pass

    def start_window(self):
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

ready = Ready()
