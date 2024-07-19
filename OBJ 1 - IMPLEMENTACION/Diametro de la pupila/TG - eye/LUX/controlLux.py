import tkinter as tk
import wmi

def set_brightness(level):
    brightness = int(level * 100)  # Convertir el nivel de brillo a un valor entre 0 y 100
    brightness = max(0, min(brightness, 100))  # Asegurar que el valor esté en el rango válido

    # Crear una instancia de la clase WMI para interactuar con el sistema operativo
    wmi_instance = wmi.WMI(namespace='wmi')

    # Obtener el controlador de pantalla
    methods = wmi_instance.WmiMonitorBrightnessMethods()[0]

    # Establecer el nivel de brillo
    methods.WmiSetBrightness(brightness, 0)  # El segundo parámetro (0) es el índice del monitor

def update_brightness(value):
    # Cuando cambia el valor del control deslizante, actualizar el brillo
    set_brightness(float(value) / 100)

def update_color(value):
    global root
    # Cuando cambia el valor del control deslizante, actualizar el color
    luminosity = float(value) / 100
    bg_color = f"#{int(255 * luminosity):02x}{int(255 * luminosity):02x}{int(255 * luminosity):02x}"
    root.configure(bg=bg_color)

def create_fullscreen_window():
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    brightness_label = tk.Label(root, text="Brillo:")
    brightness_label.pack()

    brightness_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_brightness)
    brightness_scale.pack()

    color_label = tk.Label(root, text="Color:")
    color_label.pack()

    color_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_color)
    color_scale.pack()

    root.mainloop()

# Ejecutar la aplicación
create_fullscreen_window()
