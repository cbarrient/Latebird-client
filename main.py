import requests

addr = "crawdad-humble-usually.ngrok-free.app"

# id will be automatically set, but save it in case the script errors
id = ''

while not id:
    username = input("Choose your team name: ")
    response = requests.get(f'http://{addr}/register?username={username}')
    if 'already' in response.text:
        print(response.text)
    else:
        print(response.text)
        id = response.text[-32:]

while True:
    choice = input("Type your answer: ")
    response = requests.get(f'http://{addr}/answer?id={id}&choice={choice}')
    print(response.text)
