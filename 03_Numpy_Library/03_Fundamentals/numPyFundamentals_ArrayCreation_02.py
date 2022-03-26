#내장 NumPy 배열 생성
#NumPy에는 처음부터 배열을 생성하는 내장함수가 있다.

import numpy as np

#zeros(shape)는 지정된 모양으로 0값으로 채워진 배열을 만듭니다. 기본 dtype은 float64이다.
x = np.zeros((2, 3))
print(x)

#ones(shape)는 1 개의 값으로 채워진 배열을 만듭니다. 다른 모든 측면에서 0과 동일하다.
x = np.ones((2, 3))
print(x)

#arange ()는 정기적으로 증가하는 값으로 배열을 만든다.
x = np.arange(10)
print(x)

x = np.arange(2, 10, dtype=float)
print(x)

x = np.arange(2, 3, 0.1)
print(x)
    #※Arange docstring에 설명되어있는 사용자가 알고 있어야하는 마지막 사용법과 관련하여 약간의 미묘함이 있다.

#linspace ()는 지정된 수의 요소로 배열을 만들고 지정된 시작 값과 끝 값 사이에 균등 한 간격을 둔다.
x = np.linspace(1., 4., 6)
print(x)
#이 함수의 장점은 arange()가 일반적으로 임의의 시작, 중지 및 단계 값에 대해 수행하지 않는 요소 수와 시작 및 끝 지점을 보장 할 수 있다는 것이다.

#indices()는 차원 당 하나씩 해당 차원의 변형을 나타내는 배열집합(1차원이 더 높은 배열로 쌓여 있음)을 만든다.
x = np.indices((3,3))
print(x)
#이는 일반 그리드에서 여러 차원의 함수를 평가하는 데 특히 유용하다.
