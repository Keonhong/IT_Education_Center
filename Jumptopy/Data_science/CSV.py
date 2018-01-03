import csv

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data = list(csv.reader(infile))

countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': "+str(countParticipantsIndex))

countParticipants = []
# index = 0

for row in data[1:]:
    countParticipants.append(int(row[countParticipantsIndex]))

# COUNT CITIZEN STATUS TOTAL
# countCitizenIndex = data[0].index("COUNT CITIZEN STATUS TOTAL")
# print("The index of 'COUNT CITIZEN STATUS TOTAL': "+str(countCitizenIndex))
#
# countCitizen_ = []
#
# for row in data[1:]:
#     countCitizen_.append(int(row[countCitizenIndex]))

# countFemale = data[0].index("COUNT FEMALE")
# print("The index of 'COUNT FEMALE': "+str(countFemale))
#
# countFemale_ = []
#
# for row in data[1:]:
#     countFemale_.append(int(row[countFemale]))
# for x in countFemale_:
#     print(x)
#
# get_csv_rowinstance(row_index)
# def Header_row_index():
#     for row in data