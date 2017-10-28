def variables():
    from os.path import abspath as path
    from os.path import dirname
    root = dirname(path(__file__))
    temp = path(root + "/../temp")
    conf = path(root + "/../conf")
    database = path(root + "/../database")
    root_bfs = path(root + "/../backup")
    return {"root": root, "temp": temp, "database": database,
            "root_bfs": root_bfs, "conf": conf}


def main():
    from sys import exit
    arguments = params()
    varys = variables()
    setup(varys)
    try:
        program = __import__(arguments.type)
    except ImportError:
        print('Bad type value. Needed server or client')
        exit(89)
    program.main()


def params():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Now we will PARSE!!!1")
    parser.add_argument('-t', '--type', action='store')
    return parser.parse_args()


def setup(folders_list):
    from os.path import exists as check
    from os import makedirs as makedir
    for item, path in folders_list.items():
        if not check(path):
            makedir(path)


if __name__ == '__main__':
    main()
