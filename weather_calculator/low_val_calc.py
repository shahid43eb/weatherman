from .file_reader import FileReader


class LowValCalc(FileReader):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def get_lowest_temp(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return min([
                min(list(filter(lambda x: x['Min TemperatureC'], row)), key=lambda y: int(y['Min TemperatureC']))
                for row in mapped_list], key=lambda y: int(y['Min TemperatureC']))
        else:
            return None

    def get_lowest_humidity(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return min([
                min(list(filter(lambda x: x['Min Humidity'], row)), key=lambda y: int(y['Min Humidity']))
                for row in mapped_list], key=lambda y: int(y['Min Humidity']))
        else:
            return None

    def get_avg_low_temp(self):
        mapped_list = self.get_mapped_data_list()
        if len(mapped_list) > 0:
            return min([
                min(list(filter(lambda x: x['Mean TemperatureC'], row)), key=lambda y: int(y['Mean TemperatureC']))
                for row in mapped_list], key=lambda y: int(y['Mean TemperatureC']))
        else:
            return None
