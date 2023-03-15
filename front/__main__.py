import sys

from PySide2.QtWidgets import QApplication
from front.loginWindow import LoginWindow


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()

    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
