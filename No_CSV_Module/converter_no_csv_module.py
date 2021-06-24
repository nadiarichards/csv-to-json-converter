import json
from shlex import shlex
from itertools import chain

csv_file_path='readmissions_df.csv'
json_file_path='readmissions2.json'

readmissions=[]

# def csv_to_json(csv_path, json_path):

# file=open(csv_file_path)
data=[]

with open (csv_file_path, 'r') as csv_file:
    readlines=csv_file.readlines()
    lists=[line.split(",") for line in readlines]
    # new_list=[word for line in lists for word in line.split(",")]
    # for line in lists:
    #     data.extend(line.split(","))
    # for i in lists:
    #     data.append(i[0].split(","))
    # data=[i[0].split(",") for i in lists]
    print(lists[1][3])

    # for row in lists:
    #     data.append(row)
            
    #     # for item in data:
    #     #     for key, value in item.items():
    #     try:
    #         row[key] = int(value)
    # .replace("\n", "")
    #     except ValueError:
    #         row[key] = str(value)

    print(data[0])
    #     words = str(list).split(",")
    #     print(words[0])
    # no need for readlines; the file is already an iterable of lines
    # also, using generator expressions means no extra copies
    # iterate tuples, instead of two separate iterables, so no need for zip
    # print(new_list)

# # headers
# headers = file.readline().strip().split(',')
# print(headers)

# lines=file.readlines()[1:]
# line_count=0
# line_data=[]

# for line in lines:
#     line_count+=1
#     clean_lines=line.strip().split(',')
#     line_data.append(line)
#     print(line_data[1])

# readmissions=[dict(zip(headers, row)) for row in clean_lines]
# print(readmissions)

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

# data=[]
line_count=0

# for line in file.readlines()[1:]:
#     line.readline().split(',').strip()
#     line_count+=1
#     data.append(line)
        
# print(line_count)
# print(data)

# list_of_lists=[]
# data = file.readlines()
# res = [i.strip("[]").split(", ") for i in data]

# lists = [i.strip("\n").split(", ") for i in res]
# for i in res:
#     for j in i:
#         j.split(',').strip("\n")
#     i.strip("[]").split(", ").replace("/n", "")
        # print(i)
# print(res[0])

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
