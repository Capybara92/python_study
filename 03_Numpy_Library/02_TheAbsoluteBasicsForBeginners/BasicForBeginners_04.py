#기본 배열을 만드는 방법
'''
np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(), dtype
'''

#NumPy배열을 만들려면 np.array()함수를 사용해야 한다.
#간단한 배열을 만들려면 리스트을 전달하기만 하면된다.
#원하는경우 리스트에서 데이터 유형을 지정할 수도 있다. 
import numpy as np
a = np.array([1, 2, 3])
'''배열 및 배열 작업은 여기에서 캡처 한 것보다 훨씬 더 복잡하다!'''

#0으로 채워진 배열을 쉽게 만들 수 있다.
print(np.zeros(2))

#또는 1로 채워진 배열.
print(np.ones(2))

#또는 비어있는 배열
print(np.empty(2))
#empty함수는 초기 내용이 무작위이고 메모리 상태에 따라 달라지는 배열을 만든다.

#위의 함수들을 사용하는 이유는 속도 때문이다.
#나중에 모든 요소를 ​​채워야하기 때문이다.

#다양한 요소를 사용하여 배열을 만들 수 있다.
print(np.arange(4))

#일정한 간격의 간격을 포함하는 배열도 있다.
#이렇게 하려면 첫 번째 숫자, 마지막 숫자, 단계크기를 지정한다.
print(np.arange(2, 9, 2))

#지정된 간격으로 선형간격을 갖는 값으로 배열을 만들 수도 있다.
print(np.linspace(0, 10, num=5))

#기본데이터 유형은 부동소수점(np.float64)이지만,
#dtype키워드를 사용하여 원하는 데이터유형을 명시적으로 지정할 수 있다.
x = np.ones(2, dtype=np.int64)
print(x)
