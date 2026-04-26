"""
pip install pygame
run with: py relay.py
"""

import socket
import time
import pygame

ESP32_PORT = 5005
ESP32_IP = "10.100.207.111"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(cmd):
    sock.sendto((cmd + "\n").encode(), (ESP32_IP, ESP32_PORT))
    print(f"→ {cmd}")

pygame.init()
pygame.joystick.init()
joy = None
if pygame.joystick.get_count() > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()
    print(f"Gamepad: {joy.get_name()}")
else:
    print("No gamepad found")

print("Sending to ESP32 at", ESP32_IP)
print("Left stick = direction + intensity")

last_cmd = ""
while True:
    pygame.event.pump()
    cmd = "stop"
    if joy:
        lx = joy.get_axis(0)
        if lx > 0.15:
            cmd = f"right:{int((lx-0.15)/0.85*100)}"
        elif lx < -0.15:
            cmd = f"left:{int((-lx-0.15)/0.85*100)}"
    if cmd != last_cmd:
        send(cmd)
        last_cmd = cmd
    time.sleep(0.05)
