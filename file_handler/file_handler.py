from pandas import read_excel


class FileHandler:
    def __init__(self, file):
        self.file = file

    def format_file_data(self):
        if self.file.endswith('.txt'):
            return self.__format_txt_file_data()
        elif self.file.endswith('tsv'):
            return self.__format_tsv_file_data()
        elif self.file.endswith('xlsx'):
            return self.__format_xlsx_file_data()
        else:
            raise Exception('Invalid file extension!')

    def __format_txt_file_data(self):
        f = open(self.file, 'r')
        file_data = f.read()
        rows = list(filter(None, file_data.split('\n')))
        header = rows.pop(0).split(',')
        header = list(map(str.strip, header))
        return [{header[idx]: value for idx, value in enumerate(row.split(','))} for row in rows]

    def __format_tsv_file_data(self):
        f = open(self.file, 'r')
        file_data = f.read()
        rows = list(filter(None, file_data.split('\n')))
        header = rows.pop(0).split('\t')
        header = list(map(str.strip, header))
        return [{header[idx]: value for idx, value in enumerate(row.split('\t'))} for row in rows]

    def __format_xlsx_file_data(self):
        file_data = read_excel(self.file)
        return file_data.to_dict('records')
