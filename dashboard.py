import sys
import time
import random
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty, QThread, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView
import datetime
import time
import py_obd
import obd


class Speedometer(QObject):
    speedChanged = QtCore.pyqtSignal()  # This actually doesn't do anything since qml doesn't have a function. But just keep it in case.

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
    RPMChanged = QtCore.pyqtSignal()  # This actually doesn't do anything since qml doesn't have a function. But just keep it in case.

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
    currValueChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(BarMeter, self).__init__(parent)
        self._currValue = 0.0
        self._maxSpeed = 0.0
        self._minSpeed = 0.0

    @pyqtProperty(float, notify=currValueChanged)
    def currValue(self):
        return self._currValue

    @currValue.setter
    def currValue(self, value):
        self._currValue = value
        self.currValueChanged.emit()

    @pyqtProperty(float)
    def maxValue(self):
        return self._maxSpeed

    @pyqtProperty(float)
    def minValue(self):
        return self._minSpeed

    def setCurrValue(self, value):
        self._currValue = value
        self.currValueChanged.emit()

    @QtCore.pyqtSlot(float, float, float)
    def setAllValues(self, currValue, maxValue, minValue):
        self._currValue = currValue
        self._maxSpeed = maxValue
        self._minSpeed = minValue
        self.currValueChanged.emit()


class Labels(QObject):
    currValueChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Labels, self).__init__(parent)
        self._currValue = 0.0

    @pyqtProperty(float, notify=currValueChanged)
    def currValue(self):
        return self._currValue

    @currValue.setter
    def currValue(self, value):
        self._currValue = value
        self.currValueChanged.emit()

    @QtCore.pyqtSlot(float, float, float)
    def setAllValues(self, currValue):
        self._currValue = currValue
        self.currValueChanged.emit()

class CenterScreenWidget(QObject):
    currTimeChanged = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(CenterScreenWidget, self).__init__(parent)
        self._currTime = datetime.datetime.now().strftime("%I:%M %p")
        self._currDate = datetime.datetime.now().strftime("%m/%d/%Y")

    @pyqtProperty(str, notify=currTimeChanged)
    def currTime(self):
        return self._currTime

    @currTime.setter
    def currTime(self, value):
        self._currTime = value
        self.currTimeChanged.emit()

    @pyqtProperty(str, notify=currTimeChanged)
    def currDate(self):
        return self._currDate

    @currDate.setter
    def currDate(self, value):
        self._currDate = value
        self.currTimeChanged.emit()


def change_val():
    random_float = random.uniform(0, 160)
    random_rpm = random.uniform(0, 10)
    random_int = random.randint(0, 300)

    random_battery = random.randint(0, 100)
    temperature.currValue = random_int
    speedometer.currSpeed = random_float
    battery_capacity.currValue = random_battery
    rpmmeter.currRPM = random_rpm

    avg_speed.currValue = random_int
    od_partial.currValue = random_int
    consumption.currValue = random_int
    driveable.currValue = random_int

    centerScreen.currTime = datetime.datetime.now().strftime("%I:%M %p")
    centerScreen.currDate = datetime.datetime.now().strftime("%m/%d/%Y")






def receiver(connection, speedometer, temperature, battery_capacity, rpmmeter):

    # Get data from OBD
    speed = py_obd.get_speed(connection)
    rpm = py_obd.get_rpm(connection)
    temp = py_obd.get_temperature(connection)
    battery_level = py_obd.get_battery(connection)

    # Update PyQT Objects with data
    speedometer.currSpeed = speed
    rpmmeter.currRPM = rpm
    temperature.currValue = temp
    battery_capacity.currValue = battery_level

    centerScreen.currTime = datetime.datetime.now().strftime("%I:%M %p")
    centerScreen.currDate = datetime.datetime.now().strftime("%m/%d/%Y")

def poll_speed(connection):
    speed = py_obd.get_speed(connection)
    speedometer.currSpeed = speed
    with open('output.txt', 'a') as f:
        f.write("SPEED UPDATED\n")

