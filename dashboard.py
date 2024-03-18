import sys
import time
import random
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView

class Speedometer(QObject):
     speedChanged = QtCore.pyqtSignal()      # This actually doesn't do anything since qml doesn't have a function. But just keep it in case.

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

class RPM_meter(QObject):
     RPMChanged = QtCore.pyqtSignal()      # This actually doesn't do anything since qml doesn't have a function. But just keep it in case.

     def __init__(self, parent=None):
          super(RPM_meter, self).__init__(parent)
          self._maxRPM = 10.0
          self._minRPM = 0.0
          self._currRPM = 0.0

     @pyqtProperty(float, notify=RPMChanged)
     def currRPM(self):
          return self._currRPM

     @currRPM.setter
     def currRPM(self, value):
          self._currRPM = value
          self.RPMChanged.emit()

     @pyqtProperty(float)
     def maxRPM(self):
          return self._maxRPM

     @pyqtProperty(float)
     def minRPM(self):
          return self._minRPM

     @QtCore.pyqtSlot(float, float, float)
     def setAllValues(self, currRPM, maxRPM, minRPM):
          self._currRPM = currRPM
          self._maxRPM = maxRPM
          self._minRPM = minRPM
          self.RPMChanged.emit()


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
     random_rpm = random.uniform(0, 10)
     random_int = random.randint(0, 300)
     random_battery = random.randint(0, 100)
     temperature_meter.mainValue = random_int
     speedometer.currSpeed = random_float
     battery_capacity.mainValue = random_battery
     rpmmeter.currRPM = random_rpm



if __name__ == "__main__":
     app = QApplication(sys.argv)
     view = QQuickView()
     view.setSource(QUrl('dashboard.qml'))
     engine = view.engine()
     timer = QTimer()
     # Create classes for each component
     temperature_meter = BarMeter()
     battery_capacity = BarMeter()
     speedometer = Speedometer()
     rpmmeter = RPM_meter()

     # Sets the  object for the qml to refer to. Only needs to be done once for each object.
     engine.rootContext().setContextProperty("speedometer", speedometer)
     engine.rootContext().setContextProperty("temperature_meter", temperature_meter)
     engine.rootContext().setContextProperty("battery_capacity", battery_capacity)
     engine.rootContext().setContextProperty("RPM_Meter", rpmmeter)



     # Set initial values
     speedometer.setAllValues(0.0, 160.0, 0.0)
     speedometer.currSpeed = 60.0
     temperature_meter.setAllValues(0.0, 300.0, 0.0)
     temperature_meter.mainValue = 270.0
     battery_capacity.setAllValues(0.0, 100.0, 0.0)
     battery_capacity.mainValue = 50.0
     rpmmeter.setAllValues(0.0, 10.0, 0.0)
     view.update()
     view.show()

     # After one second, values are changed via change_val function
     for i in range(10):
          timer.timeout.connect(change_val)
          timer.start(1000)


     sys.exit(app.exec_())
