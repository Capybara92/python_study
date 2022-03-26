#인덱싱 및 슬라이싱

#Python의 리스트을 슬라이싱하는 것과 동일한 방법으로 NumPy배열을 인덱싱하고 슬라이싱할 수 있다.

import numpy as np

data = np.array([1, 2, 3])

#예
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])

#특정조건을 충족하는 배열에서 값을 선택하려는 경우 NumPy를 사용하면 간단하다.
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#5보다 작은 배열의 모든값을 쉽게 출력할 수 있다.
print(a[a < 5])

#조건을 사용하여 배열을 인덱싱 할 수도 있습니다.
five_up = (a >= 5)
print(a[five_up])

#2로 나눌 수 있는 요소를 선택할 수 있다.
divisible_by_2 = a[a%2==0]
print(divisible_by_2)

#연산자 &와 |연산자를 사용하여 두 가지 조건을 충족하는 요소를 선택할 수 있다.
c = a[(a > 2) & (a < 11)]
print(c)

#값이 특정조건을 충족하는지 여부를 지정하는 리턴값을 부울로 하기 위해서 논리연산자(&, |)로 만들 수 있다.
#이것은 이름이나 다른 범주 값을 포함하는 배열에 유용 할 수 있다.
five_up = (a > 5) | (a == 5)
print(five_up)

#5미만인 요소의 인덱스들을 출력하는 데 사용할 수 있다.
b = np.nonzero(a < 5)
print(b) #(array([0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3], dtype=int64))
#첫 번째 배열은 이러한 값이있는 행 인덱스를 나타내고,
#두 번째 배열은 값이있는 열 인덱스를 나타낸다.

#요소가있는 좌표 리스트을 생성하려면 배열을 압축하고 좌표 리스트을 반복하여 출력할 수 있다.
list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)

#찾고있는 요소가 배열에 존재하지 않으면 반환된 인덱스 배열은 비어있다.
not_there = np.nonzero(a == 42)
print(not_there)
