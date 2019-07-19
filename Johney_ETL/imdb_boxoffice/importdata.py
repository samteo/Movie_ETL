import csv

with open("imdb2010.csv","r",encoding="utf-8") as data:
    rows = csv.reader(data)
    print(rows)
    print(type(rows))
