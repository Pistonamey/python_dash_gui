#!/usr/bin/env python3 
import can
import os

# CAN Bus configuration parameters here!
channel = 'vcan0'
bitrate = 500000

# import GUI

# GUI = MyGUI()

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
    exit()

# Each device that we want to display data for is included in this table.
devices = [
    # instead of a scale maybe we could have a convert function?
    # That converts the raw CAN data into the format we want. 
    # Sometimes, you might not need a linear transformation of the data. 
    #This is where this comes in handy!
    #{name, id, variable_name, scale, offset},
    #{name, id, variable_name, convert_fn}
]

bus = can.Bus(interface='socketcan', channel=channel, bitrate=bitrate)
bus.send(
    can.Message(
        arbitration_id=0x1EF, 
        data=[0, 0x69, 0x42, 10, 12, 31, 0x45, 0x11], 
        is_extended_id=False
    )
)

try:
    #gui.start()
    while True:
        print("> ", end="")
        print(bus.recv())
            
except KeyboardInterrupt:
    bus.shutdown()