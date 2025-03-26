# server/admin_gui/main_window.py

import tkinter as tk

def start_gui():
    root = tk.Tk()
    root.title("Price GameTracker Admin")
    root.geometry("800x600")
    
    label = tk.Label(root, text="Административная панель")
    label.pack()
    
    root.mainloop()