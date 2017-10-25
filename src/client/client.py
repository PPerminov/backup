from sys import exit


def options_parser():
    from argparse import ArgumentParser
    parser = ArgumentParser(usage=None)
    parser.add_argument('folder')
    args = parser.parse_args()
    return args


test_folder = options_parser().folder


def sender(file, connection):
    with open(file, 'rb') as stream:
        while True:
            try:
                line = stream.read(512)
            except:
                break
            connection.send(line)
            try:
                answer = connection.recv(1)
                if answer != 1:
                    break
            except:
                break


def connector(address):
    from socket import socket
    connection = socket()
    connection.connect((address, 5689))
    return connection


def filelist(folder):
    from os import walk, path
    folder = path.abspath(folder)
    file_list = list()
    for root, subdirs, file_name in walk(folder):
        if file_name:
            for fn in file_name:
                current_object = [root, fn]
                file_list.append(current_object)
    return file_list


def hasher(filepath):
    from hashlib import sha256
    with open(filepath, 'rb') as stream:
        digest = sha256(stream.read()).hexdigest()
    return digest


def database(filename):
    from sqlite3 import connect
    try:
        connection = connect(filename)
        return connection
    except:
        return None


def database_preparation(db_cur):
    db_cur.execute('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, path TEXT, link_path TEXT, link_type BOOLEAN, hash VARCHAR NOT NULL, cdate DATETIME not null, mdate DATETIME not null, size BIGINT UNSIGNED)')
    db_cur.execute(
        'CREATE INDEX IF NOT EXISTS files_index ON files (hash, name, cdate)')


def file_stat(file_list, db, hash_needed=False):
    from os import stat
    from os.path import islink, realpath
    return_list = list()
    for item in file_list:
        path = item[0]
        name = item[1]
        full_path = path + '/' + name
        if islink(full_path):
            link_path = realpath(full_path)
        else:
            link_path = "null"
        try:
            current_stat = stat(full_path)
            if hash_needed == True:
                sha_summ = hasher(full_path)
            else:
                sha_summ = "null"
            data = [name, path, link_path, sha_summ, current_stat.st_ctime,
                    current_stat.st_mtime, current_stat.st_size]
            return_list.append(data)
        except:
            continue
    db.executemany(
        'INSERT INTO files (name,path,link_path,hash,cdate,mdate,size) values (?,?,?,?,?,?,?)', return_list)
    db.commit()


db = database('bb.db')
database_preparation(db)


file_stat(filelist(test_folder), db, True)
