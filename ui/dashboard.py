import tkinter as tk
from tkinter import ttk
import threading
import sqlite3
from graphic.game import Game

class Dashboard():
    def __init__(self):
        pass
    
    def enter(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)
        
        game = Game()
        threading.Thread(target=game.run, daemon=True).start()

        self.notebook = ttk.Notebook(self.root)

        self.stats_tab = tk.Frame(self.notebook)
        self.history_tab = tk.Frame(self.notebook)
        self.details_tab = tk.Frame(self.notebook)
        self.info_tab = tk.Frame(self.notebook)

        self.notebook.add(self.stats_tab, text="Statistics")
        self.notebook.add(self.history_tab, text="History")
        self.notebook.add(self.details_tab, text="Details")
        self.notebook.add(self.info_tab, text="Info")

        self.notebook.pack(expand=True, fill="both")

        self.build_stats_tab()
        self.build_history_tab()
        self.build_details_tab()
        self.build_info_tab()

        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        self.root.after(100, self.update)

    def exit(self):
        if self.root:
            self.root.destroy()

    def build_stats_tab(self):
        pass

    def build_history_tab(self):
        pass

    def build_details_tab(self):
        pass

    def build_info_tab(self):
        self.info_text = tk.Label(self.info_tab, font=(16), text=
"""
FAMINE: THE SOCIAL SURVIVAL SIMULATOR

In a world where food runs low and greed runs high, 100 colonists must fight to survive.

— Every day, food drops randomly on the field.
— Colonists collect and consume food to stay alive.
— Extra food boosts their charisma. Greed pays....
— Every 7 days, the most charismatic colonist is voted out.
— Starve for 5 days, and you're dead.

Outwit, outlive, and outlast. Last one standing wins.

This simulator was inspired by primers YouTube channel.
""")
        self.info_text.pack()
        
dashboard = Dashboard()
