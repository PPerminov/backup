from sqlite3 import connect
from os.path import exists
from os import remove
from sys import exit
from os.path import abspath as path
from os.path import dirname


# Variables module
root_dir = path(dirname(path(__file__)) + "/..")
conf_dir = path(root_dir + "/conf")
db_dir = path(root_dir + "/database")
print(conf_dir)
main_db_file = path(db_dir + "/main.db")


def setup_main_db():
    if exists(main_db_file):
        remove(main_db_file)
    main_db = connect(main_db_file)
    sqlite_setup_file=path(conf_dir + "/sqlite_setup.sql")
    try:
        setup_query=open(sqlite_setup_file,'r').read()
        cursor=main_db.cursor()
        cursor.executescript(setup_query)
        cursor.close()
        main_db.commit()
        main_db.close()
        return True
    except FileNotFoundError:
        print('No setup file')
        return False

setup_main_db()
exit()

# def db_selector():
    # if not exists(main_db_file):
        # setup_main_db()


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
        if isinstance(item, socket.socket):
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
