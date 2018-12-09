
# For write data in csv file

import csv
with open (r"E:\python-examples\myfile.csv",'w') as csvfile:
    fieldnames = ["Name","Age","Gender"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'ABC','Age':'20','Gender':'Male'})
    writer.writerow({'Name':'PQR','Age':'22','Gender':'Male'})