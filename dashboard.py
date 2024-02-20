import sys
import time
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView

if __name__ == "__main__":

     app = QApplication(sys.argv)
     view = QQuickView()
     view.setSource(QUrl('dashboard.qml'))
     engine = view.engine()
     rot = 4000.0
     engine.rootContext().setContextProperty('gauge_value', rot)
     view.show()
     rot = 0.0
     engine.rootContext().setContextProperty('gauge_value', rot)
     view.update()
     view.show()
     sys.exit(app.exec_())