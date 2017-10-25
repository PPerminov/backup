def main():
    arguments=params()
    if arguments.type == "server":
        server()()
    else:
        client()

def server():
    import importlib.util
    spec = importlib.util.spec_from_file_location('server_module','./src/server/server.py')
    data = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(data)
    return data.main


def params():
    from argparse import ArgumentParser
    parser=ArgumentParser(description="Now we will PARSE!!!1")
    parser.add_argument('-t','--type',action='store')
    # parser.parse_args()
    return parser.parse_args()








if __name__ == '__main__':
    main()
