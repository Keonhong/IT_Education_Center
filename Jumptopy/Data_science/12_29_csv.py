import csv
import math

def get_csv_col_instance(primary_key):#내가 원하는 열(Column)을 찾고 싶을때
    Column_instance=[]
    col_index=0
    NotFound=True
    for i in range(len(data)):
        if primary_key in data[i]:
            col_index=i
            NotFound=False
            break
        else:
            NotFound=True

    for col in data[col_index]:
        if NotFound==True:
            print("Not Found '%s'"%primary_key)
            break
        Column_instance.append(col)
    return Column_instance

def get_csv_row_instance(row_name):
    row_instance=[]
    row_index=data[0].index(row_name)#행 데이터를 뽑아야되므로 header 컬럼중 찾는다.
    for row in data[1:]:
        row_instance.append(row[row_index])
    return row_instance

def Check_type(row_instance):#체크보단 컨버트 해주는 기능같다.
    Float_Flag=0
    for i in range(len(row_instance)):
        try:#리스트 문자형->리스트 정수형으로 변환
            row_instance[i]=int(row_instance[i])
        except ValueError:#하나라도 정수형 변환이 안된다면
            Float_Flag=1
            break

    if Float_Flag==1:#모두 실수형으로 변환시킨다.
        for j in range(len(row_instance)):
            row_instance[j]=float(row_instance[j])
    return row_instance

def My_Sum(data_list):
    My_Sum=0
    for i in range(len(data_list)):
        My_Sum+=data_list[i]
    return My_Sum

def My_Average(data_list):
    My_Average=My_Sum(data_list)
    My_Average/=len(data_list)
    return My_Average

def My_Max(data_list):
    My_Max=0
    for i in range(len(data_list)):
        if My_Max<data_list[i]:
            My_Max=data_list[i]
    return My_Max

def My_Min(data_list):
    My_Min=min(data_list)
    return My_Min

def My_Deviation(data_list):
    My_Deviation=0
    Average=My_Average(data_list)
    space="\t\t"
    print("표본\t\t편차")
    for i in range(len(data_list)):
        My_Deviation=data_list[i]-Average
        print(str(data_list[i])+space+str(My_Deviation))

def My_Standard_Deviation(data_list):# 표준편차
    Variance=My_Variance(data_list)
    My_Standard_Deviation=math.sqrt(Variance)
    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0
    Average=My_Average(data_list)

    for i in range(len(data_list)):# 제곱 **
        My_Variance+=((data_list[i])-Average)**2
    My_Variance/=len(data_list)
    return My_Variance

def My_Ascendant(data_list):#오름차순
    data_list.sort()
    for i in range(len(data_list)):
        print("%g "%data_list[i],end="")#'출력형식' 중 하나. C에도 있다.
    print()#실수면 %f 작으면 %e로 출력

def My_Descendant(data_list):#내림차순
    data_list.sort(reverse=True)
    for i in data_list:
        print("%g "%i,end="")
    print()

def print_row(row_instance):
    for row_element in row_instance:
        print("%s "%row_element,end="")
    print()

def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))

while True:
    print("1.행 2.열 3.종료 4.총합 5.평균 6.최대값 7.최소값")
    print("8.편차 9.표준편차 10.분산 11.오름차순 정렬 12.내림차순 정렬")
    case=int(input('Access 데이터유형 선택: '))
    if case==3:
        print('프로그램을 종료합니다.')
        break
    Access_key = input('Access Key를 입력하세요:')

    if case==1:#행
        print('행 데이터는 아래와 같습니다.')
        print_col(get_csv_row_instance(Access_key))
    elif case==2:#열
        print('열 데이터는 아래와 같습니다.')
        print_col(get_csv_col_instance(Access_key))
    elif case == 4:  # 합
        print_row(get_csv_row_instance(Access_key))
        row_data=Check_type(get_csv_row_instance(Access_key))
        print("총합: %s"%My_Sum(row_data))
    elif case == 5:  # 평균값
        print_row(get_csv_row_instance(Access_key))
        row_data=Check_type(get_csv_row_instance(Access_key))
        print("평균값: %s"%My_Average(row_data))
    elif case == 6:  # 최대값
        print_row(get_csv_row_instance(Access_key))
        row_data=Check_type(get_csv_row_instance(Access_key))
        print("최대값: %s"%My_Max(row_data))
    elif case == 7:  # 최소값
        print_row(get_csv_row_instance(Access_key))
        row_data=Check_type(get_csv_row_instance(Access_key))
        print("최소값: %s"%My_Min(row_data))
    elif case == 8:  # 편차
        print('편차(Deviation) 공식 : 표본값 - 평균')
        row_data=Check_type(get_csv_row_instance(Access_key))
        My_Deviation(row_data)
    elif case == 9:  # 표준편차
        print_row(get_csv_row_instance(Access_key))
        print("표준편차(Standard Deviation) 공식: √분산")
        row_data=Check_type(get_csv_row_instance(Access_key))
        print("표준편차: %s"%My_Standard_Deviation(row_data))

    elif case == 10:  # 분산
        print_row(get_csv_row_instance(Access_key))
        print('분산(Variance) 공식: ∑(표본-평균)**2/표본수')#**== 제곱
        row_data=Check_type(get_csv_row_instance(Access_key))
        print(My_Variance(row_data))
    elif case == 11: # 오름차순 정렬
        row_data=Check_type(get_csv_row_instance(Access_key))
        My_Ascendant(row_data)
    elif case == 12: # 내림차순 정렬
        row_data=Check_type(get_csv_row_instance(Access_key))
        My_Descendant(row_data)
    else:
        print('유효하지 않은 값 입력')