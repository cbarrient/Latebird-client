import machine
import time

Pin_A = 14 #D5
Pin_B = 5 #D1
Pin_C = 12 #D6
Pin_D = 4 #D2

button_A = machine.Pin(Pin_A, machine.Pin.IN, machine.Pin.PULL_UP)
button_B = machine.Pin(Pin_B, machine.Pin.IN, machine.Pin.PULL_UP)
button_C = machine.Pin(Pin_C, machine.Pin.IN, machine.Pin.PULL_UP)
button_D = machine.Pin(Pin_D, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    time.sleep(0.2)
    if not button_A.value():
        print('Button A pressed!')
    elif not button_B.value():
        print('Button B pressed!')
    elif not button_C.value():
        print('Button C pressed!')
    elif not button_D.value():
        print('Button D pressed!')
    else:
        print('Waiting for input...')