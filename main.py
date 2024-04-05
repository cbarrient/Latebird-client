import urequests as requests
import machine
import time

addr = "crawdad-humble-usually.ngrok-free.app"
id = ""
Pin_A = 14 #D5
Pin_B = 5 #D1
Pin_C = 12 #D6
Pin_D = 4 #D2

button_A = machine.Pin(Pin_A, machine.Pin.IN, machine.Pin.PULL_UP)
button_B = machine.Pin(Pin_B, machine.Pin.IN, machine.Pin.PULL_UP)
button_C = machine.Pin(Pin_C, machine.Pin.IN, machine.Pin.PULL_UP)
button_D = machine.Pin(Pin_D, machine.Pin.IN, machine.Pin.PULL_UP)

def send_answer(addr, id, choice):
    response = requests.get(f'http://{addr}/answer?id={id}&choice={choice}')
    print(response.text)

skip = input("Press enter to continue: ")
registered = input("Have you already registered? yes/no ")
if registered[0].lower() == 'y':
    while not id:
        id_test = input("Please enter your team ID: ")
        response = requests.get(f'http://{addr}/login?id={id_test}')
        if 'exist' in response.text:
            print(response.text)
        else:
            print(response.text)
            id = id_test
else:
    while not id:
        username = input("Please enter your team name: ")
        response = requests.get(f'http://{addr}/register?username={username}')
        if 'already' in response.text:
            print(response.text)
        else:
            print(response.text)
            id = response.text[-8:]

print("You can now participate in the quiz! Press any button to send your answer:")

while True:
    time.sleep(0.2)
    if not button_A.value():
        print('Button A pressed!')
        choice = 'A'
        send_answer(addr, id, choice)
    elif not button_B.value():
        print('Button B pressed!')
        choice = 'B'
        send_answer(addr, id, choice)
    elif not button_C.value():
        print('Button C pressed!')
        choice = 'C'
        send_answer(addr, id, choice)
    elif not button_D.value():
        print('Button D pressed!')
        choice = 'D'
        send_answer(addr, id, choice)
