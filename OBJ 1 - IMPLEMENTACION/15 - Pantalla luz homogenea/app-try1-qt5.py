from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys

class TextDisplay(QMainWindow):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Visualizador de Texto")
        
        # Create a QTextEdit widget and set it to fill the window
        self.text_edit = QTextEdit()
        self.text_edit.setText(text)
        self.text_edit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setCentralWidget(self.text_edit)
        
        # Make the window full screen
        self.showFullScreen()

# Example usage
app = QApplication(sys.argv)
with open('texto_limpio.txt', 'r', encoding='utf-8') as file:
    text = file.read()
window = TextDisplay(text)
sys.exit(app.exec_())
