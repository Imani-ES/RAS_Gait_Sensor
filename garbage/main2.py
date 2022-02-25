import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.stacked_widget.currentChanged.connect(self.set_button_state)
        self.page_1.clicked.connect(self.first_page)
        self.page_2.clicked.connect(self.second_page)
        self.page_3.clicked.connect(self.third_page)
        self.page_4.clicked.connect(self.fourth_page)
        self.page_5.clicked.connect(self.fifth_page)
        self.page_6.clicked.connect(self.sixth_page)


    def initUI(self):

        self.page_1 = QPushButton('Home')
        self.page_2 = QPushButton('About')
        self.page_3 = QPushButton('Connect')
        self.page_4 = QPushButton('View')
        self.page_5 = QPushButton('Audio')
        self.page_6 = QPushButton('Settings')

        self.page_1.setEnabled(False)
        self.page_2.setEnabled(False)
        self.page_3.setEnabled(False)
        self.page_4.setEnabled(False)
        self.page_5.setEnabled(False)
        self.page_6.setEnabled(False)

        self.stacked_widget = QStackedWidget()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.page_1)
        hbox.addWidget(self.page_2)
        hbox.addWidget(self.page_3)
        hbox.addWidget(self.page_4)
        hbox.addWidget(self.page_5)
        hbox.addWidget(self.page_6)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stacked_widget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


    def set_button_state(self, index):
        self.page_1.setEnabled(index != 0)
        self.page_2.setEnabled(index != 1)
        self.page_3.setEnabled(index != 2)
        self.page_4.setEnabled(index != 3)
        self.page_5.setEnabled(index != 4)
        self.page_6.setEnabled(index != 5)

        n_pages = len(self.stacked_widget)

    def insert_page(self, widget, index=-1):
        self.stacked_widget.insertWidget(index, widget)
        self.set_button_state(self.stacked_widget.currentIndex())

    def first_page(self):
        self.stacked_widget.setCurrentIndex(0)
        

    def second_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def third_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def fourth_page(self):
        self.stacked_widget.setCurrentIndex(3)

    def fifth_page(self):
        self.stacked_widget.setCurrentIndex(4)

    def sixth_page(self):
        self.stacked_widget.setCurrentIndex(5)

if __name__ == '__main__':

    app = QApplication([])
    ex = Example()
    for i in range(6):
        ex.insert_page(QLabel(f'This is page {i+1}'))
    ex.resize(1080,720)
    ex.show()
    app.exec()
