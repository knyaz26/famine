import sqlite3 as sql
from ui.settings import Settings

connection = sql.connect("database/famine_db")
cursor = connection.cursor()
cursor.executescript("""
        delete from settings;
        delete from events;
        delete from dashboard_data;
    """)
connection.commit()
connection.close()

settings = Settings()
settings.enter()

