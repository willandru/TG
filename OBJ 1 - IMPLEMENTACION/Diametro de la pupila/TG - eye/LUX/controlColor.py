import tkinter as tk

def update_luminosity(value):
    global root
    # Convert the value from the scale (0-100) to a percentage (0.0-1.0)
    luminosity = float(value) / 100
    # Update the background color with the adjusted luminosity
    bg_color = f"#{int(255 * luminosity):02x}{int(255 * luminosity):02x}{int(255 * luminosity):02x}"
    root.configure(bg=bg_color)

def create_fullscreen_window():
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_luminosity)
    scale.pack()
    # Set initial value for the scale (50% luminosity)
    scale.set(50)

    root.mainloop()

create_fullscreen_window()
