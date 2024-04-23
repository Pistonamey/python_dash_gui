import obd

# Each of these getter functions needs to return an integer and/or a float number

def query_match_pids(connection, pidlist, command):
    try:
        response = connection.query(command).value
        with open('output.txt', 'a') as f:
            f.write(f"Length of bit response: {len(response)}\n")
            f.write(f"Length of PID list: {len(pidlist)}\n")

            bit_string = ''.join(['1' if bit else '0' for bit in response])
            f.write(f"Supported MIDs: {bit_string}\n")

            # Optionally, list the supported PIDs
            for index, bit in enumerate(response):
                if bit:
                    pid_index = index + 1  # PID number is 1-based
                    if pid_index <= len(pidlist):
                        pid_name = pidlist[pid_index - 1]
                        f.write(f"  PID {pid_index:02X} ({pid_name}) is supported\n")

        return bit_string
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving supported PIDs: {e}\n")
        return 1

# Common function to query an OBD command and return a default value in case of an error
def query_obd(connection, command, default_value, error_message):
    try:
        return connection.query(command).value.magnitude
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"{error_message}: {str(e)}\n")
        return default_value

def get_supported_pids_mode01(connection):
    cmd1 = obd.commands.PIDS_A
    cmd2 = obd.commands.PIDS_B
    cmd3 = obd.commands.PIDS_C

    pid_list1 = [
        "STATUS", "FREEZE_DTC", "FUEL_STATUS", "ENGINE_LOAD", "COOLANT_TEMP", 
        "SHORT_FUEL_TRIM_1", "LONG_FUEL_TRIM_1", "SHORT_FUEL_TRIM_2", "LONG_FUEL_TRIM_2", 
        "FUEL_PRESSURE", "INTAKE_PRESSURE", "RPM", "SPEED", "TIMING_ADVANCE", 
        "INTAKE_TEMP", "MAF", "THROTTLE_POS", "AIR_STATUS", "O2_SENSORS", "O2_B1S1",
        "O2_B1S2", "O2_B1S3", "O2_B1S4", "O2_B2S1", "O2_B2S2", "O2_B2S3", "O2_B2S4", 
        "OBD_COMPLIANCE", "O2_SENSORS_ALT", "AUX_INPUT_STATUS", "RUN_TIME", "PIDS_B"
    ]

    pid_list2 = [
        "DISTANCE_W_MIL", "FUEL_RAIL_PRESSURE_VAC", "FUEL_RAIL_PRESSURE_DIRECT",
        "O2_S1_WR_VOLTAGE", "O2_S2_WR_VOLTAGE", "O2_S3_WR_VOLTAGE", "O2_S4_WR_VOLTAGE",
        "O2_S5_WR_VOLTAGE", "O2_S6_WR_VOLTAGE", "O2_S7_WR_VOLTAGE", "O2_S8_WR_VOLTAGE",
        "COMMANDED_EGR", "EGR_ERROR", "EVAPORATIVE_PURGE", "FUEL_LEVEL", "WARMUPS_SINCE_DTC_CLEAR",
        "DISTANCE_SINCE_DTC_CLEAR", "EVAP_VAPOR_PRESSURE", "BAROMETRIC_PRESSURE", 
        "O2_S1_WR_CURRENT", "O2_S2_WR_CURRENT", "O2_S3_WR_CURRENT", "O2_S4_WR_CURRENT",
        "O2_S5_WR_CURRENT", "O2_S6_WR_CURRENT", "O2_S7_WR_CURRENT", "O2_S8_WR_CURRENT",
        "CATALYST_TEMP_B1S1", "CATALYST_TEMP_B2S1", "CATALYST_TEMP_B1S2", "CATALYST_TEMP_B2S2",
        "PIDS_C"
    ]

    pid_list3 = [
        "STATUS_DRIVE_CYCLE", "CONTROL_MODULE_VOLTAGE", "ABSOLUTE_LOAD", "COMMANDED_EQUIV_RATIO",
        "RELATIVE_THROTTLE_POS", "AMBIENT_AIR_TEMP", "THROTTLE_POS_B", "THROTTLE_POS_C",
        "ACCELERATOR_POS_D", "ACCELERATOR_POS_E", "ACCELERATOR_POS_F", "THROTTLE_ACTUATOR",
        "RUN_TIME_MIL", "TIME_SINCE_DTC_CLEARED", "unsupported", "MAX_MAF", "FUEL_TYPE",
        "ETHANOL_PERCENT", "EVAP_VAPOR_PRESSURE_ABS", "EVAP_VAPOR_PRESSURE_ALT", 
        "SHORT_O2_TRIM_B1", "LONG_O2_TRIM_B1", "SHORT_O2_TRIM_B2", "LONG_O2_TRIM_B2",
        "FUEL_RAIL_PRESSURE_ABS", "RELATIVE_ACCEL_POS", "HYBRID_BATTERY_REMAINING", 
        "OIL_TEMP", "FUEL_INJECT_TIMING", "FUEL_RATE"
    ]

    # Query for PIDs 01-20
    query_match_pids(connection, pid_list1, cmd1)

    # Query for PIDs 21-40
    query_match_pids(connection, pid_list2, cmd2)

    # Query for PIDs 41-60
    query_match_pids(connection, pid_list3, cmd3)

