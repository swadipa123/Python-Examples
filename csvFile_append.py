# for append the data in the file


import csv
with open(r'E:\python-examples\myfile.csv','a') as csvfile:
    newfile = csv.writer(csvfile)
    newfile.writerow(['xyz','22','female'])
    newfile.writerow(['seeta','21','female'])