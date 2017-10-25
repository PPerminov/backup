
# from threading import Thread
# from sqlite3 import connect
# from ipaddress import IPv4Address


# class worker(Thread):
#     def __init__(self, opened_connection):
#         Thread.__init__(self)
#         if isinstance(opened_connection, socket.socket):
#             self.socket = opened_connection
#
#     def run(self):
#         while True:
#             hello_string = self.socket.recv(512)
#             if hello_string.decode().count('') >= 512:
#                 print(hello_string)


def connection_catcher(socket):
    global connections
    while True:
        current = socket.accept()
        if current:
            connections.append(current[1])
        print(connections)


def listener(address="0.0.0.0", port=6891):
    from socket import socket
    sock = socket()
    sock.bind((address, port))
    sock.listen(0)
    # print(globals())
    return sock


def killall():
    import gc
    import socket
    for item in gc.get_objects():
        if isinstance(item,socket.socket):
            item.close()



def main():
    server = listener(port=6891)
    print('Port:', server.getsockname()[1])
    connections = list()
    try:
        connection_catcher(server)
    except KeyboardInterrupt:
        from sys import exit
        killall()
        exit()
