from socket import socket

class NetworkModuleException(Exception):
    def __init__(self):
        super().__init__()
        # self.errors = errors

class Connection(socket):
    def __init__(self, connection_type, ip, port):
        self.connection_type = connection_type
        self.ip = ip
        self.port = port
        self.socket=socket()

    def start(self):
        if self.connection_type == 'server':
            self.start_server_network()
        elif self.connection_type == 'client':
            self.start_client_network()
        else:
            raise Exception

    def start_server_network(self):
        self.socket.bind((self.ip,self.port))
        self.socket.listen()

    def start_client_netwok(self):
        self.socket.connect((self.ip,self.port))

        #
        # if type == 'client':
        #     self.server=ip
        # self.bind_ip=ip
        # connection = socket()
        # connection.bind((ip,port))
        # connection.listen()
        # # return connection
