import machine
import time

pin_mapping = {'A': 14, 'B': 5, 'C': 12, 'D': 4}
buttons = {key: machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for key, pin in pin_mapping.items()}
while True:
        time.sleep(0.2)
        for key, button in buttons.items():
            if not button.value():
                print(f'Button {key} pressed!')
        
