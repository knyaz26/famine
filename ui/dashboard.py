import tkinter as tk
import threading
import sqlite3
from graphic.game import Game

class Dashboard():
    def __init__(self):
        pass
    
    def enter(self):
        self.root = tk.Tk()
        
        game = Game()
        threading.Thread(target=game.run, daemon=True).start()

        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        self.root.after(100, self.update)

    def exit(self):
        if self.root:
            self.root.destroy()

dashboard = Dashboard()
