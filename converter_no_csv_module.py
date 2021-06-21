# import csv
import json

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

def csv_to_json(csv_path, json_path):

    readmissions={}

    

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(readmissions, indent=4))

csv_to_json(csv_file_path, json_file_path)
