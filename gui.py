import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QErrorMessage, QLineEdit, QLabel, \
    QInputDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import main as m


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.title = 'Ark Dye Checker'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Load up the ability to choose
        # self.get_choice()
        choice = list(m.color_result(self.get_choice()))
        ingredients = {}
        hexcode = {}
        if len(choice) == 2:
            ingredients = choice[0]
            hexcode = choice[1]
            self.tableWidget.setRowCount(len(ingredients))
            self.tableWidget.setColumnCount(2)
            i = 0
            for x, y in ingredients.items():
                self.tableWidget.setItem(i, 0, QTableWidgetItem(x))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(y))
                self.tableWidget.move(50, 50)
                i += 1
        else:
            label = QLabel("Something went wrong! Please tell the creator as soon as possible. No error code has been "
                           "logged)")
            label.move(50, 50)
        # Show the Gui
        self.show()

    def get_choice(self):
        items = m.all_colors()
        item, ok_pressed = QInputDialog.getItem(self, "Color Choice", "Color:", items, 0, False)
        if ok_pressed and item:
            return item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
