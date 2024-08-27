import tkinter as tk

def display_text():

    with open('texto_limpio.txt', 'r', encoding='utf-8') as file:
        text = file.read()
 
    root = tk.Tk()
    root.title("Visualizador de Texto")
    
    # Make the window full screen
    root.attributes('-fullscreen', True)
    
    # Create a Text widget to display the text
    text_widget = tk.Text(root, wrap='word', height=1, width=1)
    text_widget.insert('1.0', text)
    # Configure the font and size
    text_widget.configure(font=("Arial", 20))
    
    # Ensure the widget expands to fill the window
    text_widget.pack(expand=True, fill='both')
    
    # Handle window closing
    def on_closing():
        root.attributes('-fullscreen', False)
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

display_text()