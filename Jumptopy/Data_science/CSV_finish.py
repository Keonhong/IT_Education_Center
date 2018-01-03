import csv
import math

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data = list(csv.reader(infile))

def row_float_total(row_name): #float형 총합함수
    score = 0
    for i in get_csv_rowInstance(row_name):
        score += float(i)
    return score

def Aver(row_name): #평균함수
    return row_float_total(row_name)/float(236)

def Max(row_name): #최댓값함수
    max_val = max(list(map(float,get_csv_rowInstance(row_name))))
    return max_val

def Min(row_name): #최솟값함수
    min_val = min(list(map(float,get_csv_rowInstance(row_name))))
    return min_val

def Standard_Deviation(row_name): #편차함수
    return math.sqrt(row_name)

def Variance(row_name): #분산 함수
    average = Aver(row_name)
    variance = 0
    for i in row_name:
        variance += (average - int(float(i)))**2
    return variance/float(len(row_name))

def get_csv_rowInstance(row_name): #row_instance 함수
    row_instance = []
    row_index = data[0].index(row_name)
    for row in data[1:]:
        row_instance.append(row[row_index])
    return row_instance

def print_row(row_instance, type = 'int'): #row 각 형의따라 변환함수
    if type == 'int':
        list(map(int,row_instance))
    elif type == 'float':
        list(map(float,row_instance))
    for row_element in row_instance:
        print(row_element)

def print_col(col_instance): # col_instance 함수
    for col_element in col_instance:
        print(col_element)

def get_csv_colInstance(primary_key): # col-primary 함수
    for col in data[1:]:
        if col[0] == primary_key:
            return col
        else: continue

while True:
    q = int(input("**Access 데이터 유형선택 (1.행 2.열 3.총합 4.평균 5.최댓값 6.최솟값 7.편차 8.분산 9.표준편차 10.정렬 11.종료):"))
    if   q == 1:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_rowInstance(Q):
            print(i)
    elif q == 2:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_colInstance(Q):
            print(i)
    elif q == 3:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_rowInstance(Q):
            print(i,end=' ')
        print('\n''입력한 value의 총합은 ' + '%g'% row_float_total(Q) + '입니다.')
    elif q == 4:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_rowInstance(Q):
            print(i,end=' ')
        print('\n''입력한 value의 평균은 '+ str(Aver(Q))+' 입니다.')
    elif q == 5:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_rowInstance(Q):
            print(i,end=' ')
        print('\n''입력한 value의 최댓값은 ' +'%g'% Max(Q)+' 입니다.')
    elif q == 6:
        Q = input("행의 value를 입력해주세요: ")
        for i in get_csv_rowInstance(Q):
            print(i,end=' ')
        print('\n''입력한 value의 최솟값은 ' +'%g'% Min(Q)+' 입니다.')
    elif q == 7:
        Q = input("행의 value를 입력해주세요: ")
        print('입력한 value의 편차값은 '+'%g'% Standard_Deviation(Q)+' 입니다.')
    elif q == 8:
        Q = input("행의 value를 입력해주세요: ")

    elif q == 9:
        Q = input("행의 value를 입력해주세요: ")

    elif q == 10:
        Q = input("행의 value를 입력해주세요: ")

    else:
        print("프로그램을 종료합니다.")
        break