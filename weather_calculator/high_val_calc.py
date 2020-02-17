from .file_reader import FileReader


class HighValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_highest_temp(self):
        return self.__get_highest_value("Max TemperatureC")

    def get_avg_high_temp(self):
        return self.__get_highest_value("Mean TemperatureC")

    def get_highest_humidity(self):
        return self.__get_highest_value("Max Humidity")

    def __get_highest_value(self, key_identifier):
        if len(self.mapped_data_list) > 0:
            return max([
                max(list(filter(lambda x: x.get(key_identifier), row)), key=lambda y: int(y.get(key_identifier)))
                for row in self.mapped_data_list], key=lambda y: int(y.get(key_identifier)))
        else:
            return None
