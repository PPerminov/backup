from os import walk, path, stat
from os.path import islink, realpath


class Client:
    def __init__(self, server, file_path):
        self.server = server
        self.file_path = file_path
        self.all_files = list()
        self.all_dirs = list()
        self.changed_files = list()
        self.files_iterator = walk(self.file_path)

    def build_filellist(self):
        for root, dirs, files in self.files_iterator:
            for dir in dirs:
                self.all_dirs.append(realpath(root + '/' + dir))
            for file in files:
                file_path = realpath(root + '/' + file)
                file_data = stat(file_path)
                self.all_files.append(
                    {'path': file_path,
                     'size': file_data.st_size,
                     'mtime': file_data.st_mtime}
                )
