import socket

HOST = "localhost"
PORT = 8080
BUFFER = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.send("Hello from client".encode())

    data = client.recv(BUFFER)
    print(data.decode('utf-8'))
