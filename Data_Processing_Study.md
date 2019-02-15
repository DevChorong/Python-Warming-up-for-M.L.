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
> 7. Map & Reduce
> 8. Asterisk
> 9. Linear Algebra Codes



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

Zip은 쉽게 말해서 같은 INDEX에 있는 값들을 뽑아주는 것이다.

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



## 6. Lambda

Lambda함수라는 것은 함수이름 없이 함수처럼 쓸 수 있는 임시함수 이다. 사용방법은 다음 과 같다.

```{python}
f = lambda x,y : x + y
print(f(1,4))
```

간단하게 람다함수를 사용하여 덧셈을 하는 임시함수를 만들어 보았다.

(!) 다만 Python 3 부터는 권장하지는 않는다.



## 7. Map & Reduce

**Map function** 이란 Sequence 자료형(리스트나 튜플) 각 요소에 동일한 함수를 적용하는 것을 말한다. 

즉 다음 소스코드를 보자

```{python}
ex = [ 1, 2, 3, 4, 5]
f = lambda x : x**2
print(list(map(f,ex)))
```

Python 3 부터는 map 앞에 list를  붙여야 실행된 결과 값이 나온다.

Map 함수에도 필터를 적용할 수 있지만 반드시 조건을 만족하는 값 뿐만아니라 만족하지 않은 값까지 넣어준다

즉 다음 소스코드를 보자

```{python}
ex = [ 1, 2, 3, 4, 5]
print( list( map( lambda x : x**2 if(x%2==0) else x , ex ) ) )
```

조금 복잡해 보이지만 하나씩 풀어보자

map 이라는 함수는 2개의 인자값을 받는다. 

**map( function, sequence )**

이때 앞서 말한 것 처럼 python 3 부터는 map 앞에 list를 붙여줘야한다. 따라서

**list( map( function, sequence ) )**

이번 예제를 통해서 우리는 map에서 필터를 사요하는법을 배웠다 그위치는

**list( map( function *filter* , sequence ) )**

따라서 이에 하나하나 대입해보면 위와 같은 소스코드를 이해 할 수 있다.



**reduce function** 이란 차례로 옆으로 옆으로 자료형 요소를 함수에 적용하는 것을 말한다.

다음 소스코드를 보자

```{python}
from functools import reduce
print(reduce(lambda x, y : x + y , [1,2,3,4,5] ))
```

위 소스코드를 실행하면 15가 출력된다. 

작동원리를 살펴보면 x, y 에처음에 1과 2가 들어간다 그럼 결과는 3

그다음 x, y 에는 전의 결과 3과 다음 요소 3이 들어간다. 그럼결과는 6

그다음 x, y 에는 전의 결과 6과 다음 요소 4가 들어간다. 그럼결과는 10

그다음 x, y 에는 전의 결과 10와 다음 요소 5가들어간다. 그럼결과는 15

따라서 결과는 5가 된다. 이를 통해서 펙토리얼 함수를 만들 수 있다.

```{python}
from functools import reduce
def factorial (n):
    return  reduce(lambda x, y : x * y , range(1,n+1))

print(factorial(5))
```

다음과 같이 쉽게 펙토리얼 함수를 만들 수 있다

(!) Map & reduce 함수는 지금 당장(python3) 은 사용하지 않지만 이후 pandas를 사용할때 사용된다.



## 8. Asterisk

파이썬에 특화된 기호(*)를 의미한다. * = 가변인자활용, **=키워드인자활용

Asterisk 는 나머지를 전부다 넘겨줄때 사용한다. 즉 다음 소스코드를 보자

```{python}
def asterisk_test (a, *args):
    print(a, args)
    print(type(args))
    
asterisk_test(1,2,3,4,5,6)
```

이렇게 되면 다른것은 보지말고 인자만 보면

a에 1만 대입되고 나머지 2,3,4,5,6은 튜플형태로 args로 대입된다.

```{python}
def asterisk_test (a, **kargs):
    print(a, kargs)
    print(type(kargs))
    
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
```

이렇게 되면 다른것은 보지말고 인자만 보게되면

a에 1만 대입되고 나머지에는 { 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6}으로 dict형태로 kargs에 대입된다.



```{python}
def asterisk_test (a, *args):
    print(a, args[0])
    print(type(args))
        
asterisk_test(1,(2,3,4,5,6))
```

다음과 같은 소스코드를 보자 다음 과 같은 소스코드에서는 (2,3,4,5,6)이 라는 튜플타입의 데이터가 args에 대입된다. 따라서 (2,3,4,5,6)을 보고싶다면 args[0]를 이용해서 0번째 요소만 봐야한다.



#### Asterisk Unpacking을 해보자!

기본적으로 unpacking 하는 방법은 다음과 같다.

```{python}
a, b, c = ([1,2],[3,4],[5,6])
print(a, b, c)
```

Asterisk 를 사용하여 unpacking 하는 방법은 다음과 같다.

```{python}
data = ([1,2],[3,4],[5,6])
print(*data)
```



## 9. Linear Algebra Codes

핵심 키워드 Vector / Matrix / Matrix addition / Matrix Product

가장 기본적인 Vector의 표현에 대해서 알아보자

```{python}
u = [2, 2]
v = [2, 3]
z = [3, 5]
result = []
for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])
    
print(result)
```

다만 다음과 같은 코드는 파이썬 답지못한다. 따라서 앞서 배운   List comprehension 기법들을 통해서 계산해보자. 다음 소스코드를 확인해보자

```{python}
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)]
print(result)
```

이렇게 하면 간단하게 계산 할 수 있다.

다음으로 알아볼 것은 Matrix Representation of Python 이다.

가장 간단하게 Matrix를 표현하는 방법은 List형식을 통해서 표현하는 방법이다.

그럼 선언한 Maxtrix끼리 계산하는 방법은 무엇일까?

```{python}
a = [[2,3],[4,5]]
b = [[6,7],[8,9]]

result = [[sum(row) for row in zip(*t)] for t in zip(a,b)]
print(result)
```

이 방법은 매우 복잡해 보이지만 천천히 풀어서 해석하면 쉽다.

뒤에서부터 살펴보자 

zip(a,b) 를 먼저 1회 실행하게 되면 a와 b의 첫번째 인덱스에 있는 아이 즉 a[0] 과 b[0] 이 병렬로 묶여 튜플 형태를 띈다. 따라서

> 1회 실행  || zip(a,b) => ( [2,3], [6,7] )
>
> 2회 실행  || zip(a,b) => ( [4,5], [8,9] )

이후에 이것들을 Asterisk를 통해서 가변인수로 받아주게 되면 튜플이 풀려 리스트형태를 띈다.

> 1회 실행 || (*t) => [2, 3] , [6, 7]
>
> 2회 실행 || (*t) => [4, 5] , [8, 9]

그다음 zip 으로 각각 같은 인덱스에 있는 값끼리 묶어주게 되면 다음과 같이 된다.

> 1회 실행 || zip(*t) => [2, 6] , [3, 7]
>
> 2회 실행 || zip(*t) => [4, 8] , [5, 9]

이후 이것들이 각각 row에 해당되어서 sum(row) 하게되면

> 1회 실행 || sum(row) => [8, 10]
>
> 2회 실행 || sum(row) => [12, 14]

따라서 result 를 출력하면 ( [8, 10], [12, 14]) 가 된다.



**(Advanced) Matrix Product**

Matrix Product 즉 행렬곱에 대해서 학습해보자 이것은 일종의 Trick 이니까 익혀두면 도움이 될 것이다.

```{python}
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
```



