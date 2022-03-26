#바이트 순서 변경(Changing byte ordering)

#배열의 바이트순서와 보고있는 기본메모리 사이의 관계에 영향을 줄 수있는 두 가지 방법이 있다.
#   - 기본데이터를 다른 바이트 순서로 해석하도록 배열 dtype의 바이트 순서정보를 변경한다. 이것이 arr.newbyteorder()의 역할이다.
#   - dtype해석은 그대로두고 기본 데이터의 바이트 순서를 변경한다. arr.byteswap()이 하는 일이다.

#바이트 순서를 변경해야하는 일반적인 상황
'''
    1. 데이터와 dtype 엔디안이 일치하지 않으며 데이터와 일치하도록 dtype을 변경하려고한다.
    2. 데이터와 dtype 엔디안이 일치하지 않으며 dtype과 일치하도록 데이터를 교체하려고한다.
    3. 데이터와 dtype 엔디안이 일치하지만 데이터를 스왑하고 dtype이 이것을 반영하기를 원힌다.
'''

import numpy as np

big_end_buffer = bytearray([0,1,3,2])
big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer)

#1. 데이터와 dtype엔디안이 일치하지 않으며 데이터와 일치하도록 dtype을 변경하려고한다.
#(데이터와 dtype 엔디안이 일치하지 않습니다. dtype을 데이터와 일치하도록 변경)
#일치하지 않는 부분을 만든다.
wrong_end_dtype_arr = np.ndarray(shape=(2,),dtype='<i2', buffer=big_end_buffer)
print(wrong_end_dtype_arr[0])
#이 상황에 대한 확실한 수정은 올바른 엔디안을 제공하도록 dtype을 변경하는 것이다.
fixed_end_dtype_arr = wrong_end_dtype_arr.newbyteorder()
print(fixed_end_dtype_arr[0])
#배열은 메모리에서 변경되지 않았다.
print(fixed_end_dtype_arr.tobytes() == big_end_buffer)
print()


#2. 데이터와 dtype 엔디안이 일치하지 않으며 dtype과 일치하도록 데이터를 교체하려고한다.
#(데이터와 엔디안 유형이 일치하지 않습니다. dtype과 일치하도록 데이터를 변경)
#특정순서를 유지하기 위해 메모리의 데이터가 필요한 경우이 작업을 수행 할 수 있다.
#예를들어 특정 바이트순서가 필요한 파일에 메모리를 쓸 수 있다.
fixed_end_mem_arr = wrong_end_dtype_arr.byteswap()
print(fixed_end_mem_arr[0])
#이제 배열 이 메모리에서 변경되었다.
print(fixed_end_mem_arr.tobytes() == big_end_buffer)
print()


#3. 데이터와 dtype 엔디안이 일치하지만 데이터를 스왑하고 dtype이 이것을 반영하기를 원힌다.
#(데이터 및 dtype 엔디안 일치, 데이터 및 dtype 교환)
#올바르게 지정된 배열 dtype이 있을 수 있지만 배열이 메모리에서 반대 바이트 순서를 가져야하며 dtype이 일치하여 배열값이 make sense되기를 원한다.
#이 경우 이전 작업을 모두 수행한다.
swapped_end_arr = big_end_arr.byteswap().newbyteorder()
print(swapped_end_arr[0])
print(swapped_end_arr.tobytes() == big_end_buffer)
#ndarray astype메서드를 사용하면 데이터를 특정 dtype 및 바이트 순서로 보다 쉽게 ​​캐스팅 할 수 있다.
swapped_end_arr = big_end_arr.astype('<i2')
print(swapped_end_arr[0])
print(swapped_end_arr.tobytes() == big_end_buffer)
