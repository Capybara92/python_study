#Python array 객체를 NumPy 배열로 변환

#일반적으로 파이썬에서 배열과 같은 구조로 배열 된 숫자 데이터는 array () 함수를 사용하여 배열로 변환 할 수 있다.
#가장 좋은 예로는 「목록」과 「튜플」이다.
#일부 개체는 배열 프로토콜을 지원하고 이러한 방식으로 배열로 변환 할 수 있다.

import numpy as np

x = np.array([2,3,1,0])
x = np.array([2, 3, 1, 0])
x = np.array([[1,2.0],[0,0],(1+1j,3.)]) # note mix of tuple and lists, and types
x = np.array([[ 1.+0.j, 2.+0.j], [ 0.+0.j, 0.+0.j], [ 1.+1.j, 3.+0.j]])
