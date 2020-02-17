from math import floor
from statistics import mean

from .file_reader import FileReader


class AvgValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_avg_mean_humidity(self):
        return self.__get_avg_value("Mean Humidity")

    def get_avg_mean_temp(self):
        return self.__get_avg_value("Mean TemperatureC")

    def __get_avg_value(self, key_identifier):
        if len(self.mapped_data_list) > 0:
            return floor(
                mean([mean(int(x.get(key_identifier)) for x in list(filter(lambda x: x.get(key_identifier), row)))
                      for row in self.mapped_data_list]))
        else:
            return None
