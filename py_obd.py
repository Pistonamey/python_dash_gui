import obd

# Each of these getter functions need to return an integer and/or a float number
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
