# main.py -- put your code here!
import network
import urequests as requests

addr = "10.23.17.178"
port = "5000"
username = "Team x"

response = requests.get(f'http://{addr}:{port}/register?username={username}')
if 'already' in response.text:
    print(response.text)
    exit(0)
id = response.text[-32:]

while True:
    choice = input("Type your answer: ")
    response = requests.get(f'http://{addr}:{port}/answer?id={id}&choice={choice}')
    print(response.text)
