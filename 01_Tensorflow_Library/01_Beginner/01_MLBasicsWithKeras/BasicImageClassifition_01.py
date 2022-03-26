#운동화나 셔츠같은 옷 이미지를 분류하는 신경망 모델을 훈련2
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
#4개의 파일[(train_images, train_labels), (test_images, test_labels)]을 다 다운로드 해줘야 한다.

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#처음 실행하면, 데이터를 읽어들이는 과정이 진행되며 다음 실행에는 위와 같은 위치에 있는 데이터를 읽어서 빠르게 수행된다.

train_images = train_images / 255.0
test_images = test_images / 255.0

''''''
#모델구성
#신경망 모델을 만들려면 모델의 층을 구성한 다음 모델을 컴파일한다.

#층 설정
#신경망의 기본 구성 요소는 층(layer)이다.
#층은 주입된 데이터에서 표현을 추출한다.
#아마도 문제를 해결하는데 더 의미있는 표현이 추출될 것이다.

#대부분 딥러닝은 간단한 층을 연결하여 구성된다.
#tf.keras.layers.Dense와 같은 층들의 가중치(parameter)는 훈련하는 동안 학습된다.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # flatten을 사용하여 2차원의 배열을 1차원의 배열 값으로 변경
    keras.layers.Dense(128, activation='relu'),  # relu 활성화 함수를 사용하고, 128개의 노드를 가진 신경망 층
    keras.layers.Dense(10, activation='softmax') # 10개의 레이블 값을 가진 output layer, softmax로 확률로 변형
])

#이 네트워크의 첫 번째 층인 tf.keras.layers.Flatten은 2차원 배열(28x28 픽셀)의 이미지 포맷을 28*28=784 픽셀의 1차원 배열로 변환한다.
#이 층은 이미지에 있는 픽셀의 행을 펼쳐서 일렬로 늘린다.
#이 층에는 학습되는 가중치가 없고 데이터를 변환하기만 한다.

#픽셀을 펼친 후에는 두 개의 tf.keras.layers.Dense 층이 연속되어 연결된다.
#이 층을 밀집연결(densely-connected) 또는 완전연결(fully-connected) 층이라고 부른다.
#첫 번째 Dense 층은 128개의 노드(또는 뉴런)를 가진다. 
#두 번째 (마지막) 층은 10개의 노드의 소프트맥스(softmax) 층이다.
#이 층은 10개의 확률을 반환하고 반환된 값의 전체 합은 1이다.
#각 노드는 현재 이미지가 10개 클래스 중 하나에 속할 확률을 출력한다.

#모델 컴파일
#모델을 훈련하기 전에 필요한 몇 가지 설정이 모델 컴파일 단계에서 추가된다.
#    - 손실 함수(Loss function) : 훈련 하는 동안 모델의 오차를 측정한다. 모델의 학습이 올바른 방향으로 향하도록 이 함수를 최소화해야 한다.
#    - 옵티마이저(Optimizer)    :데이터와 손실 함수를 바탕으로 모델의 업데이트 방법을 결정한다.
#    - 지표(Metrics)           : 훈련 단계와 테스트 단계를 모니터링하기 위해 사용한다.
#다음 예에서는 올바르게 분류된 이미지의 비율인 정확도를 사용힌다.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#모델 훈련
#신경망 모델을 훈련하는 단계는 다음과 같다.
#   1. 훈련 데이터를 모델에 주입한다- 이 예에서는 train_images와 train_labels 배열이다.
#   2. 모델이 이미지와 레이블을 매핑하는 방법을 배운다.
#   3. 테스트 세트에 대한 모델의 예측을 만든다.(이 예에서는 test_images 배열이다)
#   4. 이 예측이 test_labels 배열의 레이블과 맞는지 확인한다.
#훈련을 시작하기 위해 model.fit 메서드를 호출하면 모델이 훈련 데이터를 학습한다.
model.fit(train_images, train_labels, epochs=5)
#모델이 훈련되면서 손실과 정확도 지표가 출력된다.
#이 모델은 훈련 세트에서 약 0.88(88%) 정도의 정확도를 달성한다.

#정확도 평가
#그 다음 테스트 세트에서 모델의 성능을 비교한다.
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n테스트 정확도:', test_acc)
#테스트 세트의 정확도가 훈련 세트의 정확도보다 조금 낮다.
#훈련 세트의 정확도와 테스트 세트의 정확도 사이의 차이는 과대적합(overfitting) 때문이다.
#과대적합은 머신러닝 모델이 훈련 데이터보다 새로운 데이터에서 성능이 낮아지는 현상을 말한다.
