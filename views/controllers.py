from PyQt5.QtWidgets import QMainWindow


from views.mainwindow import Ui_MainWindow
from views.services import BaseService


class MainWindowController(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent=None)
        self.setupUi(self)
        self.service = BaseService()
        self.pushButton.clicked.connect(self._login)


    def _login(self):
        json_employee = self.service.search(router=f'employee/{self.lineedit_id_employee.text()}/')
        print(json_employee['name'])














