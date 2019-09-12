#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Создание простейшей визуальной программы на Python')

        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.label_img.setPixmap(QPixmap('main.png'))
        self.label_img.setScaledContents(True)

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            c = float(self.lineEdit_c.text())
            d = float(self.lineEdit_d.text())
            if x <= 5:
                answer = ((a ** 2) * c) + ((b ** 2) - d ) / x
            else:
                answer = (x ** 2) + 5
            self.label_answer.setText('Ответ: ' + format(answer, '.3f'))
        except:
            self.label_answer.setText('Ошибка')

    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ваш ответ: ')


app = QApplication(sys.argv)
window = Main()  # базовый класс для всех объектов интерфейса пользователя
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