def poll_rpm(connection):
    rpm = py_obd.get_rpm(connection)
    rpmmeter.currRPM = rpm
    with open('output.txt', 'a') as f:
        f.write("RPM UPDATED\n")

def poll_coolantTemp(connection):
    temp = py_obd.get_temperature(connection)
    temperature.currValue = temp
    with open('output.txt', 'a') as f:
        f.write("TEMP UPDATED\n")

def poll_fuel(connection):
    fuel = py_obd.get_battery(connection)
    battery_capacity.currValue = fuel
    with open('output.txt', 'a') as f:
        f.write("FUEL UPDATED\n")

def poll_time():
    centerScreen.currTime = datetime.datetime.now().strftime("%I:%M %p")
    centerScreen.currDate = datetime.datetime.now().strftime("%m/%d/%Y")
    with open('output.txt', 'a') as f:
        f.write("TIME UPDATED\n")



def set_timer(connection):
    speed_timer = QTimer()
    rpm_timer = QTimer()
    battery_timer = QTimer()
    temperature_timer = QTimer()
    date_timer = QTimer()

    speed_timer.timeout.connect(lambda: poll_speed(connection))
    rpm_timer.timeout.connect(lambda: poll_rpm(connection))
    battery_timer.timeout.connect(lambda: poll_fuel(connection))
    temperature_timer.timeout.connect(lambda: poll_coolantTemp(connection))
    date_timer.timeout.connect(lambda: poll_time())

    speed_timer.start(200) # Polling rate of speed 200 ms
    rpm_timer.start(200) # Polling rate of rpm 200 ms
    battery_timer.start(5000) # Polling rate of speed 5 s
    temperature_timer.start(5000) # Polling rate of speed 5 s
    date_timer.start(1000) # Polling rate of date and time 1 s

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl('dashboard.qml'))
    engine = view.engine()
    # Create classes for each component
    temperature = BarMeter()
    battery_capacity = BarMeter()
    speedometer = Speedometer()
    rpmmeter = RPM_meter()
    avg_speed = Labels()
    od_partial = Labels()
    consumption = Labels()
    driveable = Labels()
    centerScreen = CenterScreenWidget()
    

    # Sets the object for the qml to refer to. Only needs to be done once for each object.
    engine.rootContext().setContextProperty("speedometer", speedometer)
    engine.rootContext().setContextProperty("temperature", temperature)
    engine.rootContext().setContextProperty("battery_capacity", battery_capacity)
    engine.rootContext().setContextProperty("RPM_Meter", rpmmeter)
    engine.rootContext().setContextProperty("avg_speed", avg_speed)
    engine.rootContext().setContextProperty("od_partial", od_partial)
    engine.rootContext().setContextProperty("consumption", consumption)
    engine.rootContext().setContextProperty("driveable", driveable)
    engine.rootContext().setContextProperty("centerScreen", centerScreen)

    # Set initial values
    speedometer.setAllValues(0.0, 160.0, 0.0)
    speedometer.currSpeed = 60.0
    temperature.setAllValues(0.0, 300.0, 0.0)
    temperature.currValue = 270.0
    battery_capacity.setAllValues(0.0, 100.0, 0.0)
    battery_capacity.currValue = 50.0
    rpmmeter.setAllValues(0.0, 10.0, 0.0)
    avg_speed.setAllValues(0.0)
    od_partial.setAllValues(0.0)
    consumption.setAllValues(0.0)
    driveable.setAllValues(0.0)

    view.update()
    view.show()

    connection = obd.OBD() # auto-connects to USB or RF port

    print(connection.status())
    obd.logger.setLevel(obd.logging.DEBUG)
    py_obd.get_supported_pids_mode01(connection)
    py_obd.get_supported_pids_mode06(connection)
    set_timer(connection)
    
    # timer = QTimer()
    # timer.timeout.connect(lambda: receiver(connection, speedometer, temperature, battery_capacity, rpmmeter)
    # timer.start(500)
    

    sys.exit(app.exec_())
