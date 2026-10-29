import sys, os; os.system('clear||cls')

from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

# --- Configuration ---
X = 1000        # pixels from left of screen
Y = 100        # pixels from top of screen
WIDTH = 300    # desired display width in pixels (height scales automatically)


class ImageOverlay(QLabel):
    def __init__(self, image_path: str):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Error: could not load image '{image_path}'")
            sys.exit(1)

        scaled = pixmap.scaledToWidth(WIDTH, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(scaled)
        self.resize(scaled.size())
        self.move(X, Y)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            QApplication.quit()


def main():
    app = QApplication(['Pokemon Platinum Overlay'])
    overlay = ImageOverlay('Vitruvius.jpg')
    sys.exit(app.exec())


if __name__ == "__main__":
    main()