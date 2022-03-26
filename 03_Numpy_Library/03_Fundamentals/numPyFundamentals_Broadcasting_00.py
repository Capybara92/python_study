#브로드 캐스팅(Broadcasting)
#   numpy.broadcast
#브로드 캐스팅이라는 용어는 산술 연산중에 numpy가 다른모양의 배열을 처리하는 방법을 설명한다.
#특정 제약조건에 따라 더 작은배열은 더 큰배열에 "브로드 캐스트"되어 호환되는 모양을 갖는다.
#브로드 캐스팅은 배열연산을 벡터화하는 수단을 제공하여 Python 대신 C에서 루핑이 발생하도록합니다.
'''루핑 : 프로그램 속에서 동일한 명령이나 처리를 반복하여 실행 하는 것을 말한다.'''
#불필요한 데이터 사본을 만들지않고 이를 수행하며 일반적으로 효율적인 알고리즘 구현으로 이어진다.
#그러나 브로드캐스트가 메모리를 비효율적으로 사용하여 계산속도를 늦추기 때문에 위화감이 드는 경우가 있다.

#NumPy 작업은 일반적으로 요소별로 배열 쌍에서 수행된다.
#가장 간단한 경우 두 배열은 다음예제와 같이 정확히 같은모양을 가져야한다.

import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])

print(a * b)

#NumPy의 브로드캐스팅 규칙은 배열의 모양이 특정 제약조건을 충족할 때이 제약 조건을 완화한다.
#가장 간단한 브로드캐스팅 예제는 작업에서 배열과 스칼라 값이 결합될 때 발생한다.

a = np.array([1.0, 2.0, 3.0])
b = 2.0

print(a * b)
#결과는 b배열이었던 이전예제와 동일하다.
#산술연산 중에 스칼라 b가 a와 같은모양의 배열로 늘어나는 것을 생각할 수 있다. 
#b의 새 요소는 단순히 원래 스칼라의 복사본이다.
#스트레칭 비유는 단지 개념적이다.
#NumPy는 실제로 복사하지 않고도 원래 스칼라 값을 사용할 수 있을만큼 똑똑하므로 브로드캐스팅 작업이 가능한 한 메모리와 계산적으로 효율적이다.

#두 번째 예제의 코드는 첫 번째 예제의 코드보다 더 효율적이다.
#브로드캐스트는 곱셈 중에 메모리를 덜 이동하기 때문이다. (b배열이 아니라 스칼라 이다)