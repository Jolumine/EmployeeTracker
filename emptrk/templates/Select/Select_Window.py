from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon 

from emptrk.templates.dialogs.Confirm import Confirm

import json

class Select_Window(QDialog):
    def __init__(self, id_:str, parent=None) -> None: 
        super().__init__(parent)

        self.id_ = id_

        with open("index.json", "r") as f: 
            parsed = json.load(f)
            f.close()

        self.firstname = QLabel("Firstname")

        self.firstname_line = QLineEdit(self)
        self.firstname_line.setText(parsed[id_]["Firstname"])
        self.firstname_line.setReadOnly(True)

        self.firstname_layout = QHBoxLayout()
        self.firstname_layout.addWidget(self.firstname)
        self.firstname_layout.addWidget(self.firstname_line)

        self.lastname = QLabel("Lastname:")

        self.lastname_line = QLineEdit(self)
        self.lastname_line.setText(parsed[id_]["Lastname"])
        self.lastname_line.setReadOnly(True)

        self.lastname_layout = QHBoxLayout()
        self.lastname_layout.addWidget(self.lastname)
        self.lastname_layout.addWidget(self.lastname_line)
        
        self.gender_label = QLabel("Gender:")
        
        self.gender_box = QComboBox(self)
        self.gender_box.setToolTip("Select a gender.")
        self.gender_box.addItems(["Male", "Female", "Divers"])
        self.gender_box.setCurrentText(parsed[id_]["Gender"])
        self.gender_box.setDisabled(True)

        self.gender_layout = QHBoxLayout()
        self.gender_layout.addWidget(self.gender_label)
        self.gender_layout.addWidget(self.gender_box)

        self.age = QLabel("Age:")

        self.age_line = QLineEdit(self)
        self.age_line.setText(parsed[id_]["Age"])
        self.age_line.setReadOnly(True)

        self.age_layout = QHBoxLayout()
        self.age_layout.addWidget(self.age)
        self.age_layout.addWidget(self.age_line)

        self.number = QLabel("Phonenumber:")

        self.phone_number_line = QLineEdit(self)
        self.phone_number_line.setText(parsed[id_]["Phone"])
        self.phone_number_line.setReadOnly(True)

        self.phone_layout = QHBoxLayout()
        self.phone_layout.addWidget(self.number)
        self.phone_layout.addWidget(self.phone_number_line)

        self.salary = QLabel("Salary:")

        self.salary_line = QLineEdit(self)
        self.salary_line.setText(parsed[id_]["Salary"])
        self.salary_line.setReadOnly(True)

        self.salary_layout = QHBoxLayout()
        self.salary_layout.addWidget(self.salary)
        self.salary_layout.addWidget(self.salary_line)

        self.mail = QLabel("E-Mail:")

        self.mail_address_line = QLineEdit(self)
        self.mail_address_line.setText(parsed[id_]["E-Mail"])
        self.mail_address_line.setReadOnly(True)

        self.mail_layout = QHBoxLayout()
        self.mail_layout.addWidget(self.mail)
        self.mail_layout.addWidget(self.mail_address_line)

        self.position = QLabel("Position / Description:")

        self.pos_descr_line = QLineEdit(self)
        self.pos_descr_line.setText(parsed[id_]["Position / Description"])
        self.pos_descr_line.setReadOnly(True)

        self.pos_layout = QHBoxLayout()
        self.pos_layout.addWidget(self.position)
        self.pos_layout.addWidget(self.pos_descr_line)

        self.modify_button = QPushButton(self)
        self.modify_button.setIcon(QIcon("assets/modify.png"))
        self.modify_button.setToolTip("Click to modify the selected employee.")
        self.modify_button.clicked.connect(self.modify)

        self.delete_button = QPushButton(self)
        self.delete_button.setIcon(QIcon("assets/delete.png"))
        self.delete_button.setToolTip("Click to delete the selected employee.")
        self.delete_button.clicked.connect(self.delete)

        self.save_button = QPushButton(self)
        self.save_button.setIcon(QIcon("assets/confirm.png"))
        self.save_button.setToolTip("Click to save the changes.")
        self.save_button.clicked.connect(self.save)
        self.save_button.hide()

        self.cancel_button = QPushButton()
        self.cancel_button.setIcon(QIcon("assets/cancel.png"))
        self.cancel_button.setToolTip("Click to cancel the changes.")
        self.cancel_button.clicked.connect(self.cancel)
        self.cancel_button.hide()

        self.coloumn1 = QVBoxLayout()
        self.coloumn1.addLayout(self.firstname_layout)
        self.coloumn1.addLayout(self.lastname_layout)
        self.coloumn1.addLayout(self.gender_layout)
        self.coloumn1.addLayout(self.age_layout)

        self.coloumn2 = QVBoxLayout()
        self.coloumn2.addLayout(self.salary_layout)
        self.coloumn2.addLayout(self.mail_layout)
        self.coloumn2.addLayout(self.phone_layout)
        self.coloumn2.addLayout(self.pos_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.modify_button)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.delete_button)

        self.row = QHBoxLayout()
        self.row.addLayout(self.coloumn1)
        self.row.addLayout(self.coloumn2)
        
        self.root = QVBoxLayout()
        self.root.addLayout(self.row)
        self.root.addLayout(self.buttons_layout)

        self.setWindowTitle(f"{parsed[id_]['Firstname']} {parsed[id_]['Lastname']}")
        self.setGeometry(225, 320, 600, 225)
        self.setWindowIcon(QIcon("assets/open_folder.png"))
        self.setLayout(self.root)
        self.exec_()

    def render(self):
        self.firstname_line.clear()
        self.lastname_line.clear()
        self.age_line.clear()
        self.phone_number_line.clear()
        self.mail_address_line.clear()
        self.salary_line.clear()
        self.pos_descr_line.clear()

        with open("index.json", "r") as f: 
            parsed = json.load(f)
            f.close()

        self.firstname_line.setText(parsed[self.id_]["Firstname"])
        self.lastname_line.setText(parsed[self.id_]["Lastname"])
        self.gender_box.setCurrentText(parsed[self.id_]["Gender"])
        self.age_line.setText(parsed[self.id_]["Age"])
        self.phone_number_line.setText(parsed[self.id_]["Phone"])
        self.salary_line.setText(parsed[self.id_]["Salary"])
        self.mail_address_line.setText(parsed[self.id_]["E-Mail"])
        self.pos_descr_line.setText(parsed[self.id_]["Position / Description"])

    def delete(self): 
        dialog = Confirm(400, 320, "Confirm", "Confirm the deletion.")
        rep = dialog.exec_()

        if rep == QMessageBox.Apply: 
            with open("index.json", "r") as f: 
                parsed = json.load(f)
                f.close()

            if self.id_ in parsed: 
                del parsed[self.id_]
            else: 
                raise KeyError()

            with open("index.json", "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)
                f.close()

            with open("index.json", "r") as f: 
                parsed = json.load(f)
                f.close()

            entrys = []
            reordered = {}

            for entry in parsed: 
                entrys.append(parsed[entry])

            for entry in entrys: 
                reordered[len(reordered)+1] = entry
            
            with open("index.json", "w") as f: 
                json.dump(reordered, f, indent=4, sort_keys=False)
                f.close()

            self.close()
        else: 
            pass


    def modify(self):
        self.buttons_layout.removeWidget(self.modify_button)
        self.buttons_layout.removeWidget(self.delete_button)
        self.root.removeItem(self.buttons_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.cancel_button)
        self.root.addLayout(self.buttons_layout)
        self.modify_button.hide()
        self.delete_button.hide()
        self.save_button.show()
        self.cancel_button.show()

        self.firstname_line.setReadOnly(False)
        self.lastname_line.setReadOnly(False)
        self.age_line.setReadOnly(False)
        self.phone_number_line.setReadOnly(False)
        self.mail_address_line.setReadOnly(False)
        self.salary_line.setReadOnly(False)
        self.gender_box.setEnabled(True)
        self.pos_descr_line.setReadOnly(False)

    def save(self):
        self.buttons_layout.removeWidget(self.save_button)
        self.buttons_layout.removeWidget(self.cancel_button)
        self.root.removeItem(self.buttons_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.modify_button)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.delete_button)
        self.root.addLayout(self.buttons_layout)
        self.save_button.hide()
        self.cancel_button.hide()
        self.modify_button.show()
        self.delete_button.show() 

        with open("index.json", "r") as f: 
            parsed = json.load(f)
            f.close()

        new_entry = {
            "Firstname": self.firstname_line.text(), 
            "Lastname": self.lastname_line.text(), 
            "Gender": self.gender_box.currentText(), 
            "Age": self.age_line.text(), 
            "Phone": self.phone_number_line.text(), 
            "Salary": self.salary_line.text(), 
            "E-Mail": self.mail_address_line.text(), 
            "Position / Description": self.pos_descr_line.text()
        }

        parsed[self.id_] = new_entry

        with open("index.json", "w") as f: 
            json.dump(parsed, f, indent=4, sort_keys=False)
            f.close()

        self.firstname_line.setReadOnly(True)
        self.lastname_line.setReadOnly(True)
        self.age_line.setReadOnly(True)
        self.phone_number_line.setReadOnly(True)
        self.mail_address_line.setReadOnly(True)
        self.salary_line.setReadOnly(True)
        self.gender_box.setEnabled(False)
        self.pos_descr_line.setReadOnly(True)

        self.render()

    def cancel(self):
        self.buttons_layout.removeWidget(self.save_button)
        self.buttons_layout.removeWidget(self.cancel_button)
        self.root.removeItem(self.buttons_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.modify_button)
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.delete_button)
        self.root.addLayout(self.buttons_layout)
        self.save_button.hide()
        self.cancel_button.hide()
        self.modify_button.show()
        self.delete_button.show() 

        self.firstname_line.setReadOnly(True)
        self.lastname_line.setReadOnly(True)
        self.age_line.setReadOnly(True)
        self.phone_number_line.setReadOnly(True)
        self.mail_address_line.setReadOnly(True)
        self.salary_line.setReadOnly(True)
        self.gender_box.setEnabled(False)
        self.pos_descr_line.setReadOnly(True)
        