from dronekit import connect, VehicleMode
from pymavlink import mavutil
from time import sleep
import math
import time
from aeronist import drone


class aero:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.myDrone = drone(self.vehicle)

    def acil_inis(self):
        self.myDrone.immadiateLanding()

    def test(self):
        # self.myDrone.arm_only()
        self.myDrone.havadaTurlama()
        print('success!')

    def video(self):
        self.myDrone.arm_and_takeoff(5)
        location = self.vehicle.location.local_frame
        shift = 3
        
        self.myDrone.go_to(location.north + shift, location.east + shift, location.down, 0)
        while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
            or self.vehicle.location.local_frame.east < location.east + shift - 0.3):
            time.sleep(1)
        
        self.myDrone.go_to(location.north + shift, location.east - shift, location.down, 0)
        while (self.vehicle.location.local_frame.north < location.north + shift - 0.3 \
            or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
            time.sleep(1)

        self.myDrone.go_to(location.north - shift, location.east - shift, location.down, 0)
        while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
            or self.vehicle.location.local_frame.east > location.east - shift + 0.3):
            time.sleep(1)
        
        self.myDrone.go_to(location.north - shift, location.east + shift, -1.5, 0)
        while (self.vehicle.location.local_frame.north > location.north - shift + 0.3 \
            or self.vehicle.location.local_frame.east < location.east + shift - 0.3 \
            or self.vehicle.location.local_frame.down < -1.5 - 0.1):
            time.sleep(1)
        
        self.myDrone.go_to(self.vehicle.location.local_frame.north, self.vehicle.location.local_frame.east, -1, 0)
        print("puskurt!!!!!!")
        for i in range(5):
            time.sleep(1)
            print("pssss")
        print("bitti")
        self.myDrone.immadiateLanding()

    def otonom_kalkis_inis(self, yukseklik : int = 1, saniye : int = 3):
        yukseklik = 5
        saniye = 3
        self.myDrone.arm_and_takeoff(yukseklik)

        countdown = saniye
        print('Waiting for ', countdown, ' secs..')

        for i in range(countdown):
            print('Countdown: ', countdown - i)
            time.sleep(1)

        self.myDrone.immadiateLanding()
    
    def otonom_yuksel(self, yukseklik : int = 1):
        self.myDrone.arm_and_takeoff(yukseklik)
