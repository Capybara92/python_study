#난수생성

#난수생성은 많은 수치 및 기계 학습 알고리즘의 구성 및 평가에서 중요한 부분이다.
#인공 신경망에서 가중치를 무작위로 초기화해야 하는지, 데이터를 무작위 세트로 분할해야 하는지, 데이터 세트를 무작위로 셔플해야 하는지
#여부에 관계없이 난수(실제로 반복 가능한 의사 난수)를 생성 할 수 있어야 한다.

#Generator.integers를 사용하면 낮음(NumPy포함)에서 높음(배타적)까지 임의의 정수를 생성 할 수 있다.
#endpoint=True은 높은 숫자를 포함하도록 설정할 수 있다.

from numpy.random import default_rng
rng = default_rng()

print(rng.integers(5, size=(2, 4))) # 0과 4사이의 임의정수로 구성된 2 x 4 배열을 생성 할 수 있다.

'''
다른 난수생성 방법 
from numpy import random
vals = random.standard_normal(10)
more_vals = random.standard_normal(10)
'''
