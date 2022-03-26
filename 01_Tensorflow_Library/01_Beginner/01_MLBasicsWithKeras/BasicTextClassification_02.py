#영화리뷰 텍스트를 긍정 또는 부정으로 분류3.

import tensorflow as tf
from tensorflow import keras
import numpy as np

imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()

word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                        value=word_index["<PAD>"],
                                                        padding='post',
                                                        maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                       value=word_index["<PAD>"],
                                                       padding='post',
                                                       maxlen=256)

vocab_size = 10000

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16, input_shape=(None,)))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()

''''''
#손실함수와 옵티마이저
#모델이 훈련하려면 손실함수(loss function)와 옵티마이저(optimizer)가 필요히다.
#이 예제는 이진분류 문제이고 모델이 확률을 출력하므로(출력층의 유닛이 하나이고 sigmoid 활성화 함수를 사용한다), binary_crossentropy 손실함수를 사용한다.

#다른 손실함수를 선택할 수 없는 것은 아니다.
#예를들어, mean_squared_error를 선택할 수 있다.
#하지만 일반적으로 binary_crossentropy가 확률을 다루는데는 적합하다.
#이 함수는 확률분포 간의 거리를 측정한다.
#여기에서는 정답인 타깃분포와 예측분포 사이의 거리이다.

#나중에 회귀(regression)문제(예를들어, 주택가격을 예측하는 문제)에 대해 살펴볼 때 평균제곱오차(mean squared error) 손실함수를 어떻게 사용하는지 알아본다.

#이제 모델이 사용할 옵티마이저와 손실 함수를 설정
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    
''''''
#검증세트 만들기
#모델을 훈련할 때 모델이 만난 적 없는 데이터에서 정확도를 확인하는 것이 좋다.
#원본 훈련 데이터에서 10,000개의 샘플을 떼어내어 검증세트(validation set)를 만든다.
#(왜 테스트세트를 사용하지 않을까요? 훈련데이터만을 사용하여 모델을 개발하고 튜닝하는 것이 목표입니다. 그 다음 테스트세트를 사용해서 딱 한 번만 정확도를 평가한다.)
x_val = train_data[:10000]
partial_x_train = train_data[10000:]

y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

''''''
#모델훈련
#이 모델을 512개의 샘플로 이루어진 미니배치(mini-batch)에서 40번의 에포크(epoch)동안 훈련한다.
#x_train과 y_train 텐서에 있는 모든샘플에 대해 40번 반복한다는 뜻이다.
#훈련하는 동안 10,000개의 검증세트에서 모델의 손실과 정확도를 모니터링한다.
history = model.fit(partial_x_train, #입력데이터
                    partial_y_train, #정답데이터
                    epochs=40,
                    batch_size=512,  #몇개의 입력데이터를 받고 정답데이터랑 비교할지의 수(512개를 비교 후 가중치갱신)
                    validation_data=(x_val, y_val),
                    verbose=1)

''''''
#모델평가
#모델의 성능을 확인해 보자.
#두 개의 값이 반환된다.
#손실(오차를 나타내는 숫자이므로 낮을수록 좋습니다)과 정확도이다.
results = model.evaluate(test_data,  test_labels, verbose=2)
print(results)
#이 예제는 매우 단순한방식을 사용하므로 87%정도의 정확도를 달성했다.
#고급방법을 사용한 모델은 95%에 가까운 정확도를 얻는다.
