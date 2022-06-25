from multiprocessing.connection import Listener
from pynput import keyboard

keys = ['w', 'a', 's', 'd', 'up', 'down']
held = dict(zip(keys, [0,0,0,0,0,0]))

class keyboard_events:
    def __init__(self, drone):
        self.drone = drone

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except:
            k = key.name
        if k in keys:
            held[k] = 6
            self.drone.send_ned_velocity(
                held['w'] - held['s'],
                held['d'] - held['a'],
                min((held['down'] - held['up']) * 0.5, 1)
            )
            print('Key pressed: ' + k)

    def on_release(self, key):
        try:
            k = key.char
        except:
            k = key.name
        if k in keys:
            held[k] = 0
            self.drone.send_ned_velocity(
                held['w'] - held['s'],
                held['d'] - held['a'],
                min((held['down'] - held['up']) * 0.5, 1)
            )
            print('Key released: ' + k)