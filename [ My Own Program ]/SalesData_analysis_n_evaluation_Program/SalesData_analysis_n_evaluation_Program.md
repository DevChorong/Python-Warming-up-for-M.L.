## 한 주간 판매량 측정하여 데이터분석 및 평가하는 프로그램

### 소스 코드 (Python)

```{python}
# 파일 열기
f = open("C:\Cafe_sale_data.txt", 'r')
data = []

cnt_name = 0
cnt_line = 0

#줄별로 data라는 배열에 배정하기
while True:
    line = f.readline()
    data.append(line)
    if not line: break
    cnt_line += 1

#배정받은 배열안에서 문자열 나누기
data = [data[i].split() for i in range (cnt_line)]
print("============== 데이터 파일입니다 ==============")
for i in range(cnt_line):
    print(data[i])
print("==============================================\n")
#요일 데이터 추출
data_day = data[0]
del data[0]

#품명 데이터 추출
cnt_name = cnt_line - 1
data_name = []

for i in range (cnt_name):
    data_name.append(data[i][0])
    del data[i][0]

print("판매되는 제품의 갯수는 {0}개 입니다.\n".format(len(data_name)))
#요일데이터 및 품명데이터 출력 후 자료에서 삭제

print("요일 데이터 입니다 : {0}".format(data_day))
print("품명 데이터 입니다 : {0}\n".format(data_name))

#요일별 판매량 총합 데이터 추출
total_day = [0 for i in range(5)]

for i in range(5):
    for j in range(cnt_name):
        total_day[i] += int(data[j][i])

print("순수 요일별 판매량 합계(정수)입니다 : {0}".format(total_day))

#제품별 판매량 총합 데이터 추출
total_name = [0 for i in range(cnt_name)]

for i in range(cnt_name):   #제품 카테고리 수
    for j in range(5):      #요일 수
        total_name[i] += int(data[i][j])

print("순수 제품별 판매량 합계(정수)입니다 : {0}\n". format(total_name))

#DIctionary 만들기
dic_data_day = {i : data_day[i] for i in range(5)}
dic_data_name = {i : data_name[i] for i in range(cnt_name)}
dic_total_n_day = {i : total_day[i] for i in range(5)}
dic_total_n_name = {i : total_name[i] for i in range(cnt_name)}

#가장 잘팔린 것과 그 요일 구하기
def sorting (cnt, data):
    for i in range(cnt):
        for j in range(cnt):
            if (data[i] > data[j]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

#자료들 정렬하기
sorting(cnt_name, total_name)
sorting(5, total_day)

def find (data, dict):
    dic_num = 0
    while True:
        dic_num += 1
        if(dict[dic_num] == data):break
    return dic_num

dic_num_name = find(total_name[0],dic_total_n_name)
dic_num_day = find(total_day[0], dic_total_n_day)

print("<< 한 주 평가 >> ")
print("이번주 제품 중 가장 잘 팔린 것은 {0}(이)고 이 제품이 가장 잘팔린 요일은 {1}요일입니다. ".format(dic_data_name[dic_num_name], dic_data_day[dic_num_day]))


f.close()
```

#### 실행 결과 사진

![](DataProcessing-Study/img/SalesData_analysis_n_evaluation_Program.JPG)
