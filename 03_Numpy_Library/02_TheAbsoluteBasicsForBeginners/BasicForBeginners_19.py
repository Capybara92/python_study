#다차원 배열 재구성 및 평탄화(Reshaping and flattening multidimensional arrays)
'''flatten(), ravel()'''

#이 배열을 평평하게하는 두 가지 인기있는 방법은 위에 두 가지와 같다.
#flatten()와 ravel()의 주요 차이점은 ravel()를 사용하여 생성된 새로운 배열이 실제로 부모 배열에 대한 참조(즉, "뷰")라는 것이다.
#즉, 새로운 베열에 대한 변경사항은 상위 배열에도 영향을 미친다.
#ravel()복사본을 생성하지 않기 때문에 메모리가 효율적으로 쓰인다.

import numpy as np

x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(x.flatten())

#flatten를 사용하면 새로운 배열을 변경해도 상위 배열이 변경되지 않는다.
a1 = x.flatten()
a1[0] = 99
print(x)   # Original array
print(a1)  # New array

#그러나, ravel를 사용하면 새로운 배열에 대한 변경사항이 상위배열에 영향을준다.
a2 = x.ravel()
a2[0] = 98
print(x)   # Original array
print(a2)  # New array
