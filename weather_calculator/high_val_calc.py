from .file_reader import FileReader


class HighValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_highest_temp(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return max([
                max(list(filter(lambda x: x['Max TemperatureC'], row)), key=lambda y: int(y['Max TemperatureC']))
                for row in mapped_list], key=lambda y: int(y['Max TemperatureC']))
        else:
            return None

    def get_highest_humidity(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return max([
                max(list(filter(lambda x: x['Max Humidity'], row)), key=lambda y: int(y['Max Humidity']))
                for row in mapped_list], key=lambda y: int(y['Max Humidity']))
        else:
            return None

    def get_avg_high_temp(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return max([
                max(list(filter(lambda x: x['Mean TemperatureC'], row)), key=lambda y: int(y['Mean TemperatureC']))
                for row in mapped_list], key=lambda y: int(y['Mean TemperatureC']))
        else:
            return None
