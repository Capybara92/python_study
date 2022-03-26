#인덱스 배열과 슬라이스 결합(Combining index arrays with slices)

import numpy as np

y = np.arange(35).reshape(5,7)

print(y[np.array([0, 2, 4]), 1:3])
#실제로 슬라이스 및 인덱스 배열작업은 독립적이다.
#슬라이스 연산은 인덱스 1과 2가있는 열(즉, 두 번째 및 세 번째 열)을 추출한 다음,
#인덱스가 0, 2, 4 인 행(즉, 첫 번째, 세 번째 및 다섯 번째 행)을 추출하는 인덱스 배열 작업이 이어진다.
#이것은 다음과 동일
print(y[:, 1:3][np.array([0, 2, 4]), :])

#마찬가지로 슬라이싱은 브로드캐스트된 부울인덱스와 결합될 수 있다.
b = y > 20
print(b)
print(y[b[:,5],1:3])