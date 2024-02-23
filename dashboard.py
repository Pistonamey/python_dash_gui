import sys
import time
import random
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView

class Speedometer(QObject):
     speedChanged = QtCore.pyqtSignal()

     def __init__(self, parent=None):
          super(Speedometer, self).__init__(parent)
          self._maxSpeed = 160.0
          self._minSpeed = 0.0
          self._currSpeed = 0.0

     @pyqtProperty(float, notify=speedChanged)
     def currSpeed(self):
          return self._currSpeed

     @currSpeed.setter
     def currSpeed(self, value):
          self._currSpeed = value
          self.speedChanged.emit()

     @pyqtProperty(float)
     def maxSpeed(self):
          return self._maxSpeed

     @pyqtProperty(float)
     def minSpeed(self):
          return self._minSpeed

     @QtCore.pyqtSlot(float, float, float)
     def setAllValues(self, currSpeed, maxSpeed, minSpeed):
          self._currSpeed = currSpeed
          self._maxSpeed = maxSpeed
          self._minSpeed = minSpeed
          self.speedChanged.emit()


class BarMeter(QObject):
     mainValueChanged = QtCore.pyqtSignal()

     def __init__(self, parent=None):
          super(BarMeter, self).__init__(parent)
          self._mainValue = 0.0
          self._maxSpeed = 0.0
          self._minSpeed = 0.0


     @pyqtProperty(float, notify=mainValueChanged)
     def mainValue(self):
          return self._mainValue

     @mainValue.setter
     def mainValue(self, value):
          self._mainValue = value
          self.mainValueChanged.emit()

     @pyqtProperty(float)
     def maxValue(self):
          return self._maxSpeed

     @mainValue.setter
     def mainValue(self, value):
          self._mainValue = value
          self.mainValueChanged.emit()

     @pyqtProperty(float)
     def minValue(self):
          return self._minSpeed

     @QtCore.pyqtSlot(float, float, float)
     def setAllValues(self, mainValue, maxValue, minValue):
          self._mainValue = mainValue
          self._maxSpeed = maxValue
          self._minSpeed = minValue
          self.mainValueChanged.emit()

def change_val():
     random_float = random.uniform(0, 160)
     random_int = random.randint(0, 300)
     temperature_meter.mainValue = random_int
     speedometer.currSpeed = random_float




if __name__ == "__main__":

     app = QApplication(sys.argv)
     view = QQuickView()
     view.setSource(QUrl('dashboard.qml'))
     engine = view.engine()
     timer = QTimer()
     # Create classes for each component
     temperature_meter = BarMeter()
     speedometer = Speedometer()

     # Sets the  object for the qml to refer to. Only needs to be done once for each object.
     engine.rootContext().setContextProperty("speedometer", speedometer)
     engine.rootContext().setContextProperty("temperature_meter", temperature_meter)

     # Set initial values
     speedometer.setAllValues(0.0, 160.0, 0.0)
     speedometer.currSpeed = 60.0
     temperature_meter.setAllValues(0.0, 300.0, 0.0)
     temperature_meter.mainValue = 270.0
     view.update()
     view.show()

     # After one second, values are changed via change_val function
     for i in range(10):
          timer.timeout.connect(change_val)
          timer.start(1000)
     


     sys.exit(app.exec_())
