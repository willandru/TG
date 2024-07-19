import tkinter as tk
from tkinter import filedialog

def preprocess_text(text):
    # Remove leading and trailing whitespace
    text = text.strip()
    # Replace newline characters with spaces
    text = text.replace('\n', ' ')
    # Remove extra spaces between symbols
    text = ' '.join(text.split())
    return text

def load_text():
    file_path = 'leer.txt'  # File path to 'leer.txt'
    try:
        with open(file_path, 'r') as file:
            text = file.read()  # Read text from the file
            text = preprocess_text(text)  # Preprocess the text
            text_display.delete(1.0, tk.END)  # Clear any existing text
            text_display.insert(tk.END, text)  # Insert the loaded text into the Text widget
            justify_text()  # Justify the text
            text_display.yview_moveto(0)  # Scroll text to the top
    except FileNotFoundError:
        print("File 'leer.txt' not found.")

def justify_text():
    lines = text_display.get(1.0, tk.END).split('\n')
    for line in lines:
        # Calculate the spaces needed for justification
        line_length = len(line)
        spaces_needed = max(0, text_display['width'] - line_length)
        # Insert the spaces evenly between words
        spaces_per_word = spaces_needed // (line.count(' ') or 1)
        remainder_spaces = spaces_needed % (line.count(' ') or 1)
        justified_line = ''
        for word in line.split(' '):
            justified_line += word + ' ' * spaces_per_word + (' ' if remainder_spaces > 0 else '')
            remainder_spaces -= 1
        # Replace the original line with the justified line
        text_display.delete(f'{lines.index(line) + 1}.0', f'{lines.index(line) + 1}.end')
        text_display.insert(f'{lines.index(line) + 1}.0', justified_line)

# Create the main window
root = tk.Tk()
root.title("Text Projector")
root.attributes('-fullscreen', True)  # Set window to full screen

# Frame to hold the text display
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

# Text display with scrollbar
text_display = tk.Text(text_frame, wrap="word", font=("Arial", 50))
text_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Fill the frame and expand to fill available space

scrollbar = tk.Scrollbar(text_frame, command=text_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Attach the scrollbar to the right side of the text widget
text_display.config(yscrollcommand=scrollbar.set)

# Load text button
load_button = tk.Button(root, text="Load Text from File", command=load_text)
load_button.pack(pady=10)

# Load initial text
load_text()

root.mainloop()
