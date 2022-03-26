#기존 데이터에서 배열을 만드는 방법
'''slicing and indexing, np.vstack(), np.hstack(), np.hsplit(), .view(), copy()'''

import numpy as np

#기존 배열의 섹션에서 새로운 배열를 쉽게 만들 수 있다.
#배열이 있다고 가정 해 보자.
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

#배열를 슬라이스 할 위치를 지정하여 언제든지 배열의 섹션에서 새로운 베열를 만들 수 있다.
arr1 = a[3:8] #인덱스 위치 3에서 인덱스 위치 8까지 배열의 섹션을 가져온다.
print(arr1)


#두 개의 기존 배열를 수직 및 수평으로 쌓을 수도 있다.
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

print(np.vstack((a1, a2))) #vstack
print(np.hstack((a1, a2))) #hstack


#배열을 분할한다.
x = np.arange(1, 25).reshape(2, 12)
#동일한 모양의 3개 배열로 분할하려면 다음을 실행한다.
print(np.hsplit(x, 3)) #hsplit

#세 번째와 네 번째 열 이후에 배열을 분할하려면 다음을 실행한다.
print(np.hsplit(x, (3, 4)))
print()


#view메서드를 사용하여 원래 배열에서 같은 데이터로 보이는 새로운 배열객체를 만들 수 있다. (a shallow copy)
#view는 중요한 NumPy의 개념이다.
#NumPy함수와 인덱싱 및 슬라이싱과 같은 작업은 가능할 때마다 view를 반환한다.
#이것은 메모리를 절약하고 더 빠르다. (데이터를 복사 할 필요가 없다)
#그러나 이것을 인식하는 것이 중요하다.
#view에서 데이터를 수정하면 원래 배열도 수정된다.


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
print(b1)
#a배열을 슬라이싱하고,
b1[0] = 99
print(b1)
#b1의 처음 요소를 변경하여 b1배열을 만듬.
print(a)
#그러면 a배열에서 해당요소도 변경된다.

#copy메서드를 사용하면 배열과 해당 데이터의 전체 복사본이 만들어진다. (a deep copy)
b2 = a.copy()
print(b2)
