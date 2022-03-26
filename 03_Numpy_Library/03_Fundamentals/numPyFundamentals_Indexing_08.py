#인덱스 배열에 값 할당
#언급했듯이 단일 인덱스, 슬라이스, 인덱스 및 마스크 배열을 사용하여 할당할 배열의 하위집합을 선택할 수 있다.
#인덱스 배열에 할당되는 값은 모양이 일치해야한다. (인덱스가 생성하는 모양과 동일한 모양 또는 브로드 캐스트 가능)
#예를 들어, 슬라이스에 상수를 할당 할 수 있다.

import numpy as np

x = np.arange(10)
x[2:7] = 1
#또는 올바른 크기의 배열
x[2:7] = np.arange(5)

#더 높은 유형을 더 낮은 유형에 할당하거나(예 : float를 int에) 예외(복합을 float 또는 int에 할당)에 할당하면 할당이 변경 될 수 있다.
x[1] = 1.2
print(x[1])
print()

''' x[1] = 1.2j #TypeError: can't convert complex to int'''

#일부 참조(예 : 배열 및 마스크 인덱스)와 달리 할당은 항상 배열의 원본데이터에 적용된다. (실제로 다른 것은 의미가 없다)
#하지만 일부 작업은 순진하게 예상 한대로 작동하지 않을 수 있다.
'''이 특별한 예는 종종 사람들이 놀란다.'''
x = np.arange(0, 50, 10)
print(x)

x[np.array([1, 1, 3, 1])] += 1
print(x)

'''
사람들은 첫 번째 위치가 3씩 증가 할 것이라고 예상하지만 실제로 1만큼만 증가한다.
그 이유는 1, 1, 3의 값을 포함하는 원본(임시)에서 새 배열이 추출되기 때문이다.
, 1이면 값 1이 임시에 추가되고 임시가 다시 원래 배열에 할당된다.
따라서 x[1] + 1 에서 배열의 값은 3번 증가하는 대신 x[1]에 3번 할당된다.
'''