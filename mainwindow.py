# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3

class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Add new list'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        if (textboxValue == ''):
            textboxValue = ("لطفا فیلد را صحیح وارد کنید")
            QMessageBox.question(self, 'Message', textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")
        else:


            result = itemss()
            r = result.items_list()
            r.append(textboxValue)
            print(type(r),len(r))

            QMessageBox.question(self, 'Message', " لیست " + textboxValue + " با موفقیت اضافه شد ", QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.setWindowTitle("Combobox PyQt5")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()


    def UiComponents(self):

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 150, 120, 30)

        result = itemss()
        r = result.items_list()
        self.combo_box.addItems(r)


        btn1 = QPushButton('Show', self)
        btn1.pressed.connect(self.find)
        self.label = QLabel(self)
        self.label.setGeometry(200, 200, 200, 30)
        btn1.resize(100,30)
        btn1.move(100, 150)
        btn1.setToolTip('Show content')

        btn2 = QPushButton('New', self)
        btn2.clicked.connect(self.show_new_window)
        btn2.resize(100,30)
        btn2.move(320, 150)
        btn2.setToolTip('Add a new content')

        btn3 = QPushButton('-', self)
        btn3.resize(100,30)
        btn3.move(420, 150)
        btn3.setToolTip('Remove this content')

    def find(self):
        content = self.combo_box.currentText()
        self.label.setText("Content : " + content)

    def show_new_window(self, checked):
        self.w.show()

class itemss():

    def items_list(self):
        items = ["linux", "windows", "mac"]
        return items


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
