from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon

from emptrk.templates.Create.Create_Window import Create_Window
from emptrk.templates.Select.Select_Window import Select_Window

from emptrk.templates.dialogs.Error import Error

from emptrk.utils.get_entrys import get_entrys


class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.search_line = QLineEdit(self)
        self.search_line.setPlaceholderText("Search")
        self.search_line.textChanged.connect(self.search)
        
        self.collection = QComboBox(self)
        self.collection.setToolTip("Collection of all employees.")
        self.collection.addItems(get_entrys())

        self.select_button = QPushButton("Select", self)
        self.select_button.setToolTip("Click to open the selected user.")
        self.select_button.clicked.connect(self.select)

        self.create_button = QPushButton("Create", self)
        self.create_button.setToolTip("Click to create a new entry.")
        self.create_button.clicked.connect(self.open_create)

        self.root = QVBoxLayout()
        self.root.addWidget(self.search_line)
        self.root.addWidget(self.collection)
        self.root.addWidget(self.select_button)
        self.root.addWidget(self.create_button)

        self.setWindowTitle("Personal Tracker")
        self.setGeometry(300, 300, 450, 300)
        self.setWindowIcon(QIcon("assets/main.png"))
        self.setLayout(self.root)
        self.show()

    def render(self):
        self.collection.clear()
        self.collection.addItems(get_entrys())

    def search(self):
        self.collection.clear()
        self.collection.addItems(get_entrys(self.search_line.text()))

    def select(self):
        if len(self.collection) == 0: 
            Error(375, 300, "Error", "No entrys available, create them first.") 
        else: 
            Select_Window(self.collection.currentText().split("-")[0])
            self.render()

    def open_create(self):
        Create_Window()
        self.render()