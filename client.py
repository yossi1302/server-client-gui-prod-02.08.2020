import socket
import random
import time
import threading
import json
import pathlib


HEADER = 64
path = pathlib.Path(__file__).parent.absolute()
<<<<<<< HEAD
with open(f'{path}/vars.json') as f:
=======
with open(f'{path}/vars.json', 'r') as f:
>>>>>>> 6ceefb78f4c54588f608eec55a2e52a2b2e033ae
    data = json.load(f)
for p in data["vars"]:
    SERVER = p["ServerMACAdress"]
    PORT = int(p["PORT"])
ADDR=(SERVER, int(PORT))
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
client.connect(SERVER)


def send(msg):
    msg = str(msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def generate_random_num():
   num = random.randint(0, 10)
   return num


def quit():
    while True:
        user_input = input()
        if user_input == "quit":
            send(DISCONNECT_MESSAGE)


while True:
    thread = threading.Thread(target=quit)
    thread.start()
    num = generate_random_num()
    send(num)
    time.sleep(5)