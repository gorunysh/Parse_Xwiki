# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_from_XWiki_to_xlsx.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import Read_HTML_table
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_app_from_XWiki_to_xlsx(object):
    def setupUi(self, app_from_XWiki_to_xlsx):
        app_from_XWiki_to_xlsx.setObjectName("app_from_XWiki_to_xlsx")
        app_from_XWiki_to_xlsx.resize(800, 600)
        app_from_XWiki_to_xlsx.setMinimumSize(QtCore.QSize(800, 600))
        app_from_XWiki_to_xlsx.setMaximumSize(QtCore.QSize(800, 600))
        app_from_XWiki_to_xlsx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(app_from_XWiki_to_xlsx)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_save.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid;\n"
"border-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover {    background-color: rgb(154, 206, 235); }\n"
"\n"
"QPushButton: pressed { background-color: rgb(238, 238, 238)}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_start.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);\n"
"border-radius: 3px;\n"
"border: 1px solid;\n"
"border-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover {    background-color: rgb(154, 206, 235); }\n"
"\n"
"QPushButton: pressed { background-color: rgb(238, 238, 238)}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.gridLayout.addWidget(self.lineEdit_login, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout_2.addWidget(self.label_password, 0, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_2.addWidget(self.lineEdit_password, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_url.setFont(font)
        self.label_url.setObjectName("label_url")
        self.gridLayout_3.addWidget(self.label_url, 0, 0, 1, 1)
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_url.setFont(font)
        self.lineEdit_url.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.gridLayout_3.addWidget(self.lineEdit_url, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_pattern_name = QtWidgets.QLabel(self.centralwidget)
        self.label_pattern_name.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_pattern_name.setFont(font)
        self.label_pattern_name.setObjectName("label_pattern_name")
        self.gridLayout_4.addWidget(self.label_pattern_name, 0, 0, 1, 1)
        self.lineEdit_pattern_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pattern_name.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_pattern_name.setFont(font)
        self.lineEdit_pattern_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_pattern_name.setObjectName("lineEdit_pattern_name")
        self.gridLayout_4.addWidget(self.lineEdit_pattern_name, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_save_name = QtWidgets.QLabel(self.centralwidget)
        self.label_save_name.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_save_name.setFont(font)
        self.label_save_name.setObjectName("label_save_name")
        self.gridLayout_5.addWidget(self.label_save_name, 0, 0, 1, 1)
        self.lineEdit_save_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_save_name.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_save_name.setFont(font)
        self.lineEdit_save_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_save_name.setObjectName("lineEdit_save_name")
        self.gridLayout_5.addWidget(self.lineEdit_save_name, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_number_table = QtWidgets.QLabel(self.centralwidget)
        self.label_number_table.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_number_table.setFont(font)
        self.label_number_table.setObjectName("label_number_table")
        self.gridLayout_6.addWidget(self.label_number_table, 0, 0, 1, 1)
        self.lineEdit_number_table = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_table.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_number_table.setFont(font)
        self.lineEdit_number_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid;")
        self.lineEdit_number_table.setObjectName("lineEdit_number_table")
        self.gridLayout_6.addWidget(self.lineEdit_number_table, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        app_from_XWiki_to_xlsx.setCentralWidget(self.centralwidget)

        self.retranslateUi(app_from_XWiki_to_xlsx)
        QtCore.QMetaObject.connectSlotsByName(app_from_XWiki_to_xlsx)

    def retranslateUi(self, app_from_XWiki_to_xlsx):
        _translate = QtCore.QCoreApplication.translate
        app_from_XWiki_to_xlsx.setWindowTitle(_translate("app_from_XWiki_to_xlsx", "Таблица из Xwiki"))
        self.pushButton_save.setText(_translate("app_from_XWiki_to_xlsx", "Сохранить"))
        self.pushButton_start.setText(_translate("app_from_XWiki_to_xlsx", "Старт"))
        self.label_login.setText(_translate("app_from_XWiki_to_xlsx", "Логин"))
        self.label_password.setText(_translate("app_from_XWiki_to_xlsx", "Пароль"))
        self.label_url.setText(_translate("app_from_XWiki_to_xlsx", "Ссылка на Xwiki"))
        self.label_pattern_name.setText(_translate("app_from_XWiki_to_xlsx", "Имя шаблона"))
        self.label_save_name.setText(_translate("app_from_XWiki_to_xlsx", "Имя файла для сохранения"))
        self.label_number_table.setText(_translate("app_from_XWiki_to_xlsx", "Номер таблицы"))


class App_from_XWiki_to_xlsx(QtWidgets.QMainWindow, Ui_app_from_XWiki_to_xlsx):

    def __init__(self, config_name: str):
        super().__init__()
        self.setupUi(self)

        self.config_name = config_name
        self.message_text = ''

        self.pushButton_save.clicked.connect(self.save_json)
        self.pushButton_start.clicked.connect(self.start_main)

        self.first_data = Read_HTML_table.open_json_for_QT(config_name)


        self.lineEdit_login.setText(self.first_data['login'])

        if 'Введите' in self.first_data['password']:
            self.lineEdit_password.setText(self.first_data['password'])
        else:
            self.lineEdit_password.setText('*')

        self.lineEdit_url.setText(self.first_data['url'])
        self.lineEdit_pattern_name.setText(self.first_data['pattern_name'])
        self.lineEdit_save_name.setText(self.first_data['save_name'])
        self.lineEdit_number_table.setText(self.first_data['number_table'])

        self.close()

    def save_json(self):

        self.second_data = {
            'login': self.lineEdit_login.text(),
            'url': self.lineEdit_url.text(),
            'pattern_name': self.lineEdit_pattern_name.text(),
            'save_name': self.lineEdit_save_name.text(),
            'number_table': self.lineEdit_number_table.text(),
        }

        if self.lineEdit_password.text() == '*':
            self.second_data['password'] = self.first_data['password']
        else:
            self.second_data['password'] = self.lineEdit_password.text()

        if self.second_data != self.first_data:
            msg = QMessageBox.information(self, 'Внимание!', 'Данные обновлены')
            Read_HTML_table.save_json_for_QT(self.second_data, self.config_name)

    @pyqtSlot()
    def start_main(self):

        data = {
            'login': self.lineEdit_login.text(),
            'url': self.lineEdit_url.text(),
            'pattern_name': self.lineEdit_pattern_name.text(),
            'save_name': self.lineEdit_save_name.text(),
            'number_table': self.lineEdit_number_table.text(),
        }

        if self.lineEdit_password.text() == '*':
            data['password'] = self.first_data['password']
        else:
            data['password'] = self.lineEdit_password.text()


        exemplar = Read_HTML_table.Adventure_time()
        status_code = exemplar.registration_and_load_HTML_for_QT(url=data['url'], login=data['login'], password=data['password'])

        if status_code == 200:
            exemplar.parse_HTML(data['number_table'])
            self.message_text = exemplar.save_xslx_v4_for_QT(data['pattern_name'], data['save_name'])

        elif status_code == 401:
            self.message_text = 'Не верный логин или пароль или программа не может пройти авторизацию на сайте'
        elif status_code == 404:
            self.message_text = 'Сайт недоступен, проверьте правильность ссылки или работоспособность сайта'
        else:
            self.message_text = 'Ошибка соединения, статус код =' + str(status_code)

        # сохранение новых данных при старте
        if data != self.first_data:
            Read_HTML_table.save_json_for_QT(data, self.config_name)

        msg = QMessageBox.information(self, 'Внимание!', self.message_text)


def main_event(config_name: str):
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win_1 = App_from_XWiki_to_xlsx(config_name)
    win_1.show()
    sys.exit(app.exec_())
