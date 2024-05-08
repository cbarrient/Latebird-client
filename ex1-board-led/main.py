import machine
import time

# on-board LED = pin 2
pin = machine.Pin(2, machine.Pin.OUT)
while True:
    pin.on() # Note that pin.on() turns the LED off ¯\_(ツ)_/¯
    time.sleep(2)
    pin.off()
    time.sleep(2)