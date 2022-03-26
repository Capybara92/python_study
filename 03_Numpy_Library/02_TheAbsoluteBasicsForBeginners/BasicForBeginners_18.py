#배열을 뒤집는 방법
'''np.flip()'''

#NumPy의 np.flip()함수를 사용하면 축을 따라 배열의 내용을 뒤집을 수 있다.
#np.flip()함수를 사용할 때 반전할 배열과 축을 지정해야한다.
#축을 지정하지 않으면 NumPy는 입력 배열의 모든축을 따라 내용을 반전한다.

import numpy as np

#1D 배열 반전
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)
print('Reversed Array: ', reversed_arr)

#2D 배열 반전
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d) #모든 행과 모든 열의 내용을 반전
print(reversed_arr)

#2D 배열 행만 반전 ↓
reversed_arr_rows = np.flip(arr_2d, axis=0)
print(reversed_arr_rows)

#2D 배열 열만 반전 →
reversed_arr_columns = np.flip(arr_2d, axis=1)
print(reversed_arr_columns)

#한 열 또는 한 행의 내용만 반전 할 수도 있다.
arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)

#인덱스 위치에서 열을 반전 할 수도 있다.
arr_2d[:,1] = np.flip(arr_2d[:,1]) #인덱스 위치1 (두 번째 열)에서 열을 반전
print(arr_2d)
