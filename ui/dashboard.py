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

        self.info_tab = tk.Frame(self.notebook)

        self.notebook.add(self.info_tab, text="Info")

        self.notebook.pack(expand=True, fill="both")

        self.info_text = tk.Label(self.info_tab, text="hehehe")
        self.info_text.pack()

        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        self.root.after(100, self.update)

    def exit(self):
        if self.root:
            self.root.destroy()

dashboard = Dashboard()
