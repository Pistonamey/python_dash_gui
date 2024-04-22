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
        self._currValue = 0.0   # For any numeric outputs
        self._stringValue = ""  # For any string outputs


    @pyqtProperty(float, notify=currValueChanged)
    def currValue(self):
        return self._currValue

    @currValue.setter
    def currValue(self, value):
        self._currValue = value
        self.currValueChanged.emit()


    @pyqtProperty(str, notify=currValueChanged)
    def stringValue(self):
        return self._stringValue

    @stringValue.setter
    def stringValue(self, value):
        self._stringValue = value
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

# Class that handles user interactions
class dashboardManager(QObject):
    @QtCore.pyqtSlot()
    def switch_dashboard(self):
        if view.source().toString() == "dashboard.qml":
            view.setSource(QUrl('dashboard2.qml'))
            view.update()
            view.show()
        else:
            view.setSource(QUrl('dashboard.qml'))
            view.update()
            view.show()

def change_val():
    random_float = random.uniform(0, 160)
    random_rpm = random.uniform(0, 10)
    random_int = random.randint(0, 300)

    random_battery = random.randint(0, 100)
    temperature.currValue = random_int
    speedometer.currSpeed = random_float
    battery_capacity.currValue = random_battery
    rpmmeter.currRPM = random_rpm

    intakePressureLabel.currValue = random_int
    intakeTempLabel.currValue = random_int
    runtimeLabel.currValue = random_int
    fuelLevelLabel.currValue = random_int
    fuelTypeLabel.stringValue = "Gasoline"

    engineLoadLabel.currValue = random_int
    throttlePosLabel.currValue = random_int
    barometricPressureLabel.currValue = random_int
    throttleAcceleratorLabel.currValue = random_int
    absoluteLoadLabel.currValue = random_int

    shortTermFuelTrimLabel.currValue = random_int
    longTermFuelTrimLabel.currValue = random_int
    throttlePosLabel.currValue = random_int
    distWithMILabel.currValue = random_int
    distDTCClearLabel.currValue = random_int
    evapVaporPressureLabel.currValue = random_int

    afr_ratioLabel.currValue = random_int





    centerScreen.currTime = datetime.datetime.now().strftime("%I:%M %p")
    centerScreen.currDate = datetime.datetime.now().strftime("%m/%d/%Y")



def to60(speedometer):

    if speedometer.__currSpeed != 0:
        print("Please be at a stop\n")
        return
    
    start_time = time.time()
    print("Ready to time 0-60\n")

    while speedometer.__currSpeed < 60:
        time.sleep(0.01)

    end_time = time.time()

    elapsed_time = end_time - start_time
    
    print("0-60: " + elapsed_time)

    with open('output.txt', 'a') as output:
        output.write(f"0-60 Time: {elapsed_time}.\n")

    return elapsed_time


def receiver(connection, speedometer, temperature, battery_capacity, rpmmeter):

    # Get data from OBD
    speed = py_obd.get_speed(connection)
    rpm = py_obd.get_rpm(connection)
    # temperature = py_obd.get_temperature(connection)
    # battery_level = py_obd.get_battery(connection)

    # Update PyQT Objects with data
    speedometer.currSpeed = speed.magnitude
    rpmmeter.currRPM = (rpm.magnitude)/1000
    temperature.currValue = random.randint(0, 300)
    battery_capacity.currValue = random.randint(0, 100)

    centerScreen.currTime = datetime.datetime.now().strftime("%I:%M %p")
    centerScreen.currDate = datetime.datetime.now().strftime("%m/%d/%Y")



