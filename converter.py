import csv
import json

csv_file_path='readmissions_df.csv'
json_file_path='readmission.json'

def csv_to_json(csv_path, json_path):

    readmissions=[]

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            readmissions.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(readmissions, indent=4))

csv_to_json(csv_file_path, json_file_path)
