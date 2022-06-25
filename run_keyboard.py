from dis import dis
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from aerodrone import drone
from multiprocessing.connection import Listener
from pynput import keyboard
from input import keyboard_events
import time
import os
import sys

connection_string="127.0.0.1:14550"

vehicle = connect(connection_string,wait_ready=True,timeout=100)
myDrone = drone(vehicle)
key_events = keyboard_events(myDrone)

myDrone.arm_and_takeoff(5)
listener = keyboard.Listener(on_press=key_events.on_press, on_release=key_events.on_release)
listener.start()  # start to listen on a separate thread
print('ready to go!')
# myDrone.go_to(10, 10, -20, 0)
while True:
    if vehicle.location.global_relative_frame.alt <= 3:
        vehicle.mode = VehicleMode("LAND")
        keyboard.press(keyboard.Key.esc)
        break
    time.sleep(1)
listener.join()  # remove if main thread is polling self.keys