from dronekit import connect
import socket
import exceptions

vehicle = connect('', wait_ready=True)
print("Mode: " + vehicle.mode.name)