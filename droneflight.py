from dronekit import connect
# Connect to UDP endpoint.
vehicle = connect('COM4', baud=57600, wait_ready=True)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print("Mode: " + vehicle.mode.name)