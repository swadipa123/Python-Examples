# create new csv file

import csv
with open (r"E:\python-examples\file.csv",'w') as csvfile:
    fieldnames = ["Name","Age"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'aaa','Age':'20'})
    writer.writerow({'Name':'bbb','Age':'22'})