#구조적 인덱싱 도구(Structural indexing tools)
#표현식 및 할당에서 배열모양을 쉽게 일치시키기 위해 배열인덱스 내에서 np.newaxis객체를 사용하여 크기가 1인 새 차원을 추가 할 수 있다.

import numpy as np

y = np.arange(35).reshape(5,7)

print(y.shape)
print(y[:,np.newaxis,:].shape)

#배열에 새 요소가 없으며 차원이 증가한다는 점에 유의할 것.
#그렇지 않으면 명시적으로 모양을 변경해야하는 방식으로 두 배열을 결합하는 것이 편리할 수 ​​있다.
x = np.arange(5)

print(x[:,np.newaxis] + x[np.newaxis,:])

#생략 부호 구문은 지정되지 않은 나머지 차원을 모두 선택하는 것을 나타내는 데 사용될 수 있다.
z = np.arange(81).reshape(3,3,3,3)

print(z[1,...,2])
#or
print(z[1,:,:,2])
