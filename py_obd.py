import obd


def get_speed(connection):
    # global connection
    cmd = obd.commands.SPEED
    return connection.query(cmd).value.to("mph").magnitude


def get_rpm(connection):
    # global connection
    cmd = obd.commands.RPM
    return connection.query(cmd).value.magnitude


def get_temperature(connection):
    # global connection
    cmd = obd.commands.COOLANT_TEMP
    return connection.query(cmd).value.magnitude


def get_battery(connection):
    # global connection
    cmd = obd.commands.FUEL_LEVEL
    try:
        return connection.query(cmd).value.magnitude
    except Exception as e:
        return 1234


def get_tire_pressure(connection):
    # global connection

    # Make this a try except statement:
    # Try making the obd calls, if it does not exist or returns an error, hardcode the value into
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
        tire_pressure = [44, 44, 44, 44]
        return tire_pressure


def get_afr_ratio(connection):
    # air - fuel ratio

    cmd = obd.command.MAF

    try:
        afr_ratio = connection.query(cmd).value.magnitude
        return afr_ratio
    except Exception as e:
        afr_ratio = 9090
        return afr_ratio

    try:
        coolant_temp = connection.query(cmd).value.magnitude
        return coolant_temp
    except Exception as e:
        coolant_temp = 1234
        return coolant_temp


def get_barometric_pressure(connection):
    cmd = obd.commands.BAROMETRIC_PRESSURE 
    try:
        barometric_pressure = connection.query(cmd).value.magnitude
        return barometric_pressure
    except Exception as e:
        barometric_pressure = 1234
        return barometric_pressure
