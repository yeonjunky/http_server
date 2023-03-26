import socket

HOST = 'localhost'
PORT = 8080
MAX_CLIENTS = 10
BUFFER = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    if not server:
        raise "cannot create socket"

    header = "HTTP/1.1 200 OK\nContent-type: text/plain\nContent-length: 12\n\nHello world!"

    server.bind((HOST, PORT))

    server.listen(MAX_CLIENTS)

    conn, address = server.accept()

    data = conn.recv(BUFFER)
    print(data.decode('utf-8'))
    conn.sendall("Hello from the server".encode())
    conn.close()
