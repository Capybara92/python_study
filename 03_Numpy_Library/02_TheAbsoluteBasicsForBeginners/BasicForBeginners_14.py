#행렬 만들기

import numpy as np

#python리스트의 리스트를 전달하여 NumPy로 표시 할 2D배열(또는 "행렬")을 만들 수 있다.
data = np.array([[1, 2], [3, 4]]) #2D배열

print(data)

#인덱싱 및 슬라이싱 작업은 행렬을 조작할 때 유용하다.
print(data[0, 1])    #[행, 열]
print(data[1:3])     #[행, 열]
print(data[0:2, 0])  #[행, 열]

#벡터를 집계한 것과 동일한 방식으로 행렬을 집계 할 수 있다.
print(data.max())
print(data.min())
print(data.sum())

#행렬의 모든 값을 집계 할 수 있으며 axis매개 변수를 사용하여 열 또는 행에서 집계 할 수 있다.
print(data.max(axis=0)) # ↓(행)
print(data.max(axis=1)) # →(열)

#행렬을 만든 후에는 크기가 같은 두 개의 행렬이있는 경우 산술연산자를 사용하여 행렬을 더하고 곱할 수 있다.
data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(data + ones)

#크기가 다른 행렬에 대해 이러한 산술 연산을 수행 할 수 있지만,
#하나의 행렬에 열이나 행이 하나만있는 경우에만 가능하다.
#이 경우 NumPy는 작업에 브로드캐스트 규칙을 사용한다.
data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)

# ※NumPy가 N차원 배열을 출력할 때 마지막 축은 가장 빠르게 반복되는 반면 첫 번째 축은 가장 느리다.
