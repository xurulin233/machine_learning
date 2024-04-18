import csv

filename = "example.csv"

with open(filename, "r", encoding="GB2312") as csvfile:
    csvreader=csv.reader(csvfile)

    for row in csvreader:
        print(row)
