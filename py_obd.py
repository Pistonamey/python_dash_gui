import obd

# Each of these getter functions need to return an integer and/or a float number

def query_match_pids(connection, pidlist, command):
    try:
        response = connection.query(command).value
        with open('output.txt', 'a') as f:
            f.write("Length of bit response: " + str(len(response)) + "\n")
            f.write("Length of pid list: " + str(len(pidlist)) + "\n")
            bit_string = ''.join(['1' if bit else '0' for bit in response])
            f.write("Supported MIDs: " + bit_string + "\n")
            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    pid_index = index + 1  # To get the correct PID number
                    if pid_index <= len(pidlist):
                        pid_name = pidlist[pid_index - 1]
                        f.write(f"  PID {pid_index:02X} ({pid_name}) is supported\n")
        return bit_string
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported available PIDs: {str(e)}\n")
        return 1

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
    query_match_pids(connection, cmd1, pid_list1)
    # Query for PIDs 21-40
    query_match_pids(connection, cmd2, pid_list2)
    # Query for PIDs 41-60
    query_match_pids(connection, cmd3, pid_list3)

def get_supported_pids_mode06(connection):
    cmd1 = obd.commands.MIDS_A
    cmd2 = obd.commands.MIDS_B
    cmd3 = obd.commands.MIDS_C
    cmd4 = obd.commands.MIDS_D
    cmd5 = obd.commands.MIDS_E
    cmd6 = obd.commands.MIDS_F
    mid_list1 = [
    "MONITOR_O2_B1S1",  # PID 01
    "MONITOR_O2_B1S2",  # PID 02
    "MONITOR_O2_B1S3",  # PID 03
    "MONITOR_O2_B1S4",  # PID 04
    "MONITOR_O2_B2S1",  # PID 05
    "MONITOR_O2_B2S2",  # PID 06
    "MONITOR_O2_B2S3",  # PID 07
    "MONITOR_O2_B2S4",  # PID 08
    "MONITOR_O2_B3S1",  # PID 09
    "MONITOR_O2_B3S2",  # PID 0A
    "MONITOR_O2_B3S3",  # PID 0B
    "MONITOR_O2_B3S4",  # PID 0C
    "MONITOR_O2_B4S1",  # PID 0D
    "MONITOR_O2_B4S2",  # PID 0E
    "MONITOR_O2_B4S3",  # PID 0F
    "MONITOR_O2_B4S4",  # PID 10
    "MIDS_B"            # PID 20 (Supported MIDs [21-40])
    ]
    mid_list2 = [
    "MONITOR_CATALYST_B1",   # PID 21
    "MONITOR_CATALYST_B2",   # PID 22
    "MONITOR_CATALYST_B3",   # PID 23
    "MONITOR_CATALYST_B4",   # PID 24
    "MONITOR_EGR_B1",        # PID 31
    "MONITOR_EGR_B2",        # PID 32
    "MONITOR_EGR_B3",        # PID 33
    "MONITOR_EGR_B4",        # PID 34
    "MONITOR_VVT_B1",        # PID 35
    "MONITOR_VVT_B2",        # PID 36
    "MONITOR_VVT_B3",        # PID 37
    "MONITOR_VVT_B4",        # PID 38
    "MONITOR_EVAP_150",      # PID 39 (EVAP Monitor (Cap Off / 0.150"))
    "MONITOR_EVAP_090",      # PID 3A (EVAP Monitor (0.090"))
    "MONITOR_EVAP_040",      # PID 3B (EVAP Monitor (0.040"))
    "MONITOR_EVAP_020",      # PID 3C (EVAP Monitor (0.020"))
    "MONITOR_PURGE_FLOW",    # PID 3D
    "MIDS_C"                 # PID 40 (Supported MIDs [41-60])
    ]
    mid_list3 = [
    "MONITOR_O2_HEATER_B1S1",  # PID 41
    "MONITOR_O2_HEATER_B1S2",  # PID 42
    "MONITOR_O2_HEATER_B1S3",  # PID 43
    "MONITOR_O2_HEATER_B1S4",  # PID 44
    "MONITOR_O2_HEATER_B2S1",  # PID 45
    "MONITOR_O2_HEATER_B2S2",  # PID 46
    "MONITOR_O2_HEATER_B2S3",  # PID 47
    "MONITOR_O2_HEATER_B2S4",  # PID 48
    "MONITOR_O2_HEATER_B3S1",  # PID 49
    "MONITOR_O2_HEATER_B3S2",  # PID 4A
    "MONITOR_O2_HEATER_B3S3",  # PID 4B
    "MONITOR_O2_HEATER_B3S4",  # PID 4C
    "MONITOR_O2_HEATER_B4S1",  # PID 4D
    "MONITOR_O2_HEATER_B4S2",  # PID 4E
    "MONITOR_O2_HEATER_B4S3",  # PID 4F
    "MONITOR_O2_HEATER_B4S4",  # PID 50
    "MIDS_D"                   # PID 60 (Supported MIDs [61-80])
    ]
    mid_list4 = [
    "MONITOR_HEATED_CATALYST_B1",  # PID 61
    "MONITOR_HEATED_CATALYST_B2",  # PID 62
    "MONITOR_HEATED_CATALYST_B3",  # PID 63
    "MONITOR_HEATED_CATALYST_B4",  # PID 64
    "MONITOR_SECONDARY_AIR_1",     # PID 71
    "MONITOR_SECONDARY_AIR_2",     # PID 72
    "MONITOR_SECONDARY_AIR_3",     # PID 73
    "MONITOR_SECONDARY_AIR_4",     # PID 74
    "MIDS_E"                       # PID 80 (Supported MIDs [81-A0])
    ]
    mid_list5 = [
    "MONITOR_FUEL_SYSTEM_B1",       # PID 81
    "MONITOR_FUEL_SYSTEM_B2",       # PID 82
    "MONITOR_FUEL_SYSTEM_B3",       # PID 83
    "MONITOR_FUEL_SYSTEM_B4",       # PID 84
    "MONITOR_BOOST_PRESSURE_B1",    # PID 85
    "MONITOR_BOOST_PRESSURE_B2",    # PID 86
    "MONITOR_NOX_ABSORBER_B1",      # PID 90
    "MONITOR_NOX_ABSORBER_B2",      # PID 91
    "MONITOR_NOX_CATALYST_B1",      # PID 98
    "MONITOR_NOX_CATALYST_B2",      # PID 99
    "MIDS_F"                        # PID A0 (Supported MIDs [A1-C0])
    ]
    mid_list6 = [
    "MONITOR_MISFIRE_GENERAL",       # PID A1
    "MONITOR_MISFIRE_CYLINDER_1",    # PID A2
    "MONITOR_MISFIRE_CYLINDER_2",    # PID A3
    "MONITOR_MISFIRE_CYLINDER_3",    # PID A4
    "MONITOR_MISFIRE_CYLINDER_4",    # PID A5
    "MONITOR_MISFIRE_CYLINDER_5",    # PID A6
    "MONITOR_MISFIRE_CYLINDER_6",    # PID A7
    "MONITOR_MISFIRE_CYLINDER_7",    # PID A8
    "MONITOR_MISFIRE_CYLINDER_8",    # PID A9
    "MONITOR_MISFIRE_CYLINDER_9",    # PID AA
    "MONITOR_MISFIRE_CYLINDER_10",   # PID AB
    "MONITOR_MISFIRE_CYLINDER_11",   # PID AC
    "MONITOR_MISFIRE_CYLINDER_12",   # PID AD
    "MONITOR_PM_FILTER_B1",          # PID B0
    "MONITOR_PM_FILTER_B2"           # PID B1
    ]

    query_match_pids(connection, cmd1, mid_list1)
    query_match_pids(connection, cmd2, mid_list2)
    query_match_pids(connection, cmd3, mid_list3)
    query_match_pids(connection, cmd4, mid_list4)
    query_match_pids(connection, cmd5, mid_list5)
    query_match_pids(connection, cmd6, mid_list6)


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
