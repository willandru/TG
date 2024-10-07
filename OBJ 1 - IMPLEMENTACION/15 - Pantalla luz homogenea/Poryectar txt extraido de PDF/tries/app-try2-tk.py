import tkinter as tk
from tkinter.font import Font

def wrap_text(text, font, max_width):
    """Wraps text to fit within the maximum width."""
    lines = []
    words = text.split()
    current_line = ""
    
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.measure(test_line) <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def justify_line(line, line_width, font):
    """Justifies a single line to fit the width."""
    words = line.split()
    if len(words) == 1:
        return line
    
    total_chars = sum(font.measure(word) for word in words)
    total_spaces = line_width - total_chars
    
    spaces_between_words = total_spaces // (len(words) - 1)
    extra_spaces = total_spaces % (len(words) - 1)
    
    justified_line = words[0]
    for i in range(1, len(words)):
        spaces_to_add = spaces_between_words + (1 if i <= extra_spaces else 0)
        justified_line += ' ' * spaces_to_add + words[i]
    
    return justified_line

def display_text(text):
    root = tk.Tk()
    root.title("Visualizador de Texto")
    
    # Make the window full screen
    root.attributes('-fullscreen', True)
    
    # Create a Text widget to display the text
    text_widget = tk.Text(root, wrap='none', font=("Arial", 20))
    text_widget.pack(expand=True, fill='both')
    
    # Set up font for measuring text width
    font = Font(family="Arial", size=20)
    
    # Ensure the widget expands to fill the window
    text_widget.update_idletasks()
    line_width = text_widget.winfo_width()
    
    # Wrap text
    lines = wrap_text(text, font, line_width)
    
    # Justify text
    justified_text = ""
    for line in lines:
        justified_text += justify_line(line, line_width, font) + '\n'
    
    text_widget.insert('1.0', justified_text)
    
    # Handle window closing
    def on_closing():
        root.attributes('-fullscreen', False)
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

# Example usage
with open('texto_limpio.txt', 'r', encoding='utf-8') as file:
    text = file.read()
display_text(text)
