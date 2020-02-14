from argparse import ArgumentParser
from os import path
from zipfile import is_zipfile, ZipFile

from reports_generater.reports_generater import ReportGenerator


def parse_process_argv():
    parse = ArgumentParser()
    parse.add_argument('filepath', type=str, help='Zip file for extraction!')
    parse.add_argument('-a', type=str, help='Option for average highest temperature​, '
                                            'average lowest temperature​,​ average mean humidity!')
    parse.add_argument('-e', type=str, help='Option for ​highest temperature​, ​lowest temperature​ and ​ humidity​!')
    parse.add_argument('-c', type=str, help='Option for horizontal bar charts!')
    args = parse.parse_args()
    return args


def extract_files(filepath):
    if path.exists(filepath) and path.isfile(filepath) and is_zipfile(filepath):
        zipfile = ZipFile(filepath)
        try:
            zipfile.extractall('./files')
            extractedfilespath = path.abspath('./files/weatherfiles')
            print(f"File Extracted from {filepath} to {extractedfilespath}")
            return extractedfilespath
        except Exception:
            print("Unexpected error!")
            raise
    else:
        print("Error: Invalid File!")


def genrate_reports(args, extracted_files_path):
    if args.e:
        ReportGenerator(extracted_files_path, args.e).high_value_report()
    if args.a:
        ReportGenerator(extracted_files_path, args.a).avg_value_report()
    if args.c:
        ReportGenerator(extracted_files_path, args.c).chart_report()


def run_weatherman():
    args = parse_process_argv()
    extracted_files_path = extract_files(args.filepath)
    genrate_reports(args, extracted_files_path)


run_weatherman()
