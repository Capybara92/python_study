#NumPy는 테이블형식 데이터에서 배열을 생성하는 여러 기능을 제공한다.
#여기서는 genfromtxt기능에 중점을 둔다.

#간단히 말해서, genfromtxt 두 개의 주요루프를 실행한다.
#첫 번째 루프는 일련의 문자열에서 파일의 각 줄을 변환한다.
#두 번째 루프는 각 문자열을 적절한 데이터 유형으로 변환한다.
#이 메커니즘은 단일루프보다 느리지 만 더 많은 유연성을 제공한다.
#특히, loadtxt처럼 빠르고 단순한 함수는 못하는 것을 genfromtxt는 누락 된 데이터를 고려할 수 있다.

#예제를 제공 할 때 다음 규칙을 사용.
'''
import numpy as np
from io import StringIO
'''
