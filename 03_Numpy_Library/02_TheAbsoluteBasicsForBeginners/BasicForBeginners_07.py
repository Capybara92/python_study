#배열의 형태를 변경

#arr.reshape()함수를 사용하면 데이터를 변경하지 않고 배열에 새로운 모양을 제공한다.
#reshape메서드를 사용할 때 생성하려는 배열에는 원래배열과 동일한 수의 요소가 있어야한다.

import numpy as np

a = np.arange(6)
print(a)

b = a.reshape(3, 2)
print(b)

#np.reshape()함수에서 몇 가지 선택적 매개변수를 지정할 수 있다.
print(np.reshape(a, newshape=(1, 6), order='C'))

#newshape는 새로운 모양다.
#정수 또는 정수튜플을 지정할 수 있다.
#정수를 지정하면 결과는 해당 길이의 배열이된다.
#모양은 원래 모양과 호환되어야 한다.

#order:'C'는 C언어와 같은 인덱스 순서를 사용하여 요소를 읽고 쓰는것을 의미한다.
#F는 Fortran과 같은 인덱스 순서를 사용하여 요소를 읽고 쓰는것을 의미한다.
#A는 Fortran과 같은 인덱스 순서로 요소를 읽고 쓴다. 만일 A가 Fortran의 인접한 메모리라면 C언어의 순서를 따른다.

#기본적으로 C언어 및 Fortran의 순서는 인덱스가 배열이 메모리에 저장되는 순서와 일치하는 방식과 관련이 있다. 
#C언어에서는 마지막 인덱스가 가장 빠르게 변경된다. 
#Fortran에서 메모리에 저장된 2차원 배열의 요소를 이동할 때 첫 번째 인덱스는 가장 빠르게 변하는 인덱스이다.

#C언어 또는 Fortran에 대해 수행하는 작업은 인덱싱 규칙을 유지하는 것이 더 중요한지 데이터를 다시 정렬하지 않는지 여부에 따라 다르다.
