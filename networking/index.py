from socket import socket


class NetworkModuleException(Exception):
    def __init__(self):
        super().__init__()
        # self.errors = errors


class Connection(socket):
    def __init__(self, connection_type, ip='0.0.0.0', port=1666):
        self.connection_type = connection_type
        self.ip = ip
        self.port = port
        self.socket = socket()
        self.running = False

    def start(self):
        if self.connection_type == 'server':
            self.start_server_network()
        elif self.connection_type == 'client':
            self.start_client_network()
        else:
            raise Exception
        self.running = True

    def start_server_network(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen()

    def start_client_netwok(self):
        self.socket.connect((self.ip, self.port))

    def send(self, msg):
        self.socket.send(msg.encode('utf8'))

    def recieve(self):
        try:
            while True:
                try:
                    part = self.socket.recv(1024)
                    if not part:
                        pass
                except Exception:
                    pass
        except KeyboardInterrupt:
            pass
