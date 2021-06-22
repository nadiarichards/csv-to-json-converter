import json
from shlex import shlex

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

def csv_to_json(csv_path, json_path):

    readmissions=[]
    line_count = 0
    # if headers:
    #     columns = next(reader)

    for line in open(csv_file_path, 'r').readlines()[1:]:

      words=line.replace('\n', '').split(',')
      line_data={}

    #     line = line.rstrip()
    #     line = line.replace('"', '')
    #     items = line.split(',')
    #     key = items[0]
    #     for key in line:
    #       values=items[1], items[2], items[3], items[4], items[5]
    #     line_data[key] = values
    # return readmissions

    #     if line_count == 0:
    #         print ("1st line")
    #         line_count += 1
    #     else:
    #         # print ("next line")
    #         line_count += 1
    # print(line)

      for i in range(len(words)):
            # set key names
        if line_count!=0:
          line_key = words[i].lower()
        else: 
          line_key = i
            # set key/value
        line_data[line_key] = words[i]
          # add data to json store 
    readmissions.append(line_data)

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