# Function to query MIDs
def query_match_pids(connection, mid_list, cmd):
    # Insert your logic for querying pids based on the mid_list and command
    pass

# Main function to query supported PIDs in Mode 06
def get_supported_pids_mode06(connection):
    # Define a dictionary with OBD commands and corresponding MID lists
    commands_and_mids = {
        "MIDS_A": {
            "cmd": obd.commands.MIDS_A,
            "mids": [
                "MONITOR_O2_B1S1", "MONITOR_O2_B1S2", "MONITOR_O2_B1S3", "MONITOR_O2_B1S4",
                "MONITOR_O2_B2S1", "MONITOR_O2_B2S2", "MONITOR_O2_B2S3", "MONITOR_O2_B2S4",
                "MONITOR_O2_B3S1", "MONITOR_O2_B3S2", "MONITOR_O2_B3S3", "MONITOR_O2_B3S4",
                "MONITOR_O2_B4S1", "MONITOR_O2_B4S2", "MONITOR_O2_B4S3", "MONITOR_O2_B4S4",
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "MIDS_B"  # Supported MIDs [21-40]
            ],
        },
        "MIDS_B": {
            "cmd": obd.commands.MIDS_B,
            "mids": [
                "MONITOR_CATALYST_B1", "MONITOR_CATALYST_B2", "MONITOR_CATALYST_B3", 
                "MONITOR_CATALYST_B4", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "MONITOR_EGR_B1", "MONITOR_EGR_B2", "MONITOR_EGR_B3", "MONITOR_EGR_B4", 
                "MONITOR_VVT_B1", "MONITOR_VVT_B2", "MONITOR_VVT_B3", "MONITOR_VVT_B4", 
                "MONITOR_EVAP_150", "MONITOR_EVAP_090", "MONITOR_EVAP_040", 
                "MONITOR_EVAP_020", "MONITOR_PURGE_FLOW", "unsupported", 
                "unsupported", "MIDS_C"  # Supported MIDs [41-60]
            ],
        },
        "MIDS_C": {
            "cmd": obd.commands.MIDS_C,
            "mids": [
                "MONITOR_O2_HEATER_B1S1", "MONITOR_O2_HEATER_B1S2", "MONITOR_O2_HEATER_B1S3", 
                "MONITOR_O2_HEATER_B1S4", "MONITOR_O2_HEATER_B2S1", "MONITOR_O2_HEATER_B2S2", 
                "MONITOR_O2_HEATER_B2S3", "MONITOR_O2_HEATER_B2S4", "MONITOR_O2_HEATER_B3S1", 
                "MONITOR_O2_HEATER_B3S2", "MONITOR_O2_HEATER_B3S3", "MONITOR_O2_HEATER_B3S4", 
                "MONITOR_O2_HEATER_B4S1", "MONITOR_O2_HEATER_B4S2", "MONITOR_O2_HEATER_B4S3", 
                "MONITOR_O2_HEATER_B4S4", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "MIDS_D"  # Supported MIDs [61-80]
            ],
        },
        "MIDS_D": {
            "cmd": obd.commands.MIDS_D,
            "mids": [
                "MONITOR_HEATED_CATALYST_B1", "MONITOR_HEATED_CATALYST_B2", 
                "MONITOR_HEATED_CATALYST_B3", "MONITOR_HEATED_CATALYST_B4", 
                "MONITOR_SECONDARY_AIR_1", "MONITOR_SECONDARY_AIR_2", "MONITOR_SECONDARY_AIR_3", 
                "MONITOR_SECONDARY_AIR_4", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "unsupported", "unsupported", "unsupported", "unsupported", 
                "MIDS_E"  # Supported MIDs [81-A0]
            ],
        },
        "MIDS_E": {
            "cmd": obd.commands.MIDS_E,
            "mids": [
                "MONITOR_FUEL_SYSTEM_B1", "MONITOR_FUEL_SYSTEM_B2", 
                "MONITOR_FUEL_SYSTEM_B3", "MONITOR_FUEL_SYSTEM_B4", 
                "MONITOR_BOOST_PRESSURE_B1", "MONITOR_BOOST_PRESSURE_B2", 
                "unsupported", "unsupported", "unsupported", 
                "MONITOR_NOX_ABSORBER_B1", "MONITOR_NOX_ABSORBER_B2", 
                "unsupported", "unsupported", "unsupported", 
                "MONITOR_NOX_CATALYST_B1", "MONITOR_NOX_CATALYST_B2", 
                "unsupported", "unsupported", "unsupported", 
                "MIDS_F"  # Supported MIDs [A1-C0]
            ],
        },
        "MIDS_F": {
            "cmd": obd.commands.MIDS_F,
            "mids": [
                "MONITOR_MISFIRE_GENERAL", "MONITOR_MISFIRE_CYLINDER_1", 
                "MONITOR_MISFIRE_CYLINDER_2", "MONITOR_MISFIRE_CYLINDER_3", 
                "MONITOR_MISFIRE_CYLINDER_4", "MONITOR_MISFIRE_CYLINDER_5", 
                "MONITOR_MISFIRE_CYLINDER_6", "MONITOR_MISFIRE_CYLINDER_7", 
                "MONITOR_MISFIRE_CYLINDER_8", "MONITOR_MISFIRE_CYLINDER_9", 
                "MONITOR_MISFIRE_CYLINDER_10", "MONITOR_MISFIRE_CYLINDER_11", 
                "MONITOR_MISFIRE_CYLINDER_12", "unsupported", 
                "unsupported", "MONITOR_PM_FILTER_B1", 
                "MONITOR_PM_FILTER_B2", "unsupported", 
                "unsupported", "unsupported", 
                "unsupported", "unsupported", 
                "unsupported", "unsupported", 
                "unsupported", "unsupported", 
                "unsupported", "unsupported", 
                "unsupported", "unsupported", 
                "MIDS_G"  # Supported MIDs [C1-E0]
            ],
        },
    }
    for key, value in commands_and_mids.items():
        query_match_pids(connection, value["mids"], value["cmd"])


