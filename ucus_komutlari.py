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
