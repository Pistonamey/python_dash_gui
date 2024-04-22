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

    "RUN_TIME",               # PID 1F

    "PIDS_B"                  # PID 20

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

    pid_list3 = [

    "STATUS_DRIVE_CYCLE",          # PID 41

    "CONTROL_MODULE_VOLTAGE",      # PID 42

    "ABSOLUTE_LOAD",               # PID 43

    "COMMANDED_EQUIV_RATIO",       # PID 44

    "RELATIVE_THROTTLE_POS",       # PID 45

    "AMBIANT_AIR_TEMP",            # PID 46

    "THROTTLE_POS_B",              # PID 47

    "THROTTLE_POS_C",              # PID 48

    "ACCELERATOR_POS_D",           # PID 49

    "ACCELERATOR_POS_E",           # PID 4A

    "ACCELERATOR_POS_F",           # PID 4B

    "THROTTLE_ACTUATOR",           # PID 4C

    "RUN_TIME_MIL",                # PID 4D

    "TIME_SINCE_DTC_CLEARED",      # PID 4E

    "unsupported",                 # PID 4F

    "MAX_MAF",                     # PID 50

    "FUEL_TYPE",                   # PID 51

    "ETHANOL_PERCENT",             # PID 52

    "EVAP_VAPOR_PRESSURE_ABS",     # PID 53

    "EVAP_VAPOR_PRESSURE_ALT",     # PID 54

    "SHORT_O2_TRIM_B1",            # PID 55

    "LONG_O2_TRIM_B1",             # PID 56

    "SHORT_O2_TRIM_B2",            # PID 57

    "LONG_O2_TRIM_B2",             # PID 58

    "FUEL_RAIL_PRESSURE_ABS",      # PID 59

    "RELATIVE_ACCEL_POS",          # PID 5A

    "HYBRID_BATTERY_REMAINING",    # PID 5B

    "OIL_TEMP",                    # PID 5C

    "FUEL_INJECT_TIMING",          # PID 5D

    "FUEL_RATE",                   # PID 5E

    "unsupported"                  # PID 5F

    ]

    # Query for PIDs 01-20

    query_match_pids(connection, pid_list1, cmd1)

    # Query for PIDs 21-40

    query_match_pids(connection, pid_list2, cmd2)

    # Query for PIDs 41-60

    query_match_pids(connection, pid_list3, cmd3)



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

    "unsupported",      # PID 11

    "unsupported",      # PID 12

    "unsupported",      # PID 13

    "unsupported",      # PID 14

    "unsupported",      # PID 15

    "unsupported",      # PID 16

    "unsupported",      # PID 17

    "unsupported",      # PID 18

    "unsupported",      # PID 19

    "unsupported",      # PID 1A

    "unsupported",      # PID 1B

    "unsupported",      # PID 1C

    "unsupported",      # PID 1D

    "unsupported",      # PID 1E

    "unsupported",      # PID 1F

    "MIDS_B"             # PID 20 (Supported MIDs [21-40])

    ]

    mid_list2 = [

    "MONITOR_CATALYST_B1",  # PID 21

    "MONITOR_CATALYST_B2",  # PID 22

    "MONITOR_CATALYST_B3",  # PID 23

    "MONITOR_CATALYST_B4",  # PID 24

    "unsupported",          # PID 25

    "unsupported",          # PID 26

    "unsupported",          # PID 27

    "unsupported",          # PID 28

    "unsupported",          # PID 29

    "unsupported",          # PID 2A

    "unsupported",          # PID 2B

    "unsupported",          # PID 2C

    "unsupported",          # PID 2D

    "unsupported",          # PID 2E

    "unsupported",          # PID 2F

    "unsupported",          # PID 30

    "MONITOR_EGR_B1",       # PID 31

    "MONITOR_EGR_B2",       # PID 32

    "MONITOR_EGR_B3",       # PID 33

    "MONITOR_EGR_B4",       # PID 34

    "MONITOR_VVT_B1",       # PID 35

    "MONITOR_VVT_B2",       # PID 36

    "MONITOR_VVT_B3",       # PID 37

    "MONITOR_VVT_B4",       # PID 38

    "MONITOR_EVAP_150",     # PID 39

    "MONITOR_EVAP_090",     # PID 3A

    "MONITOR_EVAP_040",     # PID 3B

    "MONITOR_EVAP_020",     # PID 3C

    "MONITOR_PURGE_FLOW",   # PID 3D

    "unsupported",          # PID 3E

    "unsupported",          # PID 3F

    "MIDS_C"                # PID 40 (Supported MIDs [41-60])

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

    "unsupported",             # PID 51

    "unsupported",             # PID 52

    "unsupported",             # PID 53

    "unsupported",             # PID 54

    "unsupported",             # PID 55

    "unsupported",             # PID 56

    "unsupported",             # PID 57

    "unsupported",             # PID 58

    "unsupported",             # PID 59

    "unsupported",             # PID 5A

    "unsupported",             # PID 5B

    "unsupported",             # PID 5C

    "unsupported",             # PID 5D

    "unsupported",             # PID 5E

    "unsupported",             # PID 5F

    "MIDS_D"                    # PID 60 (Supported MIDs [61-80])

    ]

    mid_list4 = [

    "MONITOR_HEATED_CATALYST_B1",  # PID 61

    "MONITOR_HEATED_CATALYST_B2",  # PID 62

    "MONITOR_HEATED_CATALYST_B3",  # PID 63

    "MONITOR_HEATED_CATALYST_B4",  # PID 64

    "unsupported",                  # PID 65

    "unsupported",                  # PID 66

    "unsupported",                  # PID 67

    "unsupported",                  # PID 68

    "unsupported",                  # PID 69

    "unsupported",                  # PID 6A

    "unsupported",                  # PID 6B

    "unsupported",                  # PID 6C

    "unsupported",                  # PID 6D

    "unsupported",                  # PID 6E

    "unsupported",                  # PID 6F

    "MONITOR_SECONDARY_AIR_1",     # PID 71

    "MONITOR_SECONDARY_AIR_2",     # PID 72

    "MONITOR_SECONDARY_AIR_3",     # PID 73

    "MONITOR_SECONDARY_AIR_4",     # PID 74

    "unsupported",                  # PID 75

    "unsupported",                  # PID 76

    "unsupported",                  # PID 77

    "unsupported",                  # PID 78

    "unsupported",                  # PID 79

    "unsupported",                  # PID 7A

    "unsupported",                  # PID 7B

    "unsupported",                  # PID 7C

    "unsupported",                  # PID 7D

    "unsupported",                  # PID 7E

    "unsupported",                  # PID 7F

    "MIDS_E"                        # PID 80 (Supported MIDs [81-A0])

    ]  

    mid_list5 = [

    "MONITOR_FUEL_SYSTEM_B1",  # PID 81

    "MONITOR_FUEL_SYSTEM_B2",  # PID 82

    "MONITOR_FUEL_SYSTEM_B3",  # PID 83

    "MONITOR_FUEL_SYSTEM_B4",  # PID 84

    "MONITOR_BOOST_PRESSURE_B1",  # PID 85

    "MONITOR_BOOST_PRESSURE_B2",  # PID 86

    "unsupported",               # PID 87

    "unsupported",               # PID 88

    "unsupported",               # PID 89

    "MONITOR_NOX_ABSORBER_B1",  # PID 90

    "MONITOR_NOX_ABSORBER_B2",  # PID 91

    "unsupported",               # PID 92

    "unsupported",               # PID 93

    "unsupported",               # PID 94

    "unsupported",               # PID 95

    "unsupported",               # PID 96

    "unsupported",               # PID 97

    "MONITOR_NOX_CATALYST_B1",  # PID 98

    "MONITOR_NOX_CATALYST_B2",  # PID 99

    "unsupported",               # PID 9A

    "unsupported",               # PID 9B

    "unsupported",               # PID 9C

    "unsupported",               # PID 9D

    "unsupported",               # PID 9E

    "unsupported",               # PID 9F

    "unsupported",               # PID A0

    "MIDS_F"                     # Supported MIDs [A1-C0]

    ]

    mid_list6 = [

    "MONITOR_MISFIRE_GENERAL",          # PID A1

    "MONITOR_MISFIRE_CYLINDER_1",       # PID A2

    "MONITOR_MISFIRE_CYLINDER_2",       # PID A3

    "MONITOR_MISFIRE_CYLINDER_3",       # PID A4

    "MONITOR_MISFIRE_CYLINDER_4",       # PID A5

    "MONITOR_MISFIRE_CYLINDER_5",       # PID A6

    "MONITOR_MISFIRE_CYLINDER_6",       # PID A7

    "MONITOR_MISFIRE_CYLINDER_7",       # PID A8

    "MONITOR_MISFIRE_CYLINDER_8",       # PID A9

    "MONITOR_MISFIRE_CYLINDER_9",       # PID AA

    "MONITOR_MISFIRE_CYLINDER_10",      # PID AB

    "MONITOR_MISFIRE_CYLINDER_11",      # PID AC

    "MONITOR_MISFIRE_CYLINDER_12",      # PID AD

    "unsupported",                      # PID AE

    "unsupported",                      # PID AF

    "MONITOR_PM_FILTER_B1",              # PID B0

    "MONITOR_PM_FILTER_B2",              # PID B1

    "unsupported",                      # PID B2

    "unsupported",                      # PID B3

    "unsupported",                      # PID B4

    "unsupported",                      # PID B5

    "unsupported",                      # PID B6

    "unsupported",                      # PID B7

    "unsupported",                      # PID B8

    "unsupported",                      # PID B9

    "unsupported",                      # PID BA

    "unsupported",                      # PID BB

    "unsupported",                      # PID BC

    "unsupported",                      # PID BD

    "unsupported",                      # PID BE

    "MIDS_G"                            # PID C0 (Supported MIDs [C1-E0])

    ]



    query_match_pids(connection, mid_list1, cmd1)

    query_match_pids(connection, mid_list2, cmd2)

    query_match_pids(connection, mid_list3, cmd3)

    query_match_pids(connection, mid_list4, cmd4)

    query_match_pids(connection, mid_list5, cmd5)

    query_match_pids(connection, mid_list6, cmd6)





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





