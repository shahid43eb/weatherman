from datetime import date
from os import path, listdir

from file_handler.file_handler import FileHandler


class FileReader:
    def __init__(self, dir_path, duration):
        self.dir_path = dir_path
        self.duration = duration

    def __get_files(self):
        if path.exists(self.dir_path) and path.isdir(self.dir_path):
            date_arr = [int(x) for x in self.duration.split('/')]
            all_files = listdir(self.dir_path)
            if len(date_arr) > 1:
                return [path.join(self.dir_path, x) for x in all_files if
                        x.find(date(date_arr[0], date_arr[1], 1).strftime('%Y_%b')) > 0]
            else:
                return [path.join(self.dir_path, x) for x in all_files if x.find(self.duration) > 0]

        else:
            raise Exception('Invalid directory path!')

    def get_mapped_data_list(self):
        files = self.__get_files()
        if len(files) > 0:
            return list(map(lambda file: FileHandler(file).format_file_data(), files))
        else:
            return []
