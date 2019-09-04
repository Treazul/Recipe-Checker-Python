import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog
import main as m


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Ark Dye Checker'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    # TODO: Pretty up the UI generally
    # TODO: Try and reduce the load and file-size if needed
    # TODO: Explain myself better, I need more comments.
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Load up the ability to choose
        choice = self.get_choice
        # Initialize variables
        color_result = list(m.color_result(choice))
        ingredients = color_result[0]
        hex_code = color_result[1]
        i = 0
        if len(color_result) == 2:
            header = QLabel("To make " + choice + " you use the following ingredients", self)
            header.move(30, 30)
            for x, y in ingredients.items():
                ingredient = QLabel(x, self)
                amount = QLabel(str(y), self)
                ingredient.move(50, 50 + i)
                ingredient.setStyleSheet("QLabel { font-weight: Bold;}")
                amount.move(160, 50 + i)
                i += 20
            for x, y in hex_code.items():
                label = QLabel(x, self)
                code = QLabel(y, self)
                label.move(50, 50 + i)
                label.setStyleSheet("QLabel { font-weight: Bold;}")

                code.move(160, 50 + i)
        else:
            label_warning = QLabel("Something went wrong! Please tell the creator as soon as possible. No error code "
                                   "has been logged", self)
            label_warning.setWordWrap(True)
            label_warning.move(50, 50)
        # Load a button to go back
        choose_again = QPushButton('Choose Again', self)
        choose_again.setToolTip('Go back to the choices')
        choose_again.move(50, 100 + i)
        choose_again.clicked.connect(self.on_click)
        exit_button = QPushButton('Close', self)
        exit_button.setToolTip('Close the program')
        exit_button.move(200, 100 + i)
        exit_button.clicked.connect(self.exit_click)

        # Show the Gui
        self.show()

    @property
    def get_choice(self):
        items = m.all_colors()
        item, ok_pressed = QInputDialog.getItem(self, "Color Choice", "Color:", items, 0, False)
        if ok_pressed and item:
            return item
        else:
            exit()

    @pyqtSlot()
    def on_click(self):
        self.close()
        self.__init__()

    @pyqtSlot()
    def exit_click(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
