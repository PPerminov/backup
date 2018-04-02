from unittest import TestCase, main
from os import walk
import types
import importlib
index = importlib.import_module('index')

test_server = '127.0.0.1'
test_path = './tests/filellist'

client1 = index.Client(test_server, test_path)
client1.build_filellist()

client_network1 = index.Connection('client','127.0.0.1',6646)
server_network1 = index.Connection('server','127.0.0.1',6646)


class init_tests(TestCase):

    def test_base(self):
        self.assertTrue(isinstance(client1, index.Client))
        self.assertTrue(client1.server == test_server)
        self.assertTrue(client1.file_path == test_path)
        self.assertTrue(isinstance(
            client1.files_iterator, types.GeneratorType))
        self.assertTrue(len(client1.all_dirs) == 3)
        self.assertTrue(len(client1.all_files) == 6)
        self.assertTrue(isinstance(client1.all_files[0],dict))

    def test_network(self):
        self.assertTrue(client_network1 != server_network1)


if __name__ == '__main__':
    main()

    # all_dirs
