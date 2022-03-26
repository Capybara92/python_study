#다층 퍼셉트론 만들어보기2

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(5)

dataset = np.loadtxt("./warehouse/pima-indians-diabetes.data", delimiter=",")

#데이터셋 생성하기
#csv 형식의 파일은 numpy 패키지에서 제공하는 loadtxt() 함수로 직접 불러올 수 있다.
#데이터셋에는 속성값과 판정결과가 모두 포함되어 있기 때문에 입력(속성값 8개)와 출력(판정결과 1개) 변수로 분리한다.
x_train = dataset[:700,0:8]
y_train = dataset[:700,8]
x_test = dataset[700:,0:8]
y_test = dataset[700:,8]


''''''
#모델구성하기
#앞 강좌에서 배운 Dense 레이어만을 사용하여 다층 퍼셉트론 모델을 구성할 수 있다.
#속성이 8개이기 때문에 입력 뉴런이 8개이고, 이진 분류이기 때문에 0~1사이의 값을 나타내는 출력 뉴런이 1개이다.
#   - 첫번째 Dense 레이어는 은닉층(hidden layer)으로 8개 뉴런을 입력받아 12개 뉴런을 출력한다.
#   - 두번째 Dense 레이어는 은닉층으로 12개 뉴런을 입력받아 8개 뉴런을 출력한다.
#   - 마지막 Dense 레이어는 출럭 레이어로 8개 뉴런을 입력받아 1개 뉴런을 출력한다.
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#은닉 레이어의 활성화 함수는 모두 ‘relu’를 사용하였고, 출력 레이어만 0과 1사이로 값이 출력될 수 있도록 활성화 함수를 ‘sigmoid’로 사용하였다.
#0과 1사이의 실수값이 나오기 때문에 양성 클래스의 확률로 쉽게 매칭할 수 있다.


''''''
#모델 학습과정 설정하기
#모델을 정의했다면 모델을 손실함수와 최적화 알고리즘으로 엮어본다.
#   - loss      : 현재 가중치 세트를 평가하는 데 사용한 손실함수 이다. 이진 클래스 문제이므로 ‘binary_crossentropy’으로 지정한다.
#   - optimizer : 최적의 가중치를 검색하는 데 사용되는 최적화 알고리즘으로 효율적인 경사 하강법 알고리즘 중 하나인 ‘adam’을 사용한다.
#   - metrics   : 평가 척도를 나타내며 분류 문제에서는 일반적으로 ‘accuracy’으로 지정한다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#아래 model.compile의 파라미터가 더 존재한다.
#   - loss_weights        :
#   - weighted_metrics    :
#   - run_eagerly         :
#   - steps_per_execution :
#   - ** kwargs           :
