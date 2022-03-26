#배열유형 및 유형 간 변환_2
#NumPy 숫자유형은 dtype각각 고유한 특성(데이터 유형)을 가진 개체의 인스턴스이다.
#NumPy를 가져 오면 「import numpy as np」 np.bool_, np.float32등은 dtypes로 사용할 수 있다.

#부울(bool), 정수(int), 부호없는 정수(uint), 부동 소수점(float), 복소수를 나타내는 5가지 기본숫자 유형이 있다.
#이름에 숫자가 있는것은 유형의 비트크기(즉, 메모리에서 단일 값을 나타내는 데 필요한 비트 수)를 나타낸다.
#다음과 같은 몇 가지 유형(int, intp)은 플랫폼(예를 들어 32 비트 대 64 비트 시스템)에 따라 다른 bitsizes을 보유하고 있다.
#이것은 원시 메모리가 처리되는 저수준 코드(예 : C 또는 Fortran)와 인터페이스 할 때 고려해야한다.

import numpy as np

#데이터 유형은 파이썬숫자를 배열스칼라로 변환하는 함수(설명은 배열 스칼라 섹션 참조),
#숫자의 파이썬시퀀스를 해당유형의 배열로,
#많은 numpy함수나 메서드가 허용하는 dtype키워드에 대한 인수로 사용할 수 있다.
x = np.float32(1.0)
print(x)

y = np.int_([1,2,4])
print(y)

z = np.arange(3, dtype=np.uint8)
print(z)

#배열유형은 문자코드로도 참조 할 수 있으며, 대부분 Numeric과 같은 이전 패키지와의 역 호환성을 유지한다.
#예를 들어 일부문서는 여전히 다음을 참조 할 수 있다.
print(np.array([1, 2, 3], dtype='f'))
#dtype개체를 사용하는 것을 추천한다.

#배열유형을 변환하려면 .astype()메서드(권장) 또는 유형자체를 함수로 사용한다.
print(z.astype(float))
print(np.int8(z))
#위에서 Python float객체를 dtype으로 사용한다. 
#Numpy에서 int는 np.int_를, bool은 np.bool_을, float는 np.float_를, complex는 np.complex_를 참조한다.
#다른 데이터 유형에는 Python에 해당하는 항목이 없다.

#배열 유형을 확인하려면 dtype 속성을 확인
print(z.dtype)

#dtype 개체에는 비트 너비 및 바이트 순서와 같은 형식에 대한 정보도 포함된다.
#데이터 유형은 정수인지 여부와 같은 유형의 속성을 쿼리하는데 간접적으로 사용할 수도 있다.
d = np.dtype(int)
print(d)
print(np.issubdtype(d, np.integer))
print(np.issubdtype(d, np.floating))
