import csv
import re


class Navigate:
    # def static navigate_file():
    #     #  first number is the line and the second is the indentation
    #     with open('sample.txt') as file:
    #         for mark, line in enumerate(file.readlines()):
    #             print(mark, len(re.findall("^ *", line)[0]))
    #
    #
    # def static get_column():
    #     with open("sample.txt") as file:
    #         # splits a files in line
    #         lines = file.readlines()
    #
    #     # extracts the stuff in the column
    #     for line in lines[2:]:
    #         columns = line.split()
    #         print(columns[1])

    # away to get the line number of something we want
    @staticmethod
    def get_line(word='Why', filename="sample.txt"):

        with open(filename) as file:
            for num, line in enumerate(file, 1):
                if word in line:
                    return num

    @staticmethod
    def get_column_number(filename="sample.txt"):
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
            first_row = next(reader)
            num_cols = len(first_row)
            print(num_cols)

    @staticmethod
    def get_specific_column_number(word="do", filename="sample.txt"):
        file = open(filename,"r")
        list = []
        for line in file:
            fields = line.split(" ")
            list.append(fields)

        # print(list)
        for i in range(0, len(list)):
            j = 1
            for item in list[i]:
                if word in item:
                    return j
                j += 1




