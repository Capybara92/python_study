#학습모델 보기, 저장하기, 불러오기3

#학습된 모델 저장하기
#모델은 크게 「모델 아키텍처」와 「모델 가중치」로 구성된다. 
#「모델 아키텍처」는 모델이 어떤 층으로 어떻게 쌓여있는 지에 대한 모델구성이 정의되어 있고, 
#「모델 가중치」는 처음에는 임의의 값으로 초기화되어 있지만, 훈련셋으로 학습하면서 갱신된다.
#학습된 모델을 저장한다는 말은 「모델 아키텍처」와 「모델 가중치」를 저장한다는 말이다. 
#케라스에서는 save()함수 하나로 「모델 아키텍처」와 「모델 가중치」를 「h5」파일형식으로 모두 저장할 수 있다.
'''
from keras.models import load_model
model.save('mnist_mlp_model.h5')
'''

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
x_val = x_train[42000:] # 훈련셋의 30%를 검증셋으로 사용
x_train = x_train[:42000]
y_val = y_train[42000:] # 훈련셋의 30%를 검증셋으로 사용
y_train = y_train[:42000]

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

# 6. 모델 저장하기
from keras.models import load_model
model.save('mnist_mlp_model.h5')

#저장된 파일에는 다음의 정보가 담겨 있다.
#   - 나중에 모델을 재구성하기 위한 모델의 구성 정보
#   - 모델를 구성하는 각 뉴런들의 가중치
#   - 손실함수, 최적하기 등의 학습 설정
#   - 재학습을 할 수 있도록 마지막 학습 상태


''''''
#모델 아키텍처 보기
from IPython.display import SVG #IPython을 다운받으라고 에러가 나옴
from keras.utils.vis_utils import model_to_dot
#%matplotlib inline

#pydot 라이브러리가 필요하다고 에러가 나옴(pip설치)
#graphvis 라이브러리가 필요하다고 에러가 나옴(conda설치)
'''pydot는 현재 개발이 그쳤고 python3.5 및 3.6에서는 동작하지 않는다.'''
#SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))
#그래서 에러가 난다.
#OSError `pydot` failed to call GraphViz.Please install GraphViz (https://www.graphviz.org/) and ensure that its executables are in the $PATH.
#위의 내용의 에러는 스크립트 코드에서 나는 에러이므로, jupyter notebook에서 해보도록 한다.


''''''
#Your CPU supports instructions that this TensorFlow binary was not compiled to use : AVX2 FMA 에러
#CPU로 AVX2, FMA 명령어를 사용할 수 있지만,이 바이너리는 그것을 사용하도록 컴파일되어 있지 않기 때문에 사용할 수 없다는 메시지이다.
#pip로 설치되는 바이너리는 이러한 CPU 명령을 사용하여 빌드되지 않는다.
#특히 오류 등 문제가 있음을 나타내는 것은 아니기 때문에 무시해도 된다.
