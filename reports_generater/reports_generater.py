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
        humidity = self.get_highest_humidity()
        print(f'Highest: {BColors.FAIL}{max_temp.get("Max TemperatureC")}C{BColors.ENDC} '
              f'on {FormattedDate(max_temp.get("PKT") or max_temp.get("PKST")).get_month_day()}')
        print(f'Lowest: {BColors.OKBLUE}{min_temp.get("Min TemperatureC")}C{BColors.ENDC} '
              f'on {FormattedDate(min_temp["PKT"]).get_month_day()}')
        print(f'Humidity: {BColors.OKGREEN}{humidity.get("Max Humidity")}%{BColors.ENDC}\n')

    def avg_value_report(self):
        avg_max_temp = self.get_avg_high_temp()
        avg_min_temp = self.get_avg_low_temp()
        avg_mean_humidity = self.get_avg_mean_humidity()
        print(f"{BColors.BOLD}"
              f"{FormattedDate(self.duration).get_year_month_s() if len(self.duration.split('/')) > 1 else self.duration}"
              f"{BColors.ENDC}")
        print(f'Highest Average: {BColors.FAIL}{avg_max_temp.get("Mean TemperatureC")}C{BColors.ENDC}')
        print(f'Lowest Average: {BColors.OKBLUE}{avg_min_temp.get("Min TemperatureC")}C{BColors.ENDC}')
        print(f'Average Mean Humidity: {BColors.OKGREEN}{avg_mean_humidity}{BColors.ENDC}%\n')

    def chart_report(self):
        for month_list in self.mapped_data_list:
            for idx, day_obj in enumerate(month_list):
                low_chart = abs(int(day_obj.get('Min TemperatureC'))) * (
                    '-' if int(day_obj.get('Min TemperatureC')) < 0 else '+')
                if idx == 0:
                    print(f"{BColors.BOLD}"
                          f"{FormattedDate(day_obj.get('PKT') or day_obj.get('PKST')).get_year_month_s()}"
                          f"{BColors.ENDC}")
                print(
                    f"{FormattedDate(day_obj.get('PKT') or day_obj.get('PKST')).get_day()} {BColors.OKBLUE}"
                    f"{low_chart}"
                    f"{BColors.FAIL}{'+' * int(day_obj.get('Max TemperatureC'))}{BColors.ENDC} "
                    f"{BColors.OKBLUE}{day_obj.get('Min TemperatureC')}C{BColors.ENDC} "
                    f"{BColors.FAIL}{day_obj.get('Max TemperatureC')}C{BColors.ENDC}"
                )
