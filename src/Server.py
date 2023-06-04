from socket import *
import logging
import signal, sys
from HTTPRequest import HTTPRequest

class Server:    
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.logger = logging.getLogger("server")
        
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        self.httpRequest = HTTPRequest()
        
    def listen(self, host='', port=8080, max_clients=5, size=1024):
        with self.socket:            
            self.socket.bind((host, port))
            self.socket.listen(max_clients)

            while True:
                try:
                    client, addr = self.socket.accept()
                    data = client.recv(size).decode()

                    if len(data):
                        response = "HTTP/1.1 200 OK \r\n\r\n <p>hello world</p>"
                        self.logger.info(f"received data from {addr}")
                        print(self.httpRequest.parse(data))
                        self.response(client, response)
                        
                    else:
                        self.logger.warning("nothing to read from data.")
                        client.sendall("GET HTTP/1.1 200".encode())

                    client.close()
                    
                except KeyboardInterrupt:
                    self.socket.close()

    def echo(self, client, data):
        client.sendall("hi from server".encode())

    def response(self, client, data):
        client.sendall(data.encode())

        
def exit_handler(signal, frame):
    sys.exit(0)
    
signal.signal(signal.SIGINT, exit_handler)
        
s = Server()
s.listen()