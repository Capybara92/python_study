#배열의 모양과 크기
'''ndarray.ndim, ndarray.size, ndarray.shape'''

import numpy as np

array_example = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])


#배열의 축 수 또는 차원 수
print(array_example.ndim)

#배열의 총 요소 수
print(array_example.size)

#배열의 모양
print(array_example.shape) #(행, 열, 요소)
