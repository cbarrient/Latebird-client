import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)
while True:
    pin.on()
    time.sleep(2)
    pin.off()
    time.sleep(2)