def get_intake_pressure(connection):

    cmd = obd.commands.INTAKE_PRESSURE

    try:

        return connection.query(cmd).value.magnitude

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving Intake Pressure: {str(e)}\n")

        return 44



def get_intake_temp(connection):

    cmd = obd.commands.INTAKE_TEMP

    try:

        return connection.query(cmd).value.magnitude

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving Intake Temp: {str(e)}\n")

        return 44

    

def get_runtime(connection):

    cmd = obd.commands.RUN_TIME

    try:

        return connection.query(cmd).value.magnitude

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving engine runtime: {str(e)}\n")

        return 44

    

def get_throttle_pos(connection):

    cmd = obd.commands.THROTTLE_POS

    try:

        return connection.query(cmd).value.magnitude

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving throttle position: {str(e)}\n")

        return 44

    

def get_absolute_load(connection):

    cmd = obd.commands.ABSOLUTE_LOAD

    try:

        return connection.query(cmd).value.magnitude

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving absolute load: {str(e)}\n")

        return 44

    

def get_fuel_type(connection):

    cmd = obd.commands.FUEL_TYPE

    try:

        return str(connection.query(cmd).value)

    except Exception as e:

        with open('output.txt', 'a') as output:

            output.write(f"Error receiving absolute load: {str(e)}\n")

        return "Gasoline" 
