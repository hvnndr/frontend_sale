# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(190, 60, 196, 251))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.head = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Navilu")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.head.setFont(font)
        self.head.setObjectName("head")
        self.verticalLayout_2.addWidget(self.head)
        self.login_fields = QtWidgets.QWidget(self.widget_2)
        self.login_fields.setObjectName("login_fields")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_fields)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_id_employee = QtWidgets.QLabel(self.login_fields)
        self.lbl_id_employee.setObjectName("lbl_id_employee")
        self.verticalLayout_3.addWidget(self.lbl_id_employee)
        self.lineedit_id_employee = QtWidgets.QLineEdit(self.login_fields)
        self.lineedit_id_employee.setObjectName("lineedit_id_employee")
        self.verticalLayout_3.addWidget(self.lineedit_id_employee)
        self.lbl_password = QtWidgets.QLabel(self.login_fields)
        self.lbl_password.setObjectName("lbl_password")
        self.verticalLayout_3.addWidget(self.lbl_password)
        self.lineedit_password = QtWidgets.QLineEdit(self.login_fields)
        self.lineedit_password.setObjectName("lineedit_password")
        self.verticalLayout_3.addWidget(self.lineedit_password)
        self.verticalLayout_2.addWidget(self.login_fields)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 22))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuLogin.addAction(self.actionLogin)
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.head.setText(_translate("MainWindow", "BitShop"))
        self.lbl_id_employee.setText(_translate("MainWindow", "ID Employee"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.menuLogin.setTitle(_translate("MainWindow", "Menu"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))