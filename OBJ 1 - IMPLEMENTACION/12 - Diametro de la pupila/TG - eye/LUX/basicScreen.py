import tkinter as tk

def create_fullscreen_window(bg_color):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg=bg_color)

    root.mainloop()

# Specify the color you want to project (in hexadecimal format)
bg_color = "#FF0000"  # Red color

create_fullscreen_window(bg_color)
