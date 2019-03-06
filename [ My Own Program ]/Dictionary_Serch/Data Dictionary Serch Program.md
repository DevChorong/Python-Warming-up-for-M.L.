# Data Dictionary Serch Program

#### 소스코드

```{Python}
# Project Name : Dictionary _ serch
# Function : if you open the text file program can serch the word in text
# Data : 2019 - 03 - 07 (Thursday)

# 파일 열기
file_address  = "C:\Data.txt"
f = open("{0}".format(file_address))

# Dictionary Serching 함수 정의
def serch (serch_code, dict, count):
    find_code = -1
    for i in range(count):
        if(serch_code == dict[i]):
            find_code = i

    return find_code

# 자료를 저장할 배열과 딕셔너리 배열 그리고 자료의 갯수 Default 값 선언
data =[]
dictionary = {}
count = 0

# 연 파일을 자료배열에 저장
while True:
    line = f.readline()
    if not line: break

    line = line.rstrip('\n')
    data.append(line)
    count += 1

# 자료배열을 토대로 딕셔너리 만들기
for i in range(count):
    dictionary[i] = data[i]

# 실행 코드

code = input("찾으실 단어를 입력하세요 : ")
serch_num = serch(code, dictionary, count)

if(serch_num != -1):
    print("찾으시는 단어는 자료의 {0}번째에 있습니다.".format(serch_num + 1))

elif(serch_num == -1):
    print("찾으시는 단어는 자료에 존재하지 않습니다.")

f.close()
```

#### 실행결과

