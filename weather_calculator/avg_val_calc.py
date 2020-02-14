from math import floor
from statistics import mean

from .file_reader import FileReader


class AvgValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_avg_mean_humidity(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return floor(mean([mean(int(x['Mean Humidity']) for x in list(filter(lambda x: x['Mean Humidity'], row)))
                               for row in mapped_list]))
        else:
            return None

    def get_avg_mean_temp(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return floor(
                mean([mean(int(x['Mean TemperatureC']) for x in list(filter(lambda x: x['Mean TemperatureC'], row)))
                      for row in mapped_list]))
        else:
            return None
