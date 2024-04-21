import obd

# Each of these getter functions need to return an integer and/or a float number

def get_supported_pids_mode01(connection):
    cmd1 = obd.commands.PIDS_A
    cmd2 = obd.commands.PIDS_B
    cmd3 = obd.commands.PIDS_C
    pid_list1 = [ # PID List 01-20
    "STATUS",                 # PID 01
    "FREEZE_DTC",             # PID 02
    "FUEL_STATUS",            # PID 03
    "ENGINE_LOAD",            # PID 04
    "COOLANT_TEMP",           # PID 05
    "SHORT_FUEL_TRIM_1",      # PID 06
    "LONG_FUEL_TRIM_1",       # PID 07
    "SHORT_FUEL_TRIM_2",      # PID 08
    "LONG_FUEL_TRIM_2",       # PID 09
    "FUEL_PRESSURE",          # PID 0A
    "INTAKE_PRESSURE",        # PID 0B
    "RPM",                    # PID 0C
    "SPEED",                  # PID 0D
    "TIMING_ADVANCE",         # PID 0E
    "INTAKE_TEMP",            # PID 0F
    "MAF",                    # PID 10
    "THROTTLE_POS",           # PID 11
    "AIR_STATUS",             # PID 12
    "O2_SENSORS",             # PID 13
    "O2_B1S1",                # PID 14
    "O2_B1S2",                # PID 15
    "O2_B1S3",                # PID 16
    "O2_B1S4",                # PID 17
    "O2_B2S1",                # PID 18
    "O2_B2S2",                # PID 19
    "O2_B2S3",                # PID 1A
    "O2_B2S4",                # PID 1B
    "OBD_COMPLIANCE",         # PID 1C
    "O2_SENSORS_ALT",         # PID 1D
    "AUX_INPUT_STATUS",       # PID 1E
    "RUN_TIME"                # PID 1F
]
    pid_list2 = [ # PID List 21-40
    "DISTANCE_W_MIL",                 # PID 21
    "FUEL_RAIL_PRESSURE_VAC",         # PID 22
    "FUEL_RAIL_PRESSURE_DIRECT",      # PID 23
    "O2_S1_WR_VOLTAGE",               # PID 24
    "O2_S2_WR_VOLTAGE",               # PID 25
    "O2_S3_WR_VOLTAGE",               # PID 26
    "O2_S4_WR_VOLTAGE",               # PID 27
    "O2_S5_WR_VOLTAGE",               # PID 28
    "O2_S6_WR_VOLTAGE",               # PID 29
    "O2_S7_WR_VOLTAGE",               # PID 2A
    "O2_S8_WR_VOLTAGE",               # PID 2B
    "COMMANDED_EGR",                  # PID 2C
    "EGR_ERROR",                      # PID 2D
    "EVAPORATIVE_PURGE",              # PID 2E
    "FUEL_LEVEL",                     # PID 2F
    "WARMUPS_SINCE_DTC_CLEAR",        # PID 30
    "DISTANCE_SINCE_DTC_CLEAR",       # PID 31
    "EVAP_VAPOR_PRESSURE",            # PID 32
    "BAROMETRIC_PRESSURE",            # PID 33
    "O2_S1_WR_CURRENT",               # PID 34
    "O2_S2_WR_CURRENT",               # PID 35
    "O2_S3_WR_CURRENT",               # PID 36
    "O2_S4_WR_CURRENT",               # PID 37
    "O2_S5_WR_CURRENT",               # PID 38
    "O2_S6_WR_CURRENT",               # PID 39
    "O2_S7_WR_CURRENT",               # PID 3A
    "O2_S8_WR_CURRENT",               # PID 3B
    "CATALYST_TEMP_B1S1",             # PID 3C
    "CATALYST_TEMP_B2S1",             # PID 3D
    "CATALYST_TEMP_B1S2",             # PID 3E
    "CATALYST_TEMP_B2S2",             # PID 3F
    "PIDS_C",                         # PID 40 (Supported PIDs [41-60])
]
    pid_list3 = [ # PID List 41-60
    "STATUS_DRIVE_CYCLE",               # PID 41
    "CONTROL_MODULE_VOLTAGE",           # PID 42
    "ABSOLUTE_LOAD",                    # PID 43
    "COMMANDED_EQUIV_RATIO",            # PID 44
    "RELATIVE_THROTTLE_POS",            # PID 45
    "AMBIANT_AIR_TEMP",                 # PID 46
    "THROTTLE_POS_B",                   # PID 47
    "THROTTLE_POS_C",                   # PID 48
    "ACCELERATOR_POS_D",                # PID 49
    "ACCELERATOR_POS_E",                # PID 4A
    "ACCELERATOR_POS_F",                # PID 4B
    "THROTTLE_ACTUATOR",                # PID 4C
    "RUN_TIME_MIL",                     # PID 4D
    "TIME_SINCE_DTC_CLEARED",           # PID 4E
    "unsupported",                      # PID 4F (Unsupported PID)
    "MAX_MAF",                          # PID 50
    "FUEL_TYPE",                        # PID 51
    "ETHANOL_PERCENT",                  # PID 52
    "EVAP_VAPOR_PRESSURE_ABS",          # PID 53
    "EVAP_VAPOR_PRESSURE_ALT",          # PID 54
    "SHORT_O2_TRIM_B1",                 # PID 55
    "LONG_O2_TRIM_B1",                  # PID 56
    "SHORT_O2_TRIM_B2",                 # PID 57
    "LONG_O2_TRIM_B2",                  # PID 58
    "FUEL_RAIL_PRESSURE_ABS",           # PID 59
    "RELATIVE_ACCEL_POS",               # PID 5A
    "HYBRID_BATTERY_REMAINING",         # PID 5B
    "OIL_TEMP",                         # PID 5C
    "FUEL_INJECT_TIMING",               # PID 5D
    "FUEL_RATE"                         # PID 5E
]
    # Query for PIDs 01-20
    try:
        response = connection.query(cmd1).value
        bit_string = ''.join(['1' if bit else '0' for bit in response])
        with open('output.txt', 'a') as f:
            f.write("Supported PIDs: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    pid_index = index + 1  # To get the correct PID number
                    if pid_index <= len(pid_list1):
                        pid_name = pid_list1[pid_index - 1]
                        f.write(f"  PID {pid_index:02X} ({pid_name}) is supported\n")
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs for PIDs 01-20: {str(e)}\n")

    # Query for PIDs 21-40
    try:
        response = connection.query(cmd2).value
        bit_string = ''.join(['1' if bit else '0' for bit in response])
        with open('output.txt', 'a') as f:
            f.write("Supported PIDs: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    pid_index = index + 1  # To get the correct PID number
                    if pid_index <= len(pid_list2):
                        pid_name = pid_list2[pid_index - 1]
                        f.write(f"  PID {pid_index:02X} ({pid_name}) is supported\n")
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs for PIDs 21-40: {str(e)}\n")

    # Query for PIDs 41-60
    try:
        response = connection.query(cmd3).value
        bit_string = ''.join(['1' if bit else '0' for bit in response])
        with open('output.txt', 'a') as f:
            f.write("Supported PIDs: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    pid_index = index + 1  # To get the correct PID number
                    if pid_index <= len(pid_list3):
                        pid_name = pid_list3[pid_index - 1]
                        f.write(f"  PID {pid_index:02X} ({pid_name}) is supported\n")
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs for PIDs 41-60: {str(e)}\n")
    
    
def get_supported_pids_mode06(connection):
    cmd = obd.commands.MIDS_A
    try:
        response = connection.query(cmd).value
        bit_string = ''.join(['1' if bit else '0' for bit in response])
        with open('output.txt', 'a') as f:
            f.write("Supported MIDs: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    f.write(f"  PID {index + 1} is supported\n")
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs: {str(e)}\n")
        return 1
    
def get_supported_pids_mode09(connection):
    cmd = obd.commands.PIDS_9A
    try:
        response = connection.query(cmd).value
        bit_string = ''.join(['1' if bit else '0' for bit in response])
        with open('output.txt', 'a') as f:
            f.write("Supported PIDS_9A: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    f.write(f"  PID {index + 1} is supported\n")
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs: {str(e)}\n")
        return 1

def get_speed(connection):
    # global connection
    cmd = obd.commands.SPEED
    try:
        return connection.query(cmd).value.to("mph").magnitude
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving speed: {str(e)}\n")
        return 44

def get_rpm(connection):
    # global connection
    cmd = obd.commands.RPM
    try:
        return (connection.query(cmd).value.magnitude) / 1000
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving RPM: {str(e)}\n")
        return 4444/1000

def get_temperature(connection):
    # global connection
    cmd = obd.commands.COOLANT_TEMP
    try:
        return connection.query(cmd).value.magnitude
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving Coolant Temperature: {str(e)}\n")
        return 44

def get_battery(connection):
    # global connection
    cmd = obd.commands.FUEL_LEVEL
    try:
        return round(connection.query(cmd).value.magnitude)
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving Fuel Levels: {str(e)}\n")
        return 44


def get_tire_pressure(connection):
    # global connection
    cmd1 = obd.commands.MONITOR_SECONDARY_AIR_1
    cmd2 = obd.commands.MONITOR_SECONDARY_AIR_2
    cmd3 = obd.commands.MONITOR_SECONDARY_AIR_3
    cmd4 = obd.commands.MONITOR_SECONDARY_AIR_4
    tire_pressure = []
    try:
        tire_pressure[0] = connection.query(cmd1).value.magnitude
        tire_pressure[1] = connection.query(cmd2).value.magnitude
        tire_pressure[2] = connection.query(cmd3).value.magnitude
        tire_pressure[3] = connection.query(cmd4).value.magnitude
        return tire_pressure
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving Tire Pressures: {str(e)}\n")
        tire_pressure = [44, 44, 44, 44]
        return tire_pressure


def get_afr_ratio(connection):
    # air - fuel ratio
    cmd = obd.command.MAF

    try:
        return connection.query(cmd).value.magnitude
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving AFR Ratios: {str(e)}\n")
        return 4444


def get_barometric_pressure(connection):
    cmd = obd.commands.BAROMETRIC_PRESSURE 
    try:
        return connection.query(cmd).value.magnitude
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving Barometric Pressures: {str(e)}\n")
        barometric_pressure = 1234
        return barometric_pressure
