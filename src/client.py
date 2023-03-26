import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ["HOST"]
PORT = int(os.environ["PORT"])
BUFFER = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b"asdfwe")

    data = client.recv(BUFFER)
    print(data.decode('utf-8'))
