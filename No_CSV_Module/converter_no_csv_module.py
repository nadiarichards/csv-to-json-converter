import json
from shlex import shlex

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

readmissions=[]

# def csv_to_json(csv_path, json_path):

file=open(csv_file_path, 'r')
# headers
header = file.readline()
print(header)
lines=file.readlines()[1:]
# header=next(lines)
line_count=0
line_data={}
# field_names=lines[]
# print(header)
for line in lines:
    line_count+=1
    # stripped_line=line.join([i for i in lines]).replace("/n", "").replace(" "" ", "")
    #strips the newline character
    # print("Line{}: {}".format(line_count, line.strip()))
    # print(line)

#     key = line
#     line_data[key]=line
#     readmissions.append(line_data)
# print(readmissions)


    # if headers:
    #     columns = next(reader)

    # for line in open(csv_file_path, 'r').readlines()[1:]:

# Words is the last line of the doc as a list of objects[]
    #   words=line.replace('\n', '').split(',')
      # line_count=(len(line))
    #   line_count=0
    #   line_data={}
      # print(line[0])

        # line = line.rstrip()
        # line = line.replace('"', '')
        # items = line.split(',')

      # key = words[0]
      # for key in line:
      #   values=words[1], words[2], words[3], words[4], words[5]
      #   line_data[key] = values
      # readmissions.append(line_data)

      # print(words[0])

    #   if line_count == 0:
    #       print ("1st line", line)
    #       line_count += 1
    #   else:
    #       print ("next line")
    #       line_count += 1
    #       print(line)
    # print(line_count)

    #   for i in range(line_count):
    #         # set key names
    #     if line_count!=0:
    #       line_key = line[i].lower()
    #     else: 
    #       line_key = i
    #       print(line)
    #         # set key/value
    #     line_data[line_key] = line[i]
    #       # add data to json store 
    # readmissions.append(line_data)

# def string_and_integer()

#     for item in readmissions:
#         for key, value in item.iteritems():
#             try:
#                 item[key] = int(value)
#             except ValueError:
#                 item[key] = str(value)



#     with open(json_file_path, 'w', encoding='utf-8') as json_file:
#         json_file.write(json.dumps(readmissions, indent=4))

# csv_to_json(csv_file_path, json_file_path)
