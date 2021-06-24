import json
import re

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

def csv_to_json(csv_path, json_path):

    with open (csv_file_path, 'r') as csv_file:
        readlines=csv_file.readlines()
        lists=[]
        for line in readlines:
            split_list=line.rstrip("\n").replace('|', ',')
            list=re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', split_list)
            lists.append(list)

        keys=lists[0]
        values=lists[1:]
        readmissions=[dict(zip(keys, l)) for l in lists]

        for item in readmissions:
            for key, value in item.items():
                key, value.strip()
                try:
                    item[key] = int(value)
                except ValueError:
                    item[key] = str(value)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(readmissions, indent=4))

csv_to_json(csv_file_path, json_file_path)
