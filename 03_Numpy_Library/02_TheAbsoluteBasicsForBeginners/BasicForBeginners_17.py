#행렬 전치 및 재구성(Transposing and reshaping a matrix)
'''arr.reshape(), arr.transpose(), arr.T'''
                        #transpose (순서를) 뒤바꾸다 (=reverse), (다른 장소·환경으로) 바꾸다[이동시키다] (=transfer)

#행렬을 전치해야하는 것이 일반적이다.
#NumPy배열에는 T행렬을 전치할 수 있는 속성이 있다.

#행렬의 차원을 전환해야 할 수도 있다.
#예를 들어,
#데이터세트와 다른 특정입력 형태를 예상하는 모델이있는 경우 이러한 상황이 발생할 수 있다.
#reshape방법이 가능하다.
#행렬에 대해 원하는 새로운 차원을 전달하기만 하면된다.

import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])

print(data.reshape(2, 3))
print(data.reshape(3, 2))


#.transpose()를 사용하여 지정한 값에 따라 배열의 축을 반전하거나 변경할 수도 있다.
arr = np.arange(6).reshape((2, 3))
print(arr)

print(arr.transpose())
#또는
print(arr.T)
