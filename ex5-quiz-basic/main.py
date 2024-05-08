import urequests as requests
import machine
import time

pin_mapping = {'A': 14, 'B': 5, 'C': 12, 'D': 4}
buttons = {key: machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for key, pin in pin_mapping.items()}

def register_or_login(addr):
    registered = input("Have you already registered? yes/no: ")
    if registered.lower().startswith('y'):
        return login(addr)
    else:
        return register(addr)

def register(addr):
    response = ""
    while "success" not in response:
        username = input("Please enter your team name: ")
        response = requests.get(f'http://{addr}/register?username={username}').text
        print(response)
    return response[-8:]

def login(addr):
    response = ""
    while 'Welcome back' not in response:
        id_test = input("Please enter your team ID: ")
        response = requests.get(f'http://{addr}/login?id={id_test}').text
        print(response)
    return id_test
        
def send_answer(addr, id, choice):
    response = requests.get(f'http://{addr}/answer?id={id}&choice={choice}').text
    print(response)

def main():
    id = ""
    addr = "crawdad-humble-usually.ngrok-free.app"
    input("Press enter to start")
    id = register_or_login(addr)

    print("You can now participate in the quiz! Press any button to send your answer:")

    while True:
        time.sleep(0.2)
        for key, button in buttons.items():
            if not button.value():
                print(f'Button {key} pressed!')
                send_answer(addr, id, key)

main()