from re import S
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from time import sleep
import math
import sys
from ucus_komutlari import aero

connection_string="127.0.0.1:14550"
# connection_string="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
vehicle = connect(connection_string,wait_ready=True,timeout=100)

drone = aero(vehicle)

drone.video()