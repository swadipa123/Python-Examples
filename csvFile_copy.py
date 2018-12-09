# copy the data of one csv file to another csv file

import csv
with open(r'E:\python-examples\mycopy.csv','w') as csvfile:
    filewriter = csv.writer(csvfile)
    with open(r'E:\python-examples\myfile.csv','r') as infile:
        filereader= csv.reader(infile)
        for row in filereader:
            filewriter.writerow(row)