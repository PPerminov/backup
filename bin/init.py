def variables():
    from os.path import abspath as path
    from os.path import dirname
    root = dirname(path(__file__))
    server = path(root + "/server")
    client = path(root + "/client")
    temp = path(root + "/../temp")
    conf = path(root + "/../conf")
    database = path(root + "/../database")
    root_bfs = path(root + "/../backup")
    return {"root": root, "server": server,
            "client": client, "temp": temp, "database": database,
            "root_bfs": root_bfs, "conf": conf}


def main():
    import sys
    arguments = params()
    varys = variables()
    setup(varys)
    if arguments.type == "server":
        server()()
    elif arguments.type == "client":
        client()
    else:
        sys.exit()


def server():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'server_module', './src/server/server.py')
    data = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(data)
    return data.main


def params():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Now we will PARSE!!!1")
    parser.add_argument('-t', '--type', action='store')
    return parser.parse_args()


def setup(folders_list):
    from os.path import exists as check
    from os import makedirs as makedir
    for item, de in folders_list.items():
        if not check(de):
            makedir(de)


if __name__ == '__main__':
    main()
