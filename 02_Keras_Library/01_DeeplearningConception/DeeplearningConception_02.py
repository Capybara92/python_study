#학습과정 살펴보기1

#케라스로 딥러닝 모델 개발할 때, 가장 많이 보게 되는 것이 fit함수가 화면에 찍어주는 로그이다.
#이 로그에 포함된 수치들은 학습이 제대로 되고 있는 지, 학습을 그만할 지 등 판단하는 중요한 척도가 된다.
#수치 자체도 큰 의미가 있지만 수치들이 에포코마다 바뀌는 변화 추이를 보는 것이 중요하기 때문에 그래프로 표시하여 보는 것이 더 직관적이다.
#본 절에서는 케라스에서 제공하는 기능을 이용하는 방법, 텐서보드와 연동하여 보는 방법, 콜백함수를 직접 만들어서 사용하는 방법에 대해서 알아보자.
#   - 히스토리 기능 사용하기
#   - 텐서보드와 연동하기
#   - 직접 콜백함수 만들어보기

#히스토리 기능 사용하기
#케라스에서 학습시킬 때 fit함수를 사용한다. 이 함수의 반환 값으로 히스토리 객체를 얻을 수 있는데, 이 객체는 다음의 정보를 담고 있다.
#   - 매 에포크 마다의 훈련 손실값 (loss)
#   - 매 에포크 마다의 훈련 정확도 (acc)
#   - 매 에포크 마다의 검증 손실값 (val_loss)
#   - 매 에포크 마다의 검증 정확도 (val_acc)

#히스토리 기능은 케라스의 모든 모델에 탑재되어 있으므로 별도의 설정없이 fit 함수의 반환으로 쉽게 얻을 수 있다.
#사용법은 다음과 같다.
'''
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10, validation_data=(X_val, Y_val))

print(hist.history['loss'])
print(hist.history['acc'])
print(hist.history['val_loss'])
print(hist.history['val_acc'])
'''
#수치들은 각 에포크마다 해당 값이 추가되므로 배열 형태로 저장되어 있다.
#이러한 수치들을 매 에포크마다 변화되는 추이를 그래프로 표시하여 비교하면서 보면 학습 상태를 직관적으로 이해하기 쉽다.
#matplotlib 패키지를 이용하면 하나의 그래프로 쉽게 표시할 수 있다.
#   - train_loss('y' 노란색) : 훈련 손실값이며 x축은 에포크 수, 좌측 y축은 손실값을 나타낸다.
#   - val_loss('r' 빨간색)   : 검증 손실값이며 x축은 에포크 수, 좌측 y축은 손실값을 나타낸다.
#   - train_acc('b' 파란색)  : 훈련 정확도이며 x축은 에포크 수, 우측 y축은 정확도를 나타낸다.
#   - val_acc('g' 녹색)      : 검증 정확도이며 x축은 에포크 수, 우측 y축은 정확도를 나타낸다.


''''''
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

np.random.seed(3)

# 1. 데이터셋 준비하기

# 훈련셋과 시험셋 로딩
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 훈련셋과 검증셋 분리
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]

X_train = X_train.reshape(50000, 784).astype('float32') / 255.0
X_val = X_val.reshape(10000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0

# 훈련셋, 검증셋 고르기
train_rand_idxs = np.random.choice(50000, 700)
val_rand_idxs = np.random.choice(10000, 300)

X_train = X_train[train_rand_idxs]
Y_train = Y_train[train_rand_idxs]
X_val = X_val[val_rand_idxs]
Y_val = Y_val[val_rand_idxs]

# 라벨링 전환
Y_train = np_utils.to_categorical(Y_train)
Y_val = np_utils.to_categorical(Y_val)
Y_test = np_utils.to_categorical(Y_test)

# 2. 모델 구성하기
model = Sequential()
model.add(Dense(units=2, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# 3. 모델 엮기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10, validation_data=(X_val, Y_val))

# 5. 모델 학습 과정 표시하기
'''
%matplotlib inline
Jupyter IPython 노트북을 사용하지 않는경우 줄을 주석처리(또는 삭제)하면 모든것이 잘 작동하며 콘솔에서 Python스크립트를 실행하는 경우 별도의 플롯창이 열린다.
그러나 Jupyter IPython 노트북을 사용하는 경우 노트북의 첫 번째 Python 코드셀에 "%matplotlib inline"줄이 있어야 플롯을 볼 수 있다.
'''

import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
