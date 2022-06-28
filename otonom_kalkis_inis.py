from tokenize import String
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from aerodrone import drone
from pynput import keyboard
import time
import math

connection_string="127.0.0.1:14550"

vehicle = connect(connection_string,wait_ready=True,timeout=100)
myDrone = drone(vehicle)

myDrone.arm_and_takeoff(1)

countdown = 3
print('Waiting for ', countdown, ' secs..')

for i in range(countdown):
    print('Countdown: ', countdown - i)
    time.sleep(1)

myDrone.immadiateLanding()