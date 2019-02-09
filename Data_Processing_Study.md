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

split 기법은 간단하다 문장으로 되어있는 데이터를 어떠한 기준을 토대로 나누어 배열로 저장하는 방식이다.

다음의 소스코드를 보자

```{python}
data = 'one two three'
data_s = data.split( )
print(data)
```

다음 소스코드에서 보면 data 라는 변수에다가 'one two three' 라는 문장을 기입하고

그 기입된 값을 공백을 중심으로 끊은 다음에 data_s 라는 변수에 넣어주면 파이썬 언어 특성상 배열로 만들어준다



