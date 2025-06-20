import tkinter as tk

class Settings():
    def enter(self):
        self.root = tk.Tk()
        self.root.title("Settings")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        self.root.after(100, self.update)
    
    def exit(self):
        if self.root:
            self.root.destroy()

settings = Settings()