# Individual functions to query specific OBD commands
def get_speed(connection):
    return query_obd(connection,obd.commands.SPEED, 44, "Error receiving speed")  # Returning speed in mph

def get_rpm(connection):
    return query_obd(connection,obd.commands.RPM, 4.444, "Error receiving RPM")  # RPM in thousands

def get_temperature(connection):
    return query_obd(connection,obd.commands.COOLANT_TEMP, 44, "Error receiving coolant temperature")

def get_battery(connection):
    return round(query_obd(connection,obd.commands.FUEL_LEVEL, 44, "Error receiving fuel levels"))

def get_intake_pressure(connection):
    return query_obd(connection,obd.commands.INTAKE_PRESSURE, 44, "Error receiving intake pressure")

def get_intake_temp(connection):
    return query_obd(connection,obd.commands.INTAKE_TEMP, 44, "Error receiving intake temperature")

def get_runtime(connection):
    return query_obd(connection,obd.commands.RUN_TIME, 44, "Error receiving engine runtime")

def get_throttle_pos(connection):
    return query_obd(connection,obd.commands.THROTTLE_POS, 44, "Error receiving throttle position")

def get_absolute_load(connection):
    return query_obd(connection,obd.commands.ABSOLUTE_LOAD, 44, "Error receiving absolute load")
    
def get_engine_load(connection):
    return query_obd(connection,obd.commands.ENGINE_LOAD, 44, "Error receiving absolute load")

def get_fuel_type(connection):
    try:
        return str(connection.query(obd.commands.FUEL_TYPE).value)
    except Exception as e:
        with open('output.txt', 'a') as output:
            output.write(f"Error receiving fuel type: {str(e)}\n")
        return "Gasoline"  # Default to gasoline
