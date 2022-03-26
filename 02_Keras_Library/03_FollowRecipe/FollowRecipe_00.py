#수치입력 수치예측 모델 레시피1

#수치를 입력해서 수치를 예측하는 모델들에 대해서 알아보겠다.
#수치예측을 위한 데이터셋 생성을 해보고, 
#선형회귀를 위한 가장 간단한 퍼셉트론 신경망 모델부터 깊은 다층퍼셉트론 신경망 모델까지 구성 및 학습을 시켜보겠다.

#데이터셋 준비
#입력 x에 대해 2를 곱해 두배 정도값을 갖는 출력 y가 되도록 데이터셋을 생성해봤다.
#선형회귀 모델을 사용한다면 Y = w * X + b 일 때, w가 2에 가깝고, b가 0.16에 가깝게 되도록 학습시키는 것이 목표이다.
#선형 회귀 : 종속 변수 y와 한개 이상의 독립 변수(또는 설명 변수) X와의 선형 상관관계를 모델링하는 회귀분석 기법이다.
import numpy as np

# 데이터셋 생성
x_train = np.random.random((1000, 1)) #numpy.random.random_sample()과 같다.(0.0 이상 1.0 미만) 
#499를 넘어가면 왜 소수점이 1의자리가 늘어가는가? 
#500이상부터는 왜 500만 출력하는가?
#길이를 출력하면 100개가 나온다. print(len(x_train))
y_train = x_train * 2 + np.random.random((1000, 1)) / 3.0
x_test = np.random.random((100, 1))
y_test = x_test * 2 + np.random.random((100, 1)) / 3.0

# 데이터셋 확인
import matplotlib.pyplot as plt

plt.plot(x_train, y_train, 'ro')
plt.plot(x_test, y_test, 'bo')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


''''''
#레이어 준비
#Input data, Labels : 1차원의 입력 데이터 및 라벨이다.
#Dense              : 모든 입력 뉴런과 출력 뉴런을 연결하는 전결합층이다.
#relu               : 활성화 함수로 주로 은닉층에 사용된다.
