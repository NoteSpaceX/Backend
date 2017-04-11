import csv
import re
from tkinter import END


class Navigate:
    # away to get the line number of something we want
    @staticmethod
    def get_line(word, text):
        #
        with open(text) as file:
            for num, line in enumerate(file, 1):
                if word in line:
                    return num

        # text = text.get('1.0', END)
        # for line in text:
        #     if word in line

    @staticmethod
    def get_column_number(filename):
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
            first_row = next(reader)
            num_cols = len(first_row)
            print(num_cols)

    @staticmethod
    def get_specific_column_number(word, filename):
        file = open(filename,"r")
        list = []

        for line in file:
            fields = line.split(" ")
            list.append(fields)

        for i in range(0, len(list)):
            j = 0
            for item in list[i]:
                if word in item:
                    return j
                j += len(item) + 1



