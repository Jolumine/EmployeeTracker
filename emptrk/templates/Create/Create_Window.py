from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel
from PyQt5.QtGui import QIcon 

from emptrk.templates.dialogs.Error import Error

import json
import datetime # optional


class Create_Window(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.firstname = QLineEdit(self)
        self.firstname.setPlaceholderText("Firstname")

        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Lastname")
        
        self.gender_label = QLabel("Gender:")
        
        self.gender_box = QComboBox(self)
        self.gender_box.setToolTip("Select a gender.")
        self.gender_box.addItems(["Male", "Female", "Divers"])

        self.gender_layout = QHBoxLayout()
        self.gender_layout.addWidget(self.gender_label)
        self.gender_layout.addWidget(self.gender_box)

        self.age = QLineEdit(self)
        self.age.setPlaceholderText("Age")

        self.phone_number = QLineEdit(self)
        self.phone_number.setPlaceholderText("Phone number")

        self.salary = QLineEdit(self)
        self.salary.setPlaceholderText("Salary")

        self.mail_address = QLineEdit(self)
        self.mail_address.setPlaceholderText("E-Mail")

        self.pos_descr = QLineEdit(self)
        self.pos_descr.setPlaceholderText("Position / Description")

        self.create_button = QPushButton("Create", self)
        self.create_button.setToolTip("Click to create employee")
        self.create_button.clicked.connect(self.create_user)

        self.coloumn1 = QVBoxLayout()
        self.coloumn1.addWidget(self.firstname)
        self.coloumn1.addWidget(self.lastname)
        self.coloumn1.addLayout(self.gender_layout)
        self.coloumn1.addWidget(self.age)

        self.coloumn2 = QVBoxLayout()
        self.coloumn2.addWidget(self.phone_number)
        self.coloumn2.addWidget(self.salary)
        self.coloumn2.addWidget(self.mail_address)
        self.coloumn2.addWidget(self.pos_descr)

        self.row = QHBoxLayout()
        self.row.addLayout(self.coloumn1)
        self.row.addLayout(self.coloumn2)

        self.root = QVBoxLayout()
        self.root.addLayout(self.row)
        self.root.addWidget(self.create_button)

        self.setWindowTitle("Create")
        self.setGeometry(225, 320, 600, 225)
        self.setLayout(self.root)
        self.setWindowIcon(QIcon("assets/open_folder.png"))
        self.exec_()

    def create_user(self) -> None:
        fname = self.firstname.text()
        lname = self.lastname.text()
        gen = self.gender_box.currentText()
        age = self.age.text()
        num = self.phone_number.text()
        sal = self.salary.text()
        mail = self.mail_address.text()
        pos_descr = self.pos_descr.text()

        if fname == "" or lname == "" or sal == "":
            Error(350, 320, "Error", "Please fill Firstname, Lastname and Salary.") 
        else: 
            with open("index.json", "r") as f: 
                parsed = json.load(f)
                f.close()

            id_ = len(parsed)+1
            new_entry = {
                "Firstname": fname, 
                "Lastname": lname, 
                "Gender": gen, 
                "Age": age, 
                "Phone": num, 
                "Salary": sal, 
                "E-Mail": mail, 
                "Position / Description": pos_descr
            }

            parsed[id_] = new_entry

            with open("index.json", "w") as f: 
                f.close()

            with open("index.json", "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)
                f.close()

        self.close()