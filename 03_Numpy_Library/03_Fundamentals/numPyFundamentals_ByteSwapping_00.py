#바이트 스와핑(Byte-swapping)

#ndarray는 메모리 내의 데이터 파이썬 어레이 인터페이스를 제공하는 개체이다.
#배열로 보려는 메모리가 Python을 실행중인 컴퓨터와 동일한 바이트 순서가 아닌 경우가 종종 발생한다.

#예를 들어, Intel Pentium과 같은 little-endian CPU가있는 컴퓨터에서 작업 할 수 있지만,
#big-endian 컴퓨터에서 작성한 파일에서 일부 데이터를 로드했다. 
#Sun(big-endian)컴퓨터에서 작성한 파일에서 4바이트를 로드했다는 가정하에,
#이 4바이트는 두 개의 16비트 정수를 나타냅니다. big-endian에서 2바이트 정수는 MSB(Most Significant Byte)를 먼저 저장한 다음,
#LBS(Least Significant Byte)를 사용하여 저장한다. 따라서 바이트는 메모리 순서로 다음과 같다.
'''
    1. MSB 정수 1
    2. LSB 정수 1
    3. MSB 정수 2
    4. LSB 정수 2
'''

import numpy as np

#두 개의 정수가 실제로 1과 770이라고 가정 해 보자. 770 = 256 * 3 + 2이기 때문에 메모리의 4 바이트에는 각각 0, 1, 3, 2가 포함된다
big_end_buffer = bytearray([0,1,3,2])
print(big_end_buffer)
#ndarray이 정수에 액세스 하기 위해를 사용할 수 있다.
#이 경우 이 메모리 주위에 배열을 만들고 numpy에게 두 개의 정수가 있으며 16비트와 빅 엔디안임을 알릴 수 있다.

big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer)

print(big_end_arr[0])
print(big_end_arr[1])

#「>i2」의 array dtype을 유의할것. 「>」의 의미는 ‘big-endian’(「<」는 ‘little-endian’)이고, 「i2」의 의미는 ‘signed 2-byte integer’이다.
#예를 들어 데이터가 unsigned 4바이트 little-endian정수를 나타내는 경우, 그 dtype문자열은 <u4 이다.

#사실이라면 우리는 무엇을 시도해야 할까?
little_end_u4 = np.ndarray(shape=(1,),dtype='<u4', buffer=big_end_buffer)
print(little_end_u4[0] == 1 * 256**1 + 3 * 256**2 + 2 * 256**3)

#big_end_arr인 경우 기본데이터는 big-endian(데이터 엔디안)이고, dtype을 일치하도록 설정했다.(dtype도 big-endian 임)
#그러나 때로는 이것을 뒤집어야 힌다.

#스칼라는 현재 바이트 순서정보를 포함하지 않으므로 배열에서 스칼라를 추출하면 기본 바이트순서로 정수가 반환된다.
'''Warning'''
print(big_end_arr[0].dtype.byteorder == little_end_u4[0].dtype.byteorder)