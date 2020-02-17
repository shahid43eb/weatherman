from .file_reader import FileReader


class LowValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_lowest_temp(self):
        return self.__get_lowest_value("Min TemperatureC")

    def get_lowest_humidity(self):
        return self.__get_lowest_value("Min Humidity")

    def get_avg_low_temp(self):
        return self.__get_lowest_value("Mean TemperatureC")

    def __get_lowest_value(self, key_identifier):
        if len(self.mapped_data_list) > 0:
            return min([
                min(list(filter(lambda x: x.get(key_identifier), row)), key=lambda y: int(y.get(key_identifier)))
                for row in self.mapped_data_list], key=lambda y: int(y.get(key_identifier)))
        else:
            return None
