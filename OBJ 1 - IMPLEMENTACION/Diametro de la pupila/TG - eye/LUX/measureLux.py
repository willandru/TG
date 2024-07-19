import tkinter as tk
import wmi

def set_brightness(level):
    brightness = int(level * 100)  # Convert the brightness level to a value between 0 and 100
    brightness = max(0, min(brightness, 100))  # Ensure the value is within the valid range

    # Create an instance of the WMI class to interact with the operating system
    wmi_instance = wmi.WMI(namespace='wmi')

    # Get the display controller
    methods = wmi_instance.WmiMonitorBrightnessMethods()[0]

    # Set the brightness level
    methods.WmiSetBrightness(brightness, 0)  # The second parameter (0) is the monitor index

def decrease_brightness():
    global brightness, brightness_label
    if brightness > 0:
        brightness -= 1
        set_brightness(brightness / 100)
        brightness_label.config(text=str(brightness))

def increase_brightness():
    global brightness, brightness_label
    if brightness < 100:
        brightness += 1
        set_brightness(brightness / 100)
        brightness_label.config(text=str(brightness))

def create_fullscreen_window(start_low_brightness=True, black_background=False):
    global root, brightness, brightness_label

    blanco = "#FFFFFF"
    negro = "#000000"
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    
    if black_background:
        root.configure(bg=negro)
        font_color = blanco  # White font color for black background
        label_bg = negro     # White label background for black background
    else:
        root.configure(bg=blanco)
        font_color = negro  # Black font color for white background
        label_bg = blanco     # Black label background for white background
    
    if start_low_brightness:
        set_brightness(0)  # Start with lowest brightness

    brightness = 0  # Initial brightness

    font_size = 15
    font = ("Segoe UI Light", font_size)
    
    brightness_label = tk.Label(root, text="0", bg=label_bg, fg=font_color, font=font)
    brightness_label.pack(expand=True)

    root.bind("<Left>", lambda event: decrease_brightness())  # Decrease brightness on Left arrow key press
    root.bind("<Right>", lambda event: increase_brightness())  # Increase brightness on Right arrow key press
    root.bind("<Escape>", lambda event: root.destroy())  # Exit fullscreen on Escape key press

    root.mainloop()

# Run the application with black background
create_fullscreen_window(black_background=False)
