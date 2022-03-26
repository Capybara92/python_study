#수치입력 수치예측 모델 레시피2

#모델준비
#   1. 선형회귀 모델
#   2. 퍼셉트론 신경망 모델
#   3. 다층퍼셉트론 신경망 모델
#   4. 깊은 다층퍼셉트론 신경망 모델

#선형회귀 모델
#가장 간단한 1차 선형회귀 모델로 수치예측을 해보자.
#아래 식에서 x, y는 우리가 만든 데이터셋이고, 회귀분석을 통해서, w와 b값을 구하는 것이 목표이다.
#Y = w * X + b

#w와 b값을 구하게 되면, 임의의 입력 x에 대해서 출력 y가 나오는 데 이것이 예측 값이다.
#w, b 값은 분산, 공분산, 평균을 이용하여 쉽게 구할 수 있다.
#w = np.cov(X, Y, bias=1)[0,1] / np.var(X)
#b = np.average(Y) - w * np.average(X)

#간단한 수식이지만 이 수식을 도출하기란 꽤나 복잡하다.
#오차를 최소화하는 극대값을 구하기 위해 편미분을 수행하고, 다시 식을 전개하는 등등의 과정이 필요하다.

# 0. 사용할 패키지 불러오기
import numpy as np
from sklearn.metrics import mean_squared_error
import random

# 1. 데이터셋 생성하기
x_train = np.random.random((1000, 1))
y_train = x_train * 2 + np.random.random((1000, 1)) / 3.0
x_test = np.random.random((100, 1))
y_test = x_test * 2 + np.random.random((100, 1)) / 3.0

x_train = x_train.reshape(1000,)
y_train = y_train.reshape(1000,)
x_test = x_test.reshape(100,)
y_test = y_test.reshape(100,)

# 2. 모델 구성하기
w = np.cov(x_train, y_train, bias=1)[0,1] / np.var(x_train)
b = np.average(y_train) - w * np.average(x_train)

print(w, b)

# 3. 모델 평가하기
y_predict = w * x_test + b
mse = mean_squared_error(y_test, y_predict)
print('mse : ' + str(mse))
