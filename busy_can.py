import math
import can
import threading
from time import sleep

def int_to_bytes(val: int):
    return val.to_bytes(math.ceil(math.log2(val)/8), 'big')

def battery():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
        
        count = 0
        dt = .001
        level = 80
        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x1, 
                    data=int_to_bytes(level), 
                    is_extended_id=False
                )
            )
            sleep(dt)
            count += dt
            level = 80 - count*10/60
    except KeyboardInterrupt:
        return

def speed():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 100

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x2, 
                    data=int_to_bytes(level), 
                    is_extended_id=False
                )
            )
            sleep(.01)
            if level == 1:
                level = 100
            level = level - 1
    except KeyboardInterrupt:
        return


def engineTemperature():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 200

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x3, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if level == 1:
                level = 200
            level = level - 1
            sleep(1)
    except KeyboardInterrupt:
        return

def tripComputer():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 50

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x4, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if level == 1:
                level = 50
            level = level - 1
            sleep(10)
    except KeyboardInterrupt:
        return
    
def accelerometer():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 200

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x5, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if level == 1:
                level = 200
            level = level - 1
            sleep(0.001)
    except KeyboardInterrupt:
        return

def tirePressure():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 100

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x6, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if level == 1:
                level = 100
            level = level - 1
            sleep(20)
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    threads = list()
    threads.append(threading.Thread(target=battery))
    threads.append(threading.Thread(target=speed))
    threads.append(threading.Thread(target=engineTemperature))
    threads.append(threading.Thread(target=tripComputer))
    threads.append(threading.Thread(target=accelerometer))
    threads.append(threading.Thread(target=tirePressure))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
        