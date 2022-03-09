import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

def startApp():
    app = QGuiApplication(sys.argv)

    #set up blue tooth  - threadsfor each raspberry?

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./main.qml')
    
    #set up music

    sys.exit(app.exec())

if __name__ == "__main__":
    startApp()
