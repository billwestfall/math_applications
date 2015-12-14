# from http://stackoverflow.com/questions/1871524/convert-from-json-to-csv-using-python

import json
import csv

f = open("sonar_block.json", 'r')
data = json.load(f)
f.close()

f = open("sonar_block.csv", 'w')
csv_file = csv.writer(f)
for item in data:
    csv_file.writerow(item)

f.close()
