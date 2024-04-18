import obd

def get_speed(connection):
    cmd = obd.commands.SPEED
    return connection.query(cmd)

def get_rpm():
    cmd = obd.commands.RPM
    return float(connection.query(cmd).value.to("mph"))

def get_temperature():
    cmd = obd.commands.OIL_TEMP
    return float(connection.query(cmd).value)

def get_battery():
    cmd = obd.commands.FUEL_LEVEL
    return float(connection.query(cmd).value)

connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.SPEED # select an OBD command (sensor)

print(connection.status())

obd.logger.setLevel(obd.logging.DEBUG)
