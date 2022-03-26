#기본 배열 연산
#배열의 더하기, 빼기, 곱하기, 나누기

import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)

#더하기
print(data + ones)

#빼기
print(data - ones)

#곱하기
print(data * data)

#나누기
print(data / data)


a = np.array([1, 2, 3, 4])
#배열에서 요소의 합계
print(a.sum())


#2D배열에 행 이나 열을 추가하려면 축을 지정한다.
b = np.array([[1, 1], [2, 2]])

#행을 합산 할 수 있다.
print(b.sum(axis=0))
#열을 합산 할 수 있다.
print(b.sum(axis=1))