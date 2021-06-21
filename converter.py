import csv
import json

csv_file_path='readmissions_df.csv'
json_file_path='readmission.json'

readmissions={}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        i=rows['i']
        readmissions[i]=rows

with open(json_file_path, 'w') as json_file:
    json_file.write(json.dumps(readmissions, indent=4))


