#학습 조기종료 시키기
#앞서 ‘학습과정과 데이터셋 이야기’에서 과적합이라는 것을 살펴보았고, 이를 방지하기 위해 조기종료하는 시점에 대해서 알아보았다.
#본 절에서는 케라스에서 제공하는 기능을 이용하여 학습 중에 어떻게 조기종료를 시킬 수 있는 지 알아보자.

#과적합되는 모델 살펴보기
#먼저 과적합되는 모델을 만들고 어떻게 학습이 되었는 지 살펴보자.
#아래 코드에서 사용된 데이터수, 배치사이즈, 뉴런 수 등은 과적합 현상을 재현하기 하기 위해 설정된 것으로 실제 최적화된 수치는 아니다.

#조기 종료 시키기
#학습 조기 종료를 위해서는 「EarlyStopping」이라는 함수를 사용하며 더 이상 개선의 여지가 없을 때 학습을 종료시키는 콜백함수이다.
#콜백함수 라는것은 어떤 함수를 수행 시 그 함수에서 내가 지정한 함수를 호출하는 것을 말하며, 
#여기서는 fit 함수에서 「EarlyStopping」이라는 콜백함수가 학습 과정 중에 매번 호출된다.
#먼저 fit 함수에서 「EarlyStopping」콜백함수를 지정하는 방법은 다음과 같다.
'''
early_stopping = EarlyStopping()
model.fit(X_train, Y_train, nb_epoch= 1000, callbacks=[early_stopping])
'''
#에포크가 1000으로 지정했더라도 학습과정에서 「EarlyStopping」콜백함수를 호출하여 해당 조건이 되면 학습을 조기 종료시킨다.
#「EarlyStopping」콜백함수에서 설정할 수 있는 인자는 다음과 같다.
'''
keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=0, verbose=0, mode='auto')

- monitor   : 관찰하고자 하는 항목이다. ‘val_loss’나 ‘val_acc’가 주로 사용된다.
- min_delta : 개선되고 있다고 판단하기 위한 최소 변화량을 나타낸다. 만약 변화량이 min_delta보다 적은 경우에는 개선이 없다고 판단한다.
- patience  : 개선이 없다고 바로 종료하지 않고 개선이 없는 에포크를 얼마나 기다려 줄 것인 가를 지정한다.
              만약 10이라고 지정하면 개선이 없는 에포크가 10번째 지속될 경우 학습일 종료한다.
- verbose   : 얼마나 자세하게 정보를 표시할 것인가를 지정한다. (0, 1, 2)
- mode      : 관찰 항목에 대해 개선이 없다고 판단하기 위한 기준을 지정한다.
              예를들어, 관찰항목이 ‘val_loss’인 경우에는 감소되는 것이 멈출 때 종료되어야 하므로, ‘min’으로 설정된다.
                1. auto : 관찰하는 이름에 따라 자동으로 지정한다.
                2. min  : 관찰하고 있는 항목이 감소되는 것을 멈출 때 종료한다.
                3. max  : 관찰하고 있는 항목이 증가되는 것을 멈출 때 종료한다.
'''
#조기 종료 콜백함수를 적용한 코드는 다음과 같다.


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
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(patience = 20) # 조기종료 콜백함수 정의 #증가가 되었더라도 20 에포크 동안은 기다려보도록 지정
hist = model.fit(X_train, Y_train, epochs=3000, batch_size=10, validation_data=(X_val, Y_val), callbacks=[early_stopping])

# 5. 모델 학습 과정 표시하기
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

# 6. 모델 사용하기
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)

print('')
print('loss : ' + str(loss_and_metrics[0]))
print('accuray : ' + str(loss_and_metrics[1]))
