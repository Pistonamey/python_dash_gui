#!/usr/bin/env python3 
import can
import os
import time
from obd_commands import ENGINE_COOLANT_TEMP, VEHICLE_SPEED, ENGINE_SPEED, BATTERY_LEVEL, ECU_IDS, FUEL_LEVEL

# Each device that we want to display data for is included in this table.
devices = [
    # instead of a scale maybe we could have a convert function?
    # That converts the raw CAN data into the format we want. 
    # Sometimes, you might not need a linear transformation of the data. 
    #This is where this comes in handy!
    #{name, id, variable_name, scale, offset},
    #{name, id, variable_name, convert_fn}
]

# CAN Bus configuration parameters here!
channel = 'vcan0'
bitrate = 500000

#Try to bring can bus up
try:
    # os.system("sudo ip link add dev "+channel+" type vcan")
    # os.system("sudo ip link set "+channel+" up")    
    # For regular CAN do this instead

    os.system('sudo ip link set '+channel+' type '+(channel[:-1])+' bitrate '+str(bitrate))
except OSError:
    if channel == 'vcan0':
        print("Unable to set up vcan. Does vcan exist yet?")
    else:
        print("CAN Bus or PiCAN not detected. Please check the cables")
    exit()

def msg_handler(msg: can.Message):
    id = msg.arbitration_id
    data = msg.data

    if id not in ECU_IDS or data[1] != 0x41:
        print(f"Ignoring this message {msg}")
        return
    
    pid = data[2]
    data = data[3:]

    print(f"Raw response: {msg}")

    if pid == VEHICLE_SPEED[2]:
        print(f"The car is moving at {data[0]*0.621371} mph")

    if pid == FUEL_LEVEL[2]:
        print(f"The fuel level is {data[0]*(100/255)} %")
    
    if pid == ENGINE_COOLANT_TEMP[2]:
        if data[0] & 0b00000001:
            print(f"The engine coolant temperature in sensor 1 is {data[1]-40} degrees celsius")
        
        if data[0] & 0b00000010:
            print(f"The engine coolant temperature in sensor 2 is {data[2]-40} degrees celsius")

    if pid == BATTERY_LEVEL[2]:
        print(f"The car battery level is {data[0]}")

    if pid == ENGINE_SPEED[2]:
        print(f"The engine is moving at {(data[0]*256 + data[1])/4} rpm")

bus = can.Bus(interface='socketcan', channel=channel, bitrate=bitrate)

messages = [
    VEHICLE_SPEED, 
    FUEL_LEVEL, 
    ENGINE_COOLANT_TEMP, 
    #BATTERY_LEVEL, 
    ENGINE_SPEED
]

try:
    notifier = can.Notifier(bus, msg_handler)

    while True:
        for msg in messages:
            bus.send(
                can.Message(
                    arbitration_id=0x7DF, 
                    data=msg, 
                    is_extended_id=False
                )
            )

        time.sleep(5)
            
except KeyboardInterrupt:
    notifier.stop()
    time.sleep(5)
    bus.shutdown()