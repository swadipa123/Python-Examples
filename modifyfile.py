# append the data in the file

import csv
with open(r'E:\python-examples\mycopy.csv','a') as csvfile:             # new file  which has data already
    filewriter = csv.writer(csvfile)
    with open(r'E:\python-examples\file.csv','r') as infile:          #existing file  which(data) going to append to another file
        filereader= csv.reader(infile)
        for row in filereader:
            filewriter.writerow(row)