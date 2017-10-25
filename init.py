def main():
    arguments=params()
    if arguments.type == "server":
        server()
    else:
        client()

def server():
    import src\/server\/server as server_module
    print(dir(server_module))

def params():
    from argparse import ArgumentParser
    parser=ArgumentParser(description="Now we will PARSE!!!1")
    parser.add_argument('-t','--type',action='store')
    # parser.parse_args()
    return parser.parse_args()








if __name__ == '__main__':
    main()
