#요소 추가, 제거 및 정렬
'''np.sort(), np.concatenate()'''

import numpy as np

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

#오름차순으로 숫자를 빠르게 정렬할 수 있다.
print(np.sort(arr))
#np.sort()함수를 호출할 때 축, 종류, 순서를 지정할 수 있다.
'''
(sort종류)
argsort      : 지정된 축을따른 간접 정렬
lexsort      : 여러 키에 대한 간접적인 안정적인 정렬
searchsorted : 정렬된 배열에서 요소를 찾는 정렬
partition    : 부분 정렬
'''

#연쇄시키기(합치기)
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))

#또는

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))
#배열에서 요소를 제거하려면 인덱싱을 사용하여 유지하려는 요소를 선택하는 것이 간단하다.
