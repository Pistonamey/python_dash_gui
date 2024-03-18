#!/usr/bin/env python3
import math
import can
import threading
from time import sleep

def int_to_bytes(val: int):
    length = max(1, math.ceil(math.log2(max(val, 1))/8))
    return val.to_bytes(length, 'big')

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
            level = int(80 - count*10/60)
            
            if level <= 0:
                level = 80
                count = 0
            	
    except KeyboardInterrupt:
        bus.shutdown()
        return

def speed():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 100
        forward = False

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x2, 
                    data=int_to_bytes(level), 
                    is_extended_id=False
                )
            )

            if forward: level = level + 1
            else: level = level - 1

            if level == 100 or level == 1:
                forward = not forward

            sleep(.01)
    except KeyboardInterrupt:
        bus.shutdown()
        return


def engineTemperature():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 170
        forward = True

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x3, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )

            if forward:
                level = level + 1
            else:
                level = level - 1

            if level == 190 or level == 170:
                forward = not forward

            sleep(1)
    except KeyboardInterrupt:
        bus.shutdown()
        return

def tripComputer():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 50
        forward = False

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x4, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )

            if forward: level = level + 1
            else: level = level - 1

            if level == 1 or level == 50:
                forward = not forward

            sleep(10)
    except KeyboardInterrupt:
        bus.shutdown()
        return
    
def accelerometer():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 200
        forward = False

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x5, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if forward: level = level + 1
            else: level = level - 1

            if level == 200 or level == 0:
                forward = not forward

            sleep(0.001)
    except KeyboardInterrupt:
        bus.shutdown()
        return

def tirePressure():
    try:
        bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=50000)

        level = 100
        forward = False

        while True:
            bus.send(
                can.Message(
                    arbitration_id=0x6, 
                    data=int_to_bytes(level),
                    is_extended_id=False
                )
            )
            if forward: level = level + 1
            else: level = level - 1

            if level == 100 or level == 0:
                forward = not forward
            sleep(20)
    except KeyboardInterrupt:
        bus.shutdown()
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
        
