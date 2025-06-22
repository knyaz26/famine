import tkinter as tk
import sqlite3 as sq
from ui.dashboard import dashboard

class Settings():
    def __init__(self):
        self._inputs = [
            "colonists",
            "starting food",
            "food decay",
            "health",
            "charisma limit",
            "vote intervals"
        ]
        self._prefill = [
            "100",
            "100",
            "1",
            "5",
            "5",
            "7"
        ]
        self._constraints = [
            (10, 100),
            (10, 100),
            (0, 10),
            (1, 10),
            (1, 20),
            (3, 20)
        ]
        self._widgets = []
        self._entry_width = 10
        self._pady = 5
        
    def enter(self):
        self.root = tk.Tk()
        self.root.title("Settings")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        
        self.content = tk.Frame(self.root)
        self.content.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.5)
        self.content.columnconfigure(1, weight=1)

        for i in range(len(self._inputs)):
            self.label = tk.Label(self.content, text=self._inputs[i])
            self.separator = tk.Frame(self.content)
            self.entry = tk.Entry(self.content, width=self._entry_width)
            self._widgets.append((self.label, self.separator, self.entry))
            self.entry.insert(0, self._prefill[i])
            self.label.grid(row=i, column=0, sticky='w', pady=self._pady)
            self.separator.grid(row=i, column=1, sticky='ew', pady=self._pady)
            self.entry.grid(row=i, column=2, sticky='e', pady=self._pady)

        self.start_frame = tk.Frame(self.root)
        self.start_frame.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.5)
        self.start_button = tk.Button(self.start_frame, text="start", command=self.on_click)
        self.start_button.pack(pady=self._pady)
        self.start_text = tk.Text(self.start_frame, width=35, height=5)
        self.start_text.pack(pady=self._pady)
        self.start_text.configure(font=("Arial", 10), fg="red")
        self.start_text.config(state="disabled")
            
        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        self.root.after(100, self.update)
    
    def exit(self):
        if self.root:
            self.root.destroy()
            dashboard.enter()


    def on_click(self):
        error_msg = ""
        data = []
        for i in range(len(self._widgets)):
            raw = self._widgets[i][2].get()
            data.append(raw)
            label = self._widgets[i][0].cget("text")
            try:
                val = int(raw)
            except ValueError:
                error_msg += f"Only numbers allowed in '{label}'\n"
                continue
            low, high = self._constraints[i]
            if not (low <= val <= high):
                error_msg += f"'{label}' must be between {low} and {high}\n"
    
        self.start_text.config(state="normal")
        self.start_text.delete("1.0", "end")
        self.start_text.insert("1.0", error_msg if error_msg else "launching...")
        if not error_msg:
            connection = sq.connect('database/famine_db')
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO settings VALUES (?, ?, ?, ?, ?, ?);",
                tuple(map(int, data))
            )
            connection.commit()
            connection.close()
            self.exit()
            
        self.start_text.config(state="disabled")


settings = Settings()