def set_timer(connection):

    timer.timeout.connect(lambda: receiver(connection, speedometer, temperature, battery_capacity, rpmmeter))
    timer.start(50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl('dashboard.qml'))
    engine = view.engine()
    timer = QTimer()
    # Create classes for each component
    manager = dashboardManager()
    temperature = BarMeter()
    battery_capacity = BarMeter()
    speedometer = Speedometer()
    rpmmeter = RPM_meter()
    centerScreen = CenterScreenWidget()

    # Top labels, first row
    intakePressureLabel = Labels()
    intakeTempLabel = Labels()
    runtimeLabel = Labels()
    fuelLevelLabel = Labels()
    fuelTypeLabel = Labels()

    # Top labels, second row
    engineLoadLabel = Labels()
    throttlePosLabel = Labels()
    barometricPressureLabel = Labels()
    throttleAcceleratorLabel = Labels()
    absoluteLoadLabel = Labels()



    # The rest of them unused
    shortTermFuelTrimLabel = Labels()
    longTermFuelTrimLabel = Labels()
    distWithMILabel = Labels()
    distDTCClearLabel = Labels()
    evapVaporPressureLabel = Labels()
    timingAdvanceLabel = Labels()
    O2SensorsPresentLabel = Labels()
    fuelRailPressureDirectLabel = Labels()
    evaporativePurgeLabel = Labels()
    warmupsSinceDTCsClearedLabel = Labels()
    controlModuleVoltageLabel = Labels()
    throttlePosBLabel = Labels()
    acceleratorPosDLabel = Labels()
    acceleratorPosELabel = Labels()

    monitor_Boost_Pressure_B1_Object = object()




    afr_ratioLabel = Labels()

    # Sets the object for the qml to refer to. Only needs to be done once for each object.
    engine.rootContext().setContextProperty("manager", manager)
    engine.rootContext().setContextProperty("speedometer", speedometer)
    engine.rootContext().setContextProperty("temperature", temperature)
    engine.rootContext().setContextProperty("battery_capacity", battery_capacity)
    engine.rootContext().setContextProperty("RPM_Meter", rpmmeter)
    engine.rootContext().setContextProperty("centerScreen", centerScreen)

    # Sets context properties for 1st row
    engine.rootContext().setContextProperty("intakePressureLabel", intakePressureLabel)
    engine.rootContext().setContextProperty("intakeTempLabel", intakeTempLabel)
    engine.rootContext().setContextProperty("runtimeLabel", runtimeLabel)
    engine.rootContext().setContextProperty("fuelLevelLabel", fuelLevelLabel)
    engine.rootContext().setContextProperty("fuelTypeLabel", fuelTypeLabel)

    # Sets context properties for 2nd row
    engine.rootContext().setContextProperty("engineLoadLabel", engineLoadLabel)
    engine.rootContext().setContextProperty("throttlePosLabel", throttlePosLabel)
    engine.rootContext().setContextProperty("barometricPressureLabel", barometricPressureLabel)
    engine.rootContext().setContextProperty("throttleAcceleratorLabel", throttleAcceleratorLabel)
    engine.rootContext().setContextProperty("absoluteLoadLabel", absoluteLoadLabel)

    engine.rootContext().setContextProperty("shortTermFuelTrimLabel", shortTermFuelTrimLabel)
    engine.rootContext().setContextProperty("longTermFuelTrimLabel", longTermFuelTrimLabel)
    engine.rootContext().setContextProperty("distWithMILabel", distWithMILabel)
    engine.rootContext().setContextProperty("distDTCClearLabel", distDTCClearLabel)
    engine.rootContext().setContextProperty("evapVaporPressureLabel", evapVaporPressureLabel)
    engine.rootContext().setContextProperty("timingAdvanceLabel", timingAdvanceLabel)
    engine.rootContext().setContextProperty("O2SensorsPresentLabel", O2SensorsPresentLabel)
    engine.rootContext().setContextProperty("fuelRailPressureDirectLabel", fuelRailPressureDirectLabel)
    engine.rootContext().setContextProperty("evaporativePurgeLabel", evaporativePurgeLabel)
    engine.rootContext().setContextProperty("warmupsSinceDTCsClearedLabel", warmupsSinceDTCsClearedLabel)
    engine.rootContext().setContextProperty("controlModuleVoltageLabel", controlModuleVoltageLabel)
    engine.rootContext().setContextProperty("acceleratorPosDLabel", acceleratorPosDLabel)
    engine.rootContext().setContextProperty("acceleratorPosELabel", acceleratorPosELabel)
    engine.rootContext().setContextProperty("throttlePosBLabel", throttlePosBLabel)

    engine.rootContext().setContextProperty("afr_ratio", afr_ratioLabel)

    engine.rootContext().setContextProperty("monitor_Boost_Pressure_B1", monitor_Boost_Pressure_B1_Object)

    # Set initial values
    speedometer.setAllValues(0.0, 160.0, 0.0)
    speedometer.currSpeed = 60.0
    temperature.setAllValues(0.0, 300.0, 0.0)
    temperature.currValue = 270.0
    battery_capacity.setAllValues(0.0, 100.0, 0.0)
    battery_capacity.currValue = 50.0
    rpmmeter.setAllValues(0.0, 10.0, 0.0)


    view.update()
    view.show()

    timer.timeout.connect(change_val)
    timer.start(500)
    

    sys.exit(app.exec_())
