import sys
import time
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView

class BarMeter(QObject):
     mainValueChanged = QtCore.pyqtSignal()

     def __init__(self, parent=None):
          super(BarMeter, self).__init__(parent)
          self._mainValue = 0.0
          self._maxValue = 0.0
          self._minValue = 0.0


     @pyqtProperty(float, notify=mainValueChanged)
     def mainValue(self):
          return self._mainValue

     @mainValue.setter
     def mainValue(self, value):
          self._mainValue = value
          self.mainValueChanged.emit()

     @pyqtProperty(float)
     def maxValue(self):
          return self._maxValue

     @mainValue.setter
     def mainValue(self, value):
          self._mainValue = value
          self.mainValueChanged.emit()

     @pyqtProperty(float)
     def minValue(self):
          return self._minValue

     @QtCore.pyqtSlot(float, float, float)
     def setAllValues(self, mainValue, maxValue, minValue):
          self._mainValue = mainValue
          self._maxValue = maxValue
          self._minValue = minValue
          self.mainValueChanged.emit()




if __name__ == "__main__":

     app = QApplication(sys.argv)
     view = QQuickView()
     view.setSource(QUrl('dashboard.qml'))
     engine = view.engine()
     rot = 4000.0
     engine.rootContext().setContextProperty('gauge_value', rot)
     view.show()
     rot = 111.0
     # I commented out the "property real gauge_value: 40.0" in the qml because apparently we can't have duplicate names between both the pyqt and qml.
     # The setConextProperty links the value "rot" to the qml and allows the qml to refer to it as "gauge_value".
     engine.rootContext().setContextProperty('gauge_value', rot)
     view.update()
     view.show()

     # Create temperature_meter using BarMeter Class
     temperature_meter = BarMeter()

     # Set the temperature meter as an object for the qml to refer to. Only needs to be done once for each object.
     # So in this case, qml can refer to "temperature_meter" and uses it's class like normal
     engine.rootContext().setContextProperty("temperature_meter", temperature_meter)

     # Setting values here will update qml too
     temperature_meter.setAllValues(0.0, 300.0, 0.0)
     temperature_meter.mainValue = 270.0


     sys.exit(app.exec_())

