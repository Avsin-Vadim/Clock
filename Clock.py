import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from datetime import timedelta, datetime

# Переменная для разници во времени
deltaTime = 0


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # Открываем файлик ui с нашим интерфейсом
        uic.loadUi('main1.ui', self)
        # Запускаем функциии
        self.My.clicked.connect(self.timeMy)
        self.Berlin.clicked.connect(self.timeBerlin)
        self.NewYork.clicked.connect(self.timeNew)
        self.London.clicked.connect(self.timeLondonParish)
        self.Parish.clicked.connect(self.timeLondonParish)
        self.Vladivostok.clicked.connect(self.timeVladivostok)
        self.California.clicked.connect(self.timeCalifornia)
        # Для создания своей кнопки:
        # self.*НазваниеГорода*.clicked.connect(self.time*НазваниеГорода*)
        now = datetime.now()
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))

    # Описываем функции

    # Для создания своей кнопки:
    # def time*НазваниеГорода*(self):
    #     global a
    #     a = *Разница во времени с вашим городом*
    #     now = datetime.now() + timedelta(hours=a)
    #     self.cr.setText(
    #         "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
    #                                     now.minute, now.second))

    def timeCalifornia(self):
        global deltaTime
        deltaTime = -11
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))

    def timeMy(self):
        global deltaTime
        deltaTime = 0
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))

    def timeBerlin(self):
        global deltaTime
        deltaTime = -2
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))

    def timeLondonParish(self):
        global deltaTime
        deltaTime = -3
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year,
                                        now.hour,
                                        now.minute, now.second))

    def timeNew(self):
        global deltaTime
        deltaTime = -8
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))

    def timeVladivostok(self):
        global deltaTime
        deltaTime = 7
        now = datetime.now() + timedelta(hours=deltaTime)
        self.cr.setText(
            "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour,
                                        now.minute, now.second))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
