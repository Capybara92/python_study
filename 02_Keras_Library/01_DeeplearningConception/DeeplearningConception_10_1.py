#DeeplearningConception_10_0에서 「model_to_dot」 「SVG」 「graphviz」 「pydot」로 하려 했지만 계속 에러가나서
#plot_model로 한다.

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from tensorflow.keras.utils import plot_model

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
x_val = x_train[42000:] # 훈련셋의 30%를 검증셋으로 사용
x_train = x_train[:42000]
y_val = y_train[42000:] # 훈련셋의 30%를 검증셋으로 사용
y_train = y_train[:42000]

# 2. 모델 구성하기
model = Sequential()
model.add(Dense(units=64, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# 3. 모델 시각화
plot_model(model, to_file='model.png')
plot_model(model, to_file='model_shapes.png', show_shapes=True) #show_shapes을 True로 설정하면 층의 형태를 함께 시각화한다.
# .png파일로 그 해당 폴더에 저장이 된다.
