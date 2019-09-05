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
        self.width = 480
        self.height = 400
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
        default_y_value = 70
        default_x_value = 110
        default_x_value_2 = default_x_value * 2.5
        header_y_value = 30
        button_y_value = default_y_value + 60
        header_x_value = 12

        if len(color_result) == 2:
            header = QLabel("To make " + choice + " dye you use the following ingredients", self)
            header.move(header_x_value, header_y_value)
            header.setStyleSheet("QLabel { font: bold 18px; border-bottom-width: 2px; border-bottom-color: black; "
                                 "border-style: outset; border-radius: 10px; }")
            for x, y in ingredients.items():
                ingredient = QLabel(x, self)
                amount = QLabel(str(y), self)
                ingredient.move(default_x_value, default_y_value + i)
                ingredient.setStyleSheet("QLabel { font: bold;}")
                amount.move(default_x_value_2, default_y_value + i)
                i += 22
            for x, y in hex_code.items():
                label = QLabel(x, self)
                code = QLabel(y, self)
                label.move(default_x_value, default_y_value + i)
                label.setStyleSheet("QLabel { font: bold;}")
                code.move(default_x_value_2, default_y_value + i)
        else:
            label_warning = QLabel("Something went wrong! Please tell the creator as soon as possible. No error code "
                                   "has been logged", self)
            label_warning.setWordWrap(True)
            label_warning.move(50, 50)
        # Load a button to go back
        choose_again = QPushButton('Choose Again', self)
        choose_again.setToolTip('Go back to the choices')
        choose_again.move(default_x_value, button_y_value + i)
        choose_again.clicked.connect(self.on_click)
        exit_button = QPushButton('Close', self)
        exit_button.setToolTip('Close the program')
        exit_button.move(default_x_value * 2.2, button_y_value + i)
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
