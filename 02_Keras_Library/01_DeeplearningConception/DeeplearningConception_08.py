#학습모델 보기, 저장하기, 불러오기1

#몇시간 동안 (또는 며칠 동안) 딥러닝 모델을 학습 시킨 후 만족할만한 결과를 얻었다면, 실무에 바로 적용시키고 싶으실 것이다.
#이때 떠오르는 의문 중 하나가 “딥러닝 모델을 사용하려면 매번 이렇게 몇시간 동안 학습시켜야 되는 거야?”이다.
#대답은 “아니오” 이다. 
#딥러닝 모델을 학습시킨다는 의미는 딥러닝 모델이 가지고 있는 뉴런들의 가중치(weight)을 조정한다는 의미이고, 
#우리는 모델구성과 가중치만 저장만 해놓으면, 필요할 때 저장한 모델구성과 가중치를 불러와서 사용하면 된다.
#간단한 딥러닝 모델의 구성 및 가중치를 저장 및 불러오는 방법에 대해서 알아보자.

#   1. 간단한 모델 살펴보기
#   2. 실무에서의 딥러닝 시스템
#   3. 학습된 모델 저장하기
#   4. 모델 아키텍처 보기
#   5. 학습된 모델 불러오기


''''''
#간단한 모델 살펴보기
#아래는 MNIST 데이터셋(손글씨)을 이용하여 숫자를 분류하는 문제를 간단한 다층퍼셉트론 모델의 소스코드이다.
#이 코드에는 모델 구성부터 학습, 평가, 사용까지 포함하고 있다. 
#이를 위해 데이터셋 구성을 모두 갖추어서 훈련셋, 검증셋, 시험셋을 준비했다.
#또한 훈련셋으로 학습한 모델을 임의의 시험셋으로 예측을 해보겠다.

# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax

# 1. 데이터셋 생성하기

# 훈련셋과 시험셋 불러오기
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터셋 전처리
x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0

# 원핫인코딩 (one-hot encoding) 처리
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# 훈련셋과 검증셋 분리
x_val = x_train[:42000] # 훈련셋의 30%를 검증셋으로 사용
x_train = x_train[42000:]
y_val = y_train[:42000] # 훈련셋의 30%를 검증셋으로 사용
y_train = y_train[42000:]

# 2. 모델 구성하기
model = Sequential()
model.add(Dense(units=64, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 4. 모델 학습시키기
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_val, y_val))

# 5. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('')
print('loss_and_metrics : ' + str(loss_and_metrics))

# 6. 모델 사용하기
xhat_idx = np.random.choice(x_test.shape[0], 5)
xhat = x_test[xhat_idx]
yhat = model.predict_classes(xhat)

for i in range(5):
    print('True : ' + str(argmax(y_test[xhat_idx[i]])) + ', Predict : ' + str(yhat[i]))

#이 코드에서 ‘5. 모델 평가하기’까지가 학습을 하기 위한 과정이고, 
#‘6. 모델 사용하기’이후 코드가 학습된 모델을 사용하는 부분이다.
#이 사이를 분리하여 별도의 모듈로 만들면 우리가 원하는 결과를 얻을 수 있다.
