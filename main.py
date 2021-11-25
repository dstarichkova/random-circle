import sys
from random import randint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(400, 400)
        self.btn = QtWidgets.QPushButton(widget)
        self.btn.setGeometry(QtCore.QRect(10, 10, 151, 32))
        self.btn.setObjectName("btn")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Нарисовать круги"))
        self.btn.setText(_translate("widget", "Нарисовать круги"))


class Example(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            radius = randint(1, 200)
            qp.drawEllipse(randint(1, 400), randint(1, 400), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
