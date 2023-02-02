from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon

class Error(QDialog):
    def __init__(self, x:int, y:int, title: str, text:str, parent=None):
        super().__init__(parent)

        self.message = QLabel(text)

        self.root = QVBoxLayout()
        self.root.addWidget(self.message)

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("assets/cancel.png"))
        self.setLayout(self.root)
        self.setGeometry(x, y, 150, 100)
        self.exec_()