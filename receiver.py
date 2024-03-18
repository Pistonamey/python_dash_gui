#!/usr/bin/env python3
import can
import os
import sys
from threading import Thread
from dashboard import BarMeter, Speedometer
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

# CAN Bus configuration parameters here!
channel = 'vcan0'
bitrate = 500000

#Try to bring can bus up
try:
    os.system("sudo ip link add dev "+channel+" type vcan")
    os.system("sudo ip link set "+channel+" up")
    # For regular CAN do this instead
    # os.system('sudo ip link set '+channel+' type '+(channel[:-2])+' bitrate '+str(bitrate))
except OSError:
    if channel == 'vcan0':
        print("Unable to set up vcan. Does vcan exist yet?")
    else:
        print("CAN Bus or PiCAN not detected. Please check the cables")
    sys.exit(1)

bus = can.Bus(interface='socketcan', channel=channel, bitrate=bitrate)

# Each device that we want to display data for is included in this table.
# TODO: change to list of classes or maybe list of tuples
devices = [
    # instead of a scale maybe we could have a convert function?
    # That converts the raw CAN data into the format we want.
    # Sometimes, you might not need a linear transformation of the data.
    # This is where this comes in handy!
    # {id, variable to bind, scale, offset}
    # {"id": 0x03, "var": temperature_meter, "scale": 1, "offset" : 0}",
    # {"id": 0x01, "var": battery_capacity, "scale": 1, "offset" : 0},
    # {"id": 0x02, "var": speedometer, "scale": 1, "offset" : 0},
]

def can_receiver():
    bus.send(
        can.Message(
            arbitration_id=0x1EF,
            data=[0, 0x69, 0x42, 10, 12, 31, 0x45, 0x11],
            is_extended_id=False
        )
    )

    try:
        while True:
            msg = bus.recv()

            val = int.from_bytes(msg.data, 'big')
            id = msg.arbitration_id

            if 0x01 == id:
                battery_capacity.mainValue = val
            elif 0x02 == id:
                speedometer.currSpeed = val
            elif 0x03 == id:
                temperature_meter.mainValue = val
    except:
        bus.shutdown()


app = QApplication(sys.argv)
view = QQuickView()
view.setSource(QUrl('dashboard.qml'))
engine = view.engine()

temperature_meter = BarMeter()
battery_capacity = BarMeter()
speedometer = Speedometer()

def gui_setup():
    # Sets the  object for the qml to refer to. Only needs to be done once for each object.
    engine.rootContext().setContextProperty("speedometer", speedometer)
    engine.rootContext().setContextProperty("temperature_meter", temperature_meter)
    engine.rootContext().setContextProperty("battery_capacity", battery_capacity)

    # Set initial values
    speedometer.setAllValues(0.0, 160.0, 0.0)
    speedometer.currSpeed = 0.0
    temperature_meter.setAllValues(0.0, 300.0, 0.0)
    temperature_meter.mainValue = 0.0
    battery_capacity.setAllValues(0.0, 100.0, 0.0)
    battery_capacity.mainValue = 100.0
    view.update()
    view.show()

if __name__ == "__main__":
    can_thread = Thread(target=can_receiver)
    can_thread.daemon = True
    can_thread.start()

    gui_setup()
    ret = app.exec_()
    bus.shutdown()
    sys.exit(ret)