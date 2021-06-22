import csv
import json
import re
# import ast
# from itertools import islice

csv_file_path='readmissions_df.csv'
json_file_path='readmission.json'

def csv_to_json(csv_path, json_path):

    readmissions=[]
    # str_delimiter=(str_delimiter "|", ",")

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            row_data = re.split(',|', row)
            readmissions.append(row_data)
            
        for item in readmissions:
            for key, value in item.items():
                try:
                    item[key] = int(value)
                except ValueError:
                    item[key] = str(value)


    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(readmissions, indent=4))

csv_to_json(csv_file_path, json_file_path,)
