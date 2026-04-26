import network
import socket
import time
import _thread
import state
from machine import Pin, PWM

# ── WiFi ─────────────────────────────────────────────────────
SSID     = "XxSigmaHotspotxX"
PASSWORD = "SigmaHotspot"
w = network.WLAN(network.STA_IF)
w.active(False)
time.sleep(0.5)
w.active(True)
w.connect(SSID, PASSWORD)
print("Connecting to WiFi...")
for _ in range(20):
    if w.isconnected():
        break
    time.sleep(0.5)
print("IP:", w.ifconfig()[0])

# ── Motor / GVS ──────────────────────────────────────────────
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(4, Pin.OUT)
EN  = PWM(Pin(21, Pin.OUT), freq=1000)
MIN_DUTY = 512
MAX_DUTY = 1023

def set_gvs(direction, intensity):
    duty = int(MIN_DUTY + (intensity / 100) * (MAX_DUTY - MIN_DUTY))
    if direction == "right":
        IN1.on(); IN2.off(); EN.duty(duty)
    elif direction == "left":
        IN1.off(); IN2.on(); EN.duty(duty)
    else:
        IN1.off(); IN2.off(); EN.duty(0)

def parse_input(raw):
    raw = raw.strip().lower()
    if raw in ("stop", ""):
        return None, 0
    parts = raw.split(":")
    if len(parts) == 2:
        try:
            intensity = max(0, min(100, int(parts[1])))
            return parts[0], intensity
        except:
            pass
    return None, 0

# ── UDP listener ─────────────────────────────────────────────
def udp_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", 5005))
    s.settimeout(0.1)
    print("UDP listening on port 5005")
    while True:
        try:
            data, _ = s.recvfrom(64)
            line = data.decode("utf-8", "ignore").strip()
            if line:
                d, i = parse_input(line)
                state.data["direction"] = d
                state.data["intensity"] = i
                print("RX:", line)
        except:
            pass

# ── Launch ────────────────────────────────────────────────────
import neopixel_fx
_thread.start_new_thread(udp_listener, ())
_thread.start_new_thread(neopixel_fx.run, ())

print("GVS ready")
while True:
    set_gvs(state.data["direction"], state.data["intensity"])
    time.sleep_ms(20)
