#학습과정 살펴보기1

#직접 콜백함수 만들어보기
#기본적인 모델의 학습 상태 모니터링은 앞서 소개한 히스토리 콜백함수나 텐서보드를 이용하면 되지만, 
#「순환신경망 모델」인 경우에는 fit함수를 여러번 호출하기 때문에 제대로 학습상태를 볼 수가 없다.
#먼저 순환신경망 모델 코드를 살펴보자.
'''
for epoch_idx in range(1000):
    print ('epochs : ' + str(epoch_idx) )
    hist = model.fit(train_X, train_Y, epochs=1, batch_size=1, verbose=2, shuffle=False) # 50 is X.shape[0]
    model.reset_states()
'''
#매 에포크마다 히스토리 객체가 생성되어 매번 초기화 되기 때문에 에포크별로 추이를 볼 수가 없다.
#이 문제를 해결하기 위해 fit함수를 여러 번 호출하더라도 학습상태가 유지될 수 있도록 콜백함수를 정의해보자.
'''
import keras

# 사용자 정의 히스토리 클래스 정의
class CustomHistory(keras.callbacks.Callback):
    def init(self):
        self.losses = []
        self.vol_losses = []
        self.accs = []
        self.vol_accs = []        
        
    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
        self.vol_losses.append(logs.get('vol_loss'))
        self.accs.append(logs.get('acc'))
        self.vol_accs.append(logs.get('acc_loss'))
'''
#새로 만든 콜백함수를 이용해서 학습 상태를 모니터링 해보자.
#이전 코드에서 fit함수 내에서 1000번 에포크를 수행했던 부분을 한 번 에포크를 수행하는 fit함수를 천 번 호출하는 식으로 수정했었다.
#참고로 fit함수를 한 번 호출해서 에포크를 여러번 수행하는 것과 fit함수를 여러 번 호출하는 것은 동일한 효과를 얻을 수 있다.


''''''
import keras

# 사용자 정의 히스토리 클래스 정의
class CustomHistory(keras.callbacks.Callback):
    def init(self):
        self.train_loss = []
        self.val_loss = []
        self.train_acc = []
        self.val_acc = []        
        
    def on_epoch_end(self, batch, logs={}):
        self.train_loss.append(logs.get('loss'))
        self.val_loss.append(logs.get('val_loss'))
        self.train_acc.append(logs.get('accuracy'))
        self.val_acc.append(logs.get('val_accuracy'))
    
# 모델 학습시키기

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

custom_hist = CustomHistory()
custom_hist.init()

for epoch_idx in range(1000):
    print ('epochs : ' + str(epoch_idx) )
    model.fit(X_train, Y_train, epochs=1, batch_size=10, validation_data=(X_val, Y_val), callbacks=[custom_hist])

# 5. 모델 학습 과정 표시하기
'''
%matplotlib inline
Jupyter IPython 노트북을 사용하지 않는경우 줄을 주석처리(또는 삭제)하면 모든것이 잘 작동하며 콘솔에서 Python스크립트를 실행하는 경우 별도의 플롯창이 열린다.
그러나 Jupyter IPython 노트북을 사용하는 경우 노트북의 첫 번째 Python 코드셀에 "%matplotlib inline"줄이 있어야 플롯을 볼 수 있다.
'''
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(custom_hist.train_loss, 'y', label='train loss')
loss_ax.plot(custom_hist.val_loss, 'r', label='val loss')

acc_ax.plot(custom_hist.train_acc, 'b', label='train acc')
acc_ax.plot(custom_hist.val_acc, 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
