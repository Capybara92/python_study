#1D 배열을 2D 배열로 변환하는 방법 (배열에 새 축을 추가하는 방법) 
'''np.newaxis, np.expand_dims'''

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

#np.newaxis를 사용하여 새 축을 추가 할 수 있다.
a2 = a[np.newaxis, :]
print(a2.shape)
print()


#np.newaxis를 사용하여 1D 배열을 「행 벡터」 또는 「열 벡터」로 명시적으로 변환할 수 있다.
#첫 번째 차원을 따라 축을 삽입하여 1D 배열을 행 벡터로 변환 할 수 있다.
row_vector = a[np.newaxis, :]
print(row_vector.shape)

#열 벡터의 경우 두 번째 차원을 따라 축을 삽입할 수 있다.
col_vector = a[:, np.newaxis]
print(col_vector.shape)
print()


a = np.array([1, 2, 3, 4, 5, 6])
#np.expand_dims을 사용하여 인덱스 위치 1에 축을 추가하는 데 사용할 수 있다.
b = np.expand_dims(a, axis=1)
print(b.shape)
#또는, 인덱스 위치 0에 축을 추가할 수 있다.
c = np.expand_dims(a, axis=0)
print(c.shape)
