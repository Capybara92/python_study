#오버플로 오류(Overflow Errors)

#NumPy 숫자유형의 고정크기는 값이 데이터유형에서 사용 가능한 것보다 더 많은 메모리를 필요로 할 때 오버플로 오류를 일으킬 수 있다.
#예를 들어, numpy.power함수는 64-bit integers로 (100 * 10 ** 8)를 정확히 평가하지만, a 32-bit integer으로는 정확히 평가가 안된다.

import numpy as np

print(np.power(100, 8, dtype=np.int64))
print(np.power(100, 8, dtype=np.int32))

#NumPy와 파이썬의 정수타입은 정수오버플로가 상당히 다르고 NumPy 수가 Python의 int와 유사하게 동작할 것으로 예상하는 사용자를 혼동시킬 수 있다.
#NumPy와 달리 Python int의 크기는 유연하다.
#이것은 파이썬 정수가 모든 정수를 수용하기 위해 확장 될 수 있으며 오버플로되지 않음을 의미한다.

#Numpy는 NumPy정수 및 부동 소수점 값의 최소값 또는 최대값을 각각 확인하기 위해 「numpy.iinfo」와 「numpy.finfo」를 제공한다. 
print(np.iinfo(int))      # Bounds of the default integer on this system.
print(np.iinfo(np.int32)) # Bounds of a 32-bit integer
print(np.iinfo(np.int64)) # Bounds of a 64-bit integer

#64비트 정수가 여전히 너무 작으면 결과가 부동소수점 숫자로 캐스트 될 수 있다.
#부동소수점 숫자는 더 크지만 정확하지 않은 가능한 값 범위를 제공한다.
print(np.power(100, 100, dtype=np.int64))    # Incorrect even with 64-bit int
print(np.power(100, 100, dtype=np.float64))
