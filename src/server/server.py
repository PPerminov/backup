#!/usr/bin/env python3
"""
Идентификатор   ITPlusBackup
версия          1 1 2 3
Направление     1 с->s 0 s->c
Пароль          lkjhgf5d46e5fr7tg8y9



"""
from socket import socket
from sys import exit
from threading import Thread
from sqlite3 import connect
from ipaddr import IPAddress


def options_parser():
    from argparse import ArgumentParser
    tr = "\n\
    \n\
    fdsfdsfds"
    parser = ArgumentParser(usage=tr)
    parser.add_argument('type', choices=['client', 'server'])
    parser.add_argument('--server')
    args = parser.parse_args()
    if args.type == 'client':
        if not args.server:
            print(
                'If you choose Client mode you must point to server [--server]')
            return None
        try:
            address = IPAddress(args.server)
            return address
        except:
            print('Very bad IP')
            return None
    elif args.type == 'server':
        return True
    return False


# options_parser()
#
# exit()
ar = socket()
ar.bind(('127.0.0.1', 2569))
# print(ar)
ar.listen(0)
array_connections = []
# array_addresses=[]


class worker(Thread):
    def __init__(self, opened_connection):
        Thread.__init__(self)
        if isinstance(opened_connection, socket.socket):
            self.socket = opened_connection

    def run(self):
        while True:
            hello_string = self.socket.recv(512)
            if hello_string.decode().count('') >= 512:
                print(hello_string)


def connection_catcher(open_socket):
    print(1)


while True:
    current = None
    current = ar.accept()
    with open('ttrt','w') as file1:
        file1.write(current[0].recv(4848564165).decode())

ar.close()
