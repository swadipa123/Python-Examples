# for read csv file

import csv
with open(r"E:\python-examples\myfile.csv",'r')as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'],row['Age'],row['Gender'])