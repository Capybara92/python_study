#프로그램 내에서 가변적인 수의 인덱스 다루기(Dealing with variable numbers of indices within programs)
#인덱스 구문은 매우 강력하지만 다양한 수의 인덱스를 처리 할 때 제한적이다.

import numpy as np

z = np.arange(81).reshape(3,3,3,3)

indices = (1,1,1,1)
print(z[indices])
#코드를 사용하여 여러 인덱스의 튜플을 생성한 다음 인덱스 내에서 사용할 수 있다.

#Python에서 slice()함수를 사용하여 프로그램 내에서 슬라이스를 지정할 수 있다.
indices = (1,1,1,slice(0,2)) # same as [1,1,1,0:2]
print(z[indices])

#마찬가지로 Ellipsis개체를 사용하여 코드에서 줄임표를 지정할 수 있다.
indices = (1, Ellipsis, 1) # same as [1,...,1]
print(z[indices])
#이러한 이유로 항상 인덱스배열의 튜플을 반환하므로 np.nonzero()함수의 출력을 인덱스로 직접 사용할 수 있다.

print()
#튜플의 특수처리로 인해 리스트처럼 자동으로 배열로 변환되지 않는다.
print(z[[1,1,1,1]]) #produces a large array
print(z[(1,1,1,1)]) #returns a single value