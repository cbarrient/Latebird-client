import machine
import time

led_mapping = {'Red': 13, 'Green': 15}
leds = {key: machine.Pin(pin, machine.Pin.OUT) for key, pin in led_mapping.items()}
while True:
    color = input("Which colour do you want to see blink? (Red/Green): ")
    if color not in ['Red', 'Green']:
        continue
    leds[color].on()
    time.sleep(1)
    leds[color].off()
