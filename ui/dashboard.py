import tkinter as tk
from tkinter import ttk
import threading
import sqlite3
from graphic.game import Game
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard():
    def __init__(self):
        self.last_day = -1
        self.fig = None
        self.axs = None
        self.canvas = None

    def enter(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.game = Game()
        threading.Thread(target=self.game.run, daemon=True).start()

        self.notebook = ttk.Notebook(self.root)

        self.history_tab = tk.Frame(self.notebook)
        self.stats_tab = tk.Frame(self.notebook)
        self.details_tab = tk.Frame(self.notebook)
        self.info_tab = tk.Frame(self.notebook)

        self.notebook.add(self.info_tab, text="Info")
        self.notebook.add(self.stats_tab, text="Statistics")
        self.notebook.add(self.history_tab, text="History")
        self.notebook.add(self.details_tab, text="Details")

        self.notebook.pack(expand=True, fill="both")

        self.build_history_tab()
        self.build_details_tab()
        self.build_info_tab()
        self.build_stats_tab()

        self.root.after(2000, self.update)
        self.root.mainloop()

    def update(self):
        if self.root.winfo_exists():
            connection = sqlite3.connect("database/famine_db")
            cursor = connection.cursor()
            cursor.execute("select max(days) from dashboard_data;")
            result = cursor.fetchone()
            connection.close()

            if result and result[0] is not None and result[0] != self.last_day:
                self.last_day = result[0]
                self.refresh_stats_tab()
                self.refresh_history_tab()

            self.root.after(1000, self.update)

    def exit(self):
        self.game.running = False
        if self.root:
            self.root.destroy()

    def build_stats_tab(self):
        self.fig, self.axs = plt.subplots(2, 2, figsize=(10, 6), sharex=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.stats_tab)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def refresh_stats_tab(self):
        connection = sqlite3.connect("database/famine_db")
        cursor = connection.cursor()
        cursor.execute("select * from dashboard_data;")
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            return

        days         = [row[0] for row in rows]
        charisma     = [row[1] for row in rows]
        stockpile    = [row[2] for row in rows]
        population   = [row[3] for row in rows]
        knocked_down = [row[4] for row in rows]

        for ax in self.axs.flat:
            ax.clear()

        self.axs[0, 0].fill_between(days, charisma, color='#9370DB', alpha=0.3)
        self.axs[0, 0].plot(days, charisma, color='#663399', marker='o')
        self.axs[0, 0].set_title("Charisma")

        self.axs[0, 1].plot(days, stockpile, color='#2E8B57', marker='s')
        self.axs[0, 1].set_title("Stockpile")

        self.axs[1, 0].plot(days, population, color='#1E90FF', marker='^')
        self.axs[1, 0].set_title("Population")

        self.axs[1, 1].bar(days, knocked_down, color='#A52A2A')
        self.axs[1, 1].set_title("Knocked Down")

        for ax in self.axs.flat:
            ax.grid(True)

        self.fig.tight_layout()
        self.canvas.draw()

    def build_history_tab(self):
        frame = tk.Frame(self.history_tab)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.event_list_box = tk.Listbox(
            frame,
            yscrollcommand=scrollbar.set,
            selectmode=tk.NONE,
            font=("Helvetica", 14)
        )
        self.event_list_box.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.event_list_box.yview)

    def refresh_history_tab(self):
        connection = sqlite3.connect("database/famine_db")
        cursor = connection.cursor()
        cursor.execute("select event from events order by rowid desc;")
        rows = cursor.fetchall()
        connection.close()

        self.event_list_box.delete(0, tk.END)
        for i, row in enumerate(rows):
            self.event_list_box.insert(tk.END, row[0])
            if i % 2 == 0:
                self.event_list_box.itemconfig(i, bg="white")
            else:
                self.event_list_box.itemconfig(i, bg="#e6f0ff")


    def build_details_tab(self):
        pass

    def build_info_tab(self):
        self.info_text = tk.Label(self.info_tab, font=(16), text=
            """
            FAMINE: THE SOCIAL SURVIVAL SIMULATOR

            100 colonists have to compete to survive in an environment where food
            becomes scarser every day and greed more rampant.

            - Every day, food drops randomly on the field.
            - Colonists collect and consume food to stay alive.
            - Extra food lovers charisma.
            - Every election day, the least charismatic colonist is voted out.
            - Fail to forage food and you starve.

            Last colonist standing wins.

            This simulator was inspired by primers YouTube channel.
            """)
        self.info_text.pack()

dashboard = Dashboard()
