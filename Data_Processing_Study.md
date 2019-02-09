# [ chapter 1 ] Pythonic codes

chapter 1에서는 파이썬에서 Data Processing작업에 있어서 가장 자주 사용되고 범용적으로 사용되는

Pythonic codes 에대해서 학습해보겠다.  pythonic codes 에는 다음과 같은 것들이있다.

 ### [ INDEX ]

> 1. Split
> 2. Join
> 3. List Comprehension
> 4. Enumerate
> 5. Zip
> 6. Lambda
> 7. MapReduce
> 8. 



## 1. Split 기법

Split 기법은 간단하다 문장으로 되어있는 데이터를 어떠한 기준을 토대로 나누어 배열로 저장하는 방식이다.

다음의 소스코드를 보자

```{python}
data = 'one two three'
data_s = data.split( )
print(data_s)
```

다음 소스코드에서 보면 data 라는 변수에다가 'one two three' 라는 문장을 기입하고

그 기입된 값을 공백을 중심으로 끊은 다음에 data_s 라는 변수에 넣어주면 파이썬 언어 특성상 배열로 만들어준다



#### (Advanced) unpacking 기법

unpacking 기법이란 split으로 나눈 요소들을 각각 변수지정함을 의미한다. 즉 이렇게 사용된다.

```{python}
data = 'one two three'
a, b, c = data.split( )
print(a)
print(b)
print(c)
```

다음 소스코드를 보면 split 기법으로 one과 two 와 three 를 나눠준다음 각각 차례대로 a, b, c에 담아 주었다

이 기법을 사용하면 각 배열요소를 하나의 객체로 사용하기 용이하다.



## 2. Join 기법

Join 기법은 이전 split으로 나눈 배열목록 이나 혹은 떨어져있는 배열요소를 어떤 '표시'를 중심으로

이어붙여주는 기법이다. 즉 split의 반대 기법이라고 볼 수 있다

```{python}
data = ["red", "blue", "yellow"]
data_j = '-'.join(data)
print(data_j)
```

다음 소스코드를 보면 data에 3가지 요소 "red", "blue", "yellow" 가 data_j 에서 '-'를 중심으로 연결되어서

data_j 에는 'red-blue-yellow' 가 들어감을 알 수 있다.



## 3. List Comprehension

파이썬에서 가장 많이 사용되는 기법으로 

"기존의 리스트를 사용하여 간단히 다른 리스트를 만드는 기법" 이다.

가장 기본적인 List comprehension 방법은 append 와 for loop 를 사용한 방법으로 다음과 같다.

```{python}
data = []
for i in range(10):
    data.append(i)
print(data)
```

위 방법을 사용하면 [0,1,2,3,4,5,6,7,8,9] 의 data라는 이름의 배열이 완성된다. 하지만 더 간단하게 만드는 방법이있다. 그 방법은 다음 소스코드와 같다.

```{python}
data = [i for i in range(10)]
print(data)
```

위 방법을 사용해도 똑같이 [0,1,2,3,4,5,6,7,8,9] 의 data 라는 이름의 배열이 생성된다. 이 방법의 구조를 살펴보면

**배열명** = [**배열요소의 형태** *for loop*]  이다.

이때 만약에 자신이 원하는 조건을 만족하는 값만 배열요소로 사용하고 싶다면 **Filter**기법을 사용한다.

```{python}
data = [i for i in range(10) if(i % 2 == 0)]
print(data)
```

다음 방법을 사용하면 if절 뒤에 조건을 만족하는 값들만 배열 요소로 사용하게 된다.

즉 [0,2,4,6,8]의 data 배열이 완성된다. 



다음으로 알아볼 방법은 차원 배열 List Comprohension 에 대해서 학습해보자.

다음 소스코드를 보자

```{python}
data_1 = "ABC"
data_2 = "123"
result = [i+j for i in data_1 for j in data_2]
print(result)
```

다음 소스코드는 위에서 알아본 것 과 같이 발전된 List comprehension 방법을 통해서 만들어졌다.

다만 형태를 보면 마치 2차원 배열의 형태를 띈것 같다. 하지만 다음 소스코드의 결과 값은 다음과 같다.

​							**['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']**

왜 그렇게 될까? 그 이유는 앞에서부터 차례대로 실행 되기 때문이다. 

```{python}
data_1 = "ABC"
data_2 = "123"
result = []
for i in data_1:
    for j in data_2:
        result.append(i+j)
print(result)
```

즉 위의 두 소스코드는 같은 셈이다.

그렇다면 2차원 배열의 형태로 만들려면  어떻게 해야할 까? 간단하다 대괄호 하나 더 쳐주면 된다. 즉

```{python}
data_1 = "ABC"
data_2 = "123"
result = [ [i+j for i in data_1] for j in data_2]
print(result)
```

다음과 같은 소스코드를 실행하면 아래와 같은 결과가 나온다.

​						**[ ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'] ]**

즉 무엇이냐 대괄호를 묶어주게 되면 뒤의 루프 먼저 기준이 된다. 따라서 뒤의 루프를 기준으로

j가 1일때 A, B, C  >  j가 2일때 A, B, C >  j가 3일때 A, B, C 

이렇게 된다는 것이다 헷갈리니 꼭 알아 두도록 하자.



## 4. Enumerate

이 기법은 List의 요소를 추출 할때 INDEX번호를 붙여서 추출하는 기법을 말한다. 다음 소스코드를 보자.

```{python}
List = ['zero', 'one', 'two', 'three']
for i , v in enumerate(List):
    print(i, v)
```

다음 소스코드를 실행하면 0 zero 1 one  2 two 3 three 로 출력된다. 



## 5. Zip

이 기법은 두개의 List를 병렬적으로 나타낼 때 사용하는 방법으로 같은 INDEX에 위치한 요소끼리 병렬출력한다.

```{python}
list_a = ['A', 'B', 'C']
list_b = ['ㄱ', 'ㄴ', 'ㄷ']
for i, j in zip(list_a, list_b):
    print(i+j)
```

다음 소스코드를 실행하면 Aㄱ Bㄴ Cㄷ 이 출력된다 즉 같은 INDEX의 요소끼리 병렬 출력하는 것이다.

또한 앞서 배운 Enumerate 와 함께사용하여 

```{python}
list_a = ['A', 'B', 'C']
list_b = ['ㄱ', 'ㄴ', 'ㄷ']
for v, (i, j) in enumerate(zip(list_a, list_b)):
    print( v , i , j)
```

다음과 같이 사용할 수 있다. 다만 매개변수 선언중 소괄호를 꼭 쳐야한다는 것을 잊지말자