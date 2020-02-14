import re
from datetime import date


class FormattedDate:

    def __init__(self, i_date):
        self._date = i_date
        self._date_parts = self.__date_parts()

    def __date_parts(self):
        separators = (',', '/', ' ', '.', '-')
        dateParts = re.split("[%s]" % (''.join(separators)), self._date)
        return [int(dateParts[0]), int(dateParts[1]), (int(dateParts[2]) if (len(dateParts)) > 2 else 1)]

    def get_year_month(self):
        d = date(self._date_parts[0], self._date_parts[1], self._date_parts[2])
        return d.strftime("%Y_%b")

    def get_year_month_s(self):
        d = date(self._date_parts[0], self._date_parts[1], self._date_parts[2])
        return d.strftime("%Y %b")

    def get_month_day(self):
        d = date(self._date_parts[0], self._date_parts[1], self._date_parts[2])
        return d.strftime("%b %d")

    def get_day(self):
        d = date(self._date_parts[0], self._date_parts[1], self._date_parts[2])
        return d.strftime("%d")
