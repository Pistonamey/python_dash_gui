import obd

def get_speed(connection):
    # global connection
    cmd = obd.commands.SPEED
    return connection.query(cmd).value.to("mph")

def get_rpm(connection):
    # global connection
    cmd = obd.commands.RPM
    return connection.query(cmd).value

def get_temperature(connection):
    # global connection
    cmd = obd.commands.OIL_TEMP
    return connection.query(cmd).value

def get_battery(connection):
    # global connection
    cmd = obd.commands.FUEL_LEVEL
    return connection.query(cmd).value

 
# connection = obd.OBD() # auto-connects to USB or RF port

# print(connection.status())

# obd.logger.setLevel(obd.logging.DEBUG)
