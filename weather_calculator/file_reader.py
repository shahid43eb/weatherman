from os import path, listdir

from file_handler.file_handler import FileHandler
from helpers.formetted_date import FormattedDate


class FileReader:
    def __init__(self, dir_path, duration):
        self.dir_path = dir_path
        self.duration = duration
        self.mapped_data_list = self.__get_mapped_data_list()

    def __get_files(self):
        if path.exists(self.dir_path) and path.isdir(self.dir_path):
            all_files = listdir(self.dir_path)
            if len(self.duration.split('/')) > 1:
                return [path.join(self.dir_path, x) for x in all_files if
                        x.find(FormattedDate(self.duration).get_year_month()) > 0]
            else:
                return [path.join(self.dir_path, x) for x in all_files if x.find(self.duration) > 0]

        raise Exception('Invalid directory path!')

    def __get_mapped_data_list(self):
        files = self.__get_files()
        if len(files) > 0:
            return list(map(lambda file: FileHandler(file).format_file_data(), files))

        raise Exception('No Data Exist for given date')
