import sys

from PyQt5.QtWidgets import QApplication


from views.controllers import MainWindowController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowController()
    window.show()
    sys.exit(app.exec_())

