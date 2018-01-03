import csv

with open('Demographic_Statistics_By_Zip_Code.csv',newline='')as infile:
    data = list(csv.reader(infile))

def get_csv_rowInstance(row_name):
    row_instance = []
    row_index = data[0].index(row_name)
    for row in data[1:]:
        row_instance.append(int(row[row_index]))
    return row_instance

def print_row(row_instance, type = 'int'):
    if type == 'int':
        for i in row_instance:
            print(int(i))
    elif type == 'float':
        for i in row_instance:
            print(float(i))
    elif type == 'str':
        for i in row_instance:
            print(i)

def print_col(col_instance):
    for i in col_instance:
        print(i, end=' ')

row_instance = input("write title: ")
print_row(row_instance)






# countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
# print("The index of 'COUNT PARTICIPANTS': "+str(countParticipantsIndex))

# countParticipants = []
# index = 0

# for row in data[1:]:
#     countParticipants.append(int(row[countParticipantsIndex]))


# colum = 열(가로) // row = 행(세로)
# get_csv_rowInstance(row_index)
# 입력:row_index
# 출력:row_instance
