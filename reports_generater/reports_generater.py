from helpers.basic_colors import BColors
from helpers.formetted_date import FormattedDate
from weather_calculator.avg_val_calc import AvgValCalc
from weather_calculator.high_val_calc import HighValCalc
from weather_calculator.low_val_calc import LowValCalc


class ReportGenerator(HighValCalc, LowValCalc, AvgValCalc):
    def __init__(self, dir_path, duration):
        super().__init__(dir_path, duration)

    def high_value_report(self):
        max_temp = self.get_highest_temp()
        min_temp = self.get_lowest_temp()
        print(f"{BColors.BOLD}"
              f"{FormattedDate(self.duration).get_year_month_s() if len(self.duration.split('/')) > 1 else self.duration}"
              f"{BColors.ENDC}")
        print(f'Highest: {BColors.FAIL}{max_temp["Max TemperatureC"]}C{BColors.ENDC} '
              f'on {FormattedDate(max_temp["PKT"]).get_month_day()}')
        print(f'Lowest: {BColors.OKBLUE}{min_temp["Min TemperatureC"]}C{BColors.ENDC} '
              f'on {FormattedDate(min_temp["PKT"]).get_month_day()}')
        print(f'Humidity: {BColors.OKGREEN}{min_temp["Max Humidity"]}%{BColors.ENDC}\n')

    def avg_value_report(self):
        avg_max_temp = self.get_avg_high_temp()
        avg_min_temp = self.get_avg_low_temp()
        avg_mean_humidity = self.get_avg_mean_humidity()
        print(f"{BColors.BOLD}"
              f"{FormattedDate(self.duration).get_year_month_s() if len(self.duration.split('/')) > 1 else self.duration}"
              f"{BColors.ENDC}")
        print(f'Highest Average: {BColors.FAIL}{avg_max_temp["Mean TemperatureC"]}C{BColors.ENDC}')
        print(f'Lowest Average: {BColors.OKBLUE}{avg_min_temp["Min TemperatureC"]}C{BColors.ENDC}')
        print(f'Average Mean Humidity: {BColors.OKGREEN}{avg_mean_humidity}{BColors.ENDC}%\n')

    def chart_report(self):
        mapped_list = self.get_mapped_data_list()
        for month_list in mapped_list:
            for idx, day_obj in enumerate(month_list):
                if idx == 0:
                    print(f"{BColors.BOLD}{FormattedDate(day_obj['PKT']).get_year_month_s()}{BColors.ENDC}")
                print(
                    f"{FormattedDate(day_obj['PKT']).get_day()} {BColors.OKBLUE}"
                    f"{abs(int(day_obj['Min TemperatureC'])) * ('-' if int(day_obj['Min TemperatureC']) < 0 else '+')}"
                    f"{BColors.FAIL}{'+' * int(day_obj['Max TemperatureC'])}{BColors.ENDC} "
                    f"{BColors.OKBLUE}{day_obj['Min TemperatureC']}C{BColors.ENDC} "
                    f"{BColors.FAIL}{day_obj['Max TemperatureC']}C{BColors.ENDC}"
                )
