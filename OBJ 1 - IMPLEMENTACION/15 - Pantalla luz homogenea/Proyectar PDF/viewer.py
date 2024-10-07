import os
from pdf2image import convert_from_path
import tkinter as tk
from PIL import Image, ImageTk

class PDFViewer:
    def __init__(self, master, pdf_path):
        self.master = master
        self.master.title("Visor de PDF")

        self.canvas = tk.Canvas(master)
        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.page_images = convert_from_path(pdf_path, dpi=200)  # Change DPI as needed
        self.page_images = [ImageTk.PhotoImage(img) for img in self.page_images]

        self.current_page = 0
        self.display_page()

        self.master.bind("<Key>", self.on_key_press)

    def display_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        if self.current_page < len(self.page_images):
            img_label = tk.Label(self.frame, image=self.page_images[self.current_page])
            img_label.pack()

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_key_press(self, event):
        if event.keysym == "Down" and self.current_page < len(self.page_images) - 1:
            self.current_page += 1
            self.display_page()
        elif event.keysym == "Up" and self.current_page > 0:
            self.current_page -= 1
            self.display_page()

if __name__ == "__main__":
    root = tk.Tk()
    pdf_path = "lectura_2articulos.pdf"  # Your PDF file name
    pdf_viewer = PDFViewer(root, pdf_path)
    root.mainloop()
