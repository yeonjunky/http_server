from socket import *
import logging
import signal, sys

class Server:    
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.logger = logging.getLogger("server")
        
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        
    def listen(self, host='', port=8080, max_clients=5, size=1024):
        with self.socket:            
            self.socket.bind((host, port))
            self.socket.listen(max_clients)

            while True:
                try:
                    client, addr = self.socket.accept()
                    data = client.recv(size).decode()

                    if len(data):
                        self.logger.info(f"received data '{data}' from {addr}")
                        self.echo(client, data)
                        
                    else:
                        self.logger.warning("nothing to read from data.")
                        client.sendall("received nothing from client.".encode())

                    client.close()
                    
                except KeyboardInterrupt:
                    self.socket.close()

    def echo(self, client, data):
        client.sendall("hi from server".encode())

        
def exit_handler(signal, frame):
    sys.exit(0)
    
signal.signal(signal.SIGINT, exit_handler)
        
s = Server()
s.listen()