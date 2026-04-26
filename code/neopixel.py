import time
from machine import Pin
from neopixel import NeoPixel
import state

NUM_LEDS = 16
np = NeoPixel(Pin(23), NUM_LEDS)

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def clear():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def run():
    rainbow_offset = 0
    spin_idx = 0

    while True:
        d = state.data["direction"]
        i = state.data["intensity"]

        if d == "right":
            speed_ms = max(10, 120 - i)
            clear()
            np[spin_idx % NUM_LEDS] = (0, 80, 255)
            np.write()
            spin_idx += 1
            time.sleep_ms(speed_ms)

        elif d == "left":
            speed_ms = max(10, 120 - i)
            clear()
            np[(NUM_LEDS - 1 - spin_idx) % NUM_LEDS] = (255, 50, 0)
            np.write()
            spin_idx += 1
            time.sleep_ms(speed_ms)

        else:
            spin_idx = 0
            for j in range(NUM_LEDS):
                np[j] = wheel((j * 256 // NUM_LEDS + rainbow_offset) % 256)
            np.write()
            rainbow_offset = (rainbow_offset + 1) % 256
            time.sleep_ms(30)
