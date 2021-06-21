# import csv
import json
from shlex import shlex

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

def csv_to_json(csv_path, json_path):

    readmissions=[]
    # if headers:
    #     columns = next(reader)

    for line in open(csv_file_path, 'r').readlines()[1:]:

        line=line.replace('\n', '').split(',', '|')
        line_data={}
#         for i in range(len(line)):
#           # set key names
#           if headers:
#             line_key = columns[i].lower()
#           else: 
#             line_key = i
#           # set key/value
#           line_data[line_key] = line[i]
#         # add data to json store 
#         readmissions.append(line_data)

# def string_and_integer()

#     for item in readmissions:
#         for key, value in item.iteritems():
#             try:
#                 item[key] = int(value)
#             except ValueError:
#                 item[key] = str(value)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(readmissions, indent=4))

csv_to_json(csv_file_path, json_file_path)
