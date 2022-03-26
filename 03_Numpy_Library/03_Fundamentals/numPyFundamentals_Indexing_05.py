#부울 또는 "마스크"인덱스 배열(Boolean or “mask” index arrays)
#인덱스로 사용되는 부울배열은 인덱스배열과 완전히 다른 방식으로 처리된다.
#부울배열은 인덱싱되는 배열의 초기차원과 모양이 같아야한다.

import numpy as np

y = np.arange(35).reshape(5,7)

b = y>20
print(y[b])

#정수 인덱스배열의 경우와 달리 부울의경우, 결과는 부울배열의 모든 실제요소에 해당하는 인덱스배열의 모든요소를 ​​포함하는 1차원 배열이다. 
#인덱스배열의 요소는 항상 반복되고 행 우선(C언어 스타일) 순서로 반환된다.
#결과도 y[np.nonzero(b)].와 동일한 인덱스배열로 반환되는 것은 슬라이스로 가져오는 뷰가 아니라 데이터의 복사본이다.
#y의 차원이 b보다 많으면 결과는 다차원이된다. 예를 들면 :
print(b[:,5])
print(y[b[:,5]])

#일반적으로 부울배열의 차원이 인덱싱되는 배열보다 적으면 y[b,…]와 동일하다. 즉, y는 y의 순위를 채우는 데 필요한만큼 b다음에 b가 인덱싱된다. 
#따라서 결과의 모양은 부울배열의 True요소 수를 포함하는 하나의 차원이고, 그 뒤에 인덱싱되는 배열의 나머지 차원이 이어진다.
#예를 들어, 4개의 True요소가있는 2차원 부울모양배열(2,3)을 사용하여 3차원 모양배열(2,3,5)에서 행을 선택하면 -> 모양(4,5)
x = np.arange(30).reshape(2,3,5)
b = np.array([[True, True, False], [False, True, True]])
print(x[b])