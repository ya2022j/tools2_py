


import openpyxl

from pandas.core.frame import DataFrame
import pandas as pd
import xlrd

import csv


def writeinto_detail(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        csv_out = csv.writer(f, delimiter=",")
        csv_out.writerow(data)


def output_list(list_item):
    for item in list_item:
        writeinto_detail(text_file,[item])

    writeinto_detail(text_file,["--"*20+ "Mercari---Engineer Vocabulary List" + "--"*20])

def read_excel(excelfile):
    file_dt = pd.read_excel(excelfile)
    for item in file_dt.values.tolist():
        output_list(item)


if __name__ =="__main__":
    excelfile = "d.xlsx"
    text_file = "dd.tsv"

    read_excel(excelfile)